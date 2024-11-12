import pkgutil
import typing

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
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
        exec(content, globals_)  # noqa: S102
        node = MolDocNode(
            moldoc_name=f'moldoc_{self.env.new_serialno("moldoc")}',
            molecule=globals_["moldoc_display_molecule"],
        )

        if not hasattr(self.env, "moldoc_documents"):
            self.env.moldoc_documents = set()  # type: ignore[attr-defined]

        self.env.moldoc_documents.add(self.env.docname)  # type: ignore[attr-defined]
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
        self.body.append("<script>let moldoc_molecules=[];</script>")
        self.moldoc_scripts_added = True

    content = (
        "{"
        "const drawMol = () => {"
        "const md = molDraw;"
        f"let atoms={get_atom_array(molecule.get_atoms())};"
        f"let bonds={get_bond_array(molecule.get_bonds())};"
        "let maybeMolecule=md.maybeMolecule(atoms)(bonds);"
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
        "};"
        "if (typeof molDraw === 'undefined') { "
        "moldoc_molecules.push(drawMol); } else { drawMol() }"
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
    static_dir = app.builder.outdir / "_static"
    # Build is HTML and succeeded.
    if app.builder.format == "html" and exc is None:
        for path in asset_files:
            with static_dir.joinpath(path).open("wb") as f:
                if (data := pkgutil.get_data(__package__, path)) is not None:
                    f.write(data)
                else:
                    msg = f"{path} not found"
                    raise RuntimeError(msg)


def add_moldoc_scripts(
    app: Sphinx,
    pagename: str,
    templatename: str,  # noqa: ARG001
    context: dict[str, typing.Any],  # noqa: ARG001
    doctree: nodes.document,  # noqa: ARG001
) -> None:
    if (
        hasattr(app.env, "moldoc_documents")
        and pagename in app.env.moldoc_documents
    ):
        app.add_js_file("three.min.js")
        app.add_js_file("molDraw.js")
        app.add_js_file(None, body="moldoc_molecules.forEach(f=>f());")


def purge_moldoc_documents(
    app: Sphinx,  # noqa: ARG001
    env: BuildEnvironment,
    docnames: list[str],
) -> None:
    if hasattr(env, "moldoc_documents"):
        env.moldoc_documents.difference_update(docnames)


def merge_moldoc_documents(
    app: Sphinx,  # noqa: ARG001
    env: BuildEnvironment,
    docnames: list[str],  # noqa: ARG001
    other: BuildEnvironment,
) -> None:
    if not hasattr(env, "moldoc_documents"):
        env.moldoc_documents = set()  # type: ignore[attr-defined]
    if hasattr(other, "moldoc_documents"):
        env.moldoc_documents.update(other.moldoc_documents)  # type: ignore[attr-defined]


def setup(app: Sphinx) -> dict:
    app.connect("build-finished", copy_asset_files)
    app.connect("html-page-context", add_moldoc_scripts)
    app.connect("env-purge-doc", purge_moldoc_documents)
    app.connect("env-merge-info", merge_moldoc_documents)
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
