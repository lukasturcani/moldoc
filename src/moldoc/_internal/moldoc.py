import os
import pkgutil
import typing

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.writers.html5 import HTML5Translator

from moldoc._internal.javascript.atoms import get_atom_array
from moldoc._internal.javascript.bonds import get_bond_array
from moldoc._internal.javascript.mesh_config import get_mesh_config
from moldoc._internal.javascript.scene_config import get_scene_config
from moldoc.molecule import Molecule, MoleculeConfig
from moldoc.version import __version__


class MolDocNode(nodes.Body, nodes.Element):
    def __init__(
        self,
        moldoc_name: str,
        molecule: Molecule,
    ) -> None:
        super().__init__()
        self._moldoc_name = moldoc_name
        self._molecule = molecule

    def get_molecule(self) -> Molecule:
        return self._molecule

    def get_moldoc_name(self) -> str:
        return self._moldoc_name


class MolDoc(SphinxDirective):
    has_content = True

    def run(self) -> list[MolDocNode]:
        content = "\n".join(self.content)
        globals_: dict[str, typing.Any] = {}
        exec(content, globals_)
        node = MolDocNode(
            moldoc_name=f'moldoc_{self.env.new_serialno("moldoc")}',
            molecule=globals_["moldoc_display_molecule"],
        )
        return [node]


def html_moldoc(self: HTML5Translator, node: MolDocNode) -> None:
    molecule = node.get_molecule()

    default_molecule_config = self.config.moldoc_default_molecule_config
    if (config := molecule.get_config()) is not None:
        molecule_config = default_molecule_config.update(config)
    else:
        molecule_config = default_molecule_config

    moldoc_node_id = node.get_moldoc_name()

    if not getattr(self, "moldoc_scripts_added", False):
        self.body.append(
            '<script src="three.min.js"></script>'
            '<script src="molDraw.js"></script>'
            '<script src="../three.min.js"></script>'
            '<script src="../molDraw.js"></script>'
            "<script>const md=molDraw;"
            "let atoms=[];"
            "let bonds=[];"
            "let maybeMolecule=undefined;"
            "</script>"
        )
        self.moldoc_scripts_added = True

    content = (
        f"atoms={get_atom_array(molecule.get_atoms())};"
        f"bonds={get_bond_array(molecule.get_bonds())};"
        "maybeMolecule=md.maybeMolecule(atoms)(bonds);"
        "if (md.isLeft(maybeMolecule))"
        "{"
        'console.log("There was an issue with your molecule.");'
        "console.log(md.fromLeft()(maybeMolecule));"
        "}"
        "else"
        "{"
        "const molecule=md.fromRight()(maybeMolecule);"
        "const scene=md.scene({"
        f"{get_scene_config(moldoc_node_id, molecule_config)}"
        "});"
        "const meshes=md.meshes({"
        f"{get_mesh_config(molecule, molecule_config)}"
        "})(molecule);"
        "md.drawMol(scene(meshes));"
        "}"
    )

    self.body.append(
        f'<div id="{moldoc_node_id}" style="height:25vh;"></div>'
        f"<script>{content}</script>"
    )
    raise nodes.SkipNode


def copy_asset_files(app: Sphinx, exc: Exception | None) -> None:
    asset_files = (
        "molDraw.js",
        "three.min.js",
    )
    static_dir = os.path.join(app.builder.outdir, "_static")
    # Build is HTML and succeeded.
    if app.builder.format == "html" and exc is None:
        for path in asset_files:
            with open(os.path.join(static_dir, path), "wb") as f:
                if (data := pkgutil.get_data(__package__, path)) is not None:
                    f.write(data)
                else:
                    raise RuntimeError(f"{path} not found")


def setup(app: Sphinx) -> dict:
    app.connect("build-finished", copy_asset_files)
    app.add_directive("moldoc", MolDoc)
    app.add_node(
        node=MolDocNode,
        html=(html_moldoc, None),
    )
    app.add_config_value(
        "moldoc_default_molecule_config",
        MoleculeConfig(),
        "html",
        [MoleculeConfig],
    )
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
