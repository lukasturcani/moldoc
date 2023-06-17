from __future__ import annotations

import os
from docutils import nodes
from sphinx.util.docutils import SphinxDirective
import pkgutil

from .molecule import (
    Molecule,
)
from .javascript import (
    get_atom_array,
    get_bond_array,
    get_scene_config,
    get_mesh_config,
)


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

    def run(self):
        content = '\n'.join(self.content)
        globals_ = {}
        exec(content, globals_)
        node = MolDocNode(
            moldoc_name=f'moldoc_{self.env.new_serialno("moldoc")}',
            molecule=globals_['moldoc_display_molecule'],
        )
        return [node]


def html_moldoc(self, node: MolDocNode):
    molecule = node.get_molecule()
    moldoc_node_id = node.get_moldoc_name()

    if not getattr(self, 'moldoc_scripts_added', False):
        self.body.append(
            '<script src="/_static/three.min.js"></script>'
            '<script src="/_static/molDraw.js"></script>'
            '<script>const md=molDraw;'
            'let atoms=[];'
            'let bonds=[];'
            'let maybeMolecule=undefined;'
            '</script>'
        )
        self.moldoc_scripts_added = True

    content = (
        f'atoms={get_atom_array(molecule.get_atoms())};'
        f'bonds={get_bond_array(molecule.get_bonds())};'
        'maybeMolecule=md.maybeMolecule(atoms)(bonds);'
        'if (md.isLeft(maybeMolecule))'
        '{'
        'console.log("There was an issue with your molecule.");'
        'console.log(md.fromLeft()(maybeMolecule));'
        '}'
        'else'
        '{'
        'const molecule=md.fromRight()(maybeMolecule);'
        'const scene=md.scene({'
        f'{get_scene_config(moldoc_node_id, molecule.get_config())}'
        '});'
        'const meshes=md.meshes({'
        f'{get_mesh_config(molecule)}'
        '})(molecule);'
        'md.drawMol(scene(meshes));'
        '}'
    )

    self.body.append(
        f'<div id="{moldoc_node_id}" style="height:25vh;"></div>'
        f'<script>{content}</script>'
    )
    raise nodes.SkipNode


def copy_asset_files(app, exc) -> None:
    asset_files = (
        'molDraw.js',
        'three.min.js',
    )
    static_dir = os.path.join(app.builder.outdir, '_static')
    # Build is HTML and succeeded.
    if app.builder.format == 'html' and exc is None:
        for path in asset_files:
            with open(os.path.join(static_dir, path), 'wb') as f:
                f.write(pkgutil.get_data(__package__, path))


def setup(app):
    app.connect('build-finished', copy_asset_files)
    app.add_directive('moldoc', MolDoc)
    app.add_node(
        node=MolDocNode,
        html=(html_moldoc, None),
    )
    return {
        'version': '0.0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
