from __future__ import annotations

import os
from docutils import nodes
from docutils.parsers.rst import Directive
import pkgutil

from typing import Iterable
from .molecule import Atom, Bond, Molecule


class MolDocNode(nodes.Body, nodes.Element):
    def __init__(self, molecule: Molecule) -> None:
        super().__init__()
        self._molecule = molecule

    def get_molecule(self) -> Molecule:
        return self._molecule


class MolDoc(Directive):
    has_content = True

    def run(self):
        content = '\n'.join(self.content)
        locals_ = {}
        globals_ = {}
        exec(content, globals_, locals_)
        node = MolDocNode(locals_['moldoc_display_molecule'])
        return [node]


def _atom_to_javascript(atom: Atom) -> str:
    x, y, z = atom.get_position()
    symbol = _symbols[atom.get_atomic_number()]
    return f'md.atom(md.{symbol})( md.position({x})({y})({z}))'


def _atoms_to_javascript(
    atoms: Iterable[Atom],
) -> str:

    atoms = ','.join(map(_atom_to_javascript, atoms))
    return f'const atoms = [{atoms}];'


def _bond_to_javascript(bond: Bond) -> str:
    return (
        'md.bond'
        f'({bond.get_order()})'
        f'({bond.get_atom1_id()})'
        f'({bond.get_atom2_id()})'
    )


def _bonds_to_javascript(
    bonds: Iterable[Bond],
) -> str:

    bonds = ','.join(map(_bond_to_javascript, bonds))
    return f'const bonds = [{bonds}];'


def html_moldoc(self, node: MolDocNode):
    molecule = node.get_molecule()

    render = r'''
        if (md.isLeft(maybeMolecule))
        {
            console.log('There was an issue with your molecule.');
            console.log(md.fromLeft()(maybeMolecule));
        }
        else
        {
            const molecule = md.fromRight()(maybeMolecule);
            const scene = md.scene({ containerId: 'moldoc' });
            const meshes = md.meshes({})(molecule);
            md.drawMol(scene(meshes));
        }'''

    content = f'''
        const md = molDraw;
        {_atoms_to_javascript(molecule.get_atoms())}
        {_bonds_to_javascript(molecule.get_bonds())}
        const maybeMolecule = md.maybeMolecule(atoms)(bonds);
        {render}
    '''

    self.body.append(
        '<script src="_static/three.min.js"></script>'
        '<script src="_static/molDraw.js"></script>'
        '<div id="moldoc" style="height:25vh;"></div>'
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


_symbols = {
    1: 'h',
    2: 'he',
    3: 'li',
    4: 'be',
    5: 'b',
    6: 'c',
    7: 'n',
    8: 'o',
    9: 'f',
    10: 'ne',
    11: 'na',
    12: 'mg',
    13: 'al',
    14: 'si',
    15: 'p',
    16: 's',
    17: 'cl',
    18: 'ar',
    19: 'k',
    20: 'ca',
    21: 'sc',
    22: 'ti',
    23: 'v',
    24: 'cr',
    25: 'mn',
    26: 'fe',
    27: 'co',
    28: 'ni',
    29: 'cu',
    30: 'zn',
    31: 'ga',
    32: 'ge',
    33: 'as',
    34: 'se',
    35: 'br',
    36: 'kr',
    37: 'rb',
    38: 'sr',
    39: 'y',
    40: 'zr',
    41: 'nb',
    42: 'mo',
    43: 'tc',
    44: 'ru',
    45: 'rh',
    46: 'pd',
    47: 'ag',
    48: 'cd',
    49: 'in_',
    50: 'sn',
    51: 'sb',
    52: 'te',
    53: 'i',
    54: 'xe',
    55: 'cs',
    56: 'ba',
    72: 'hf',
    73: 'ta',
    74: 'w',
    75: 're',
    76: 'os',
    77: 'ir',
    78: 'pt',
    79: 'au',
    80: 'hg',
    81: 'tl',
    82: 'pb',
    83: 'bi',
    84: 'po',
    85: 'at',
    86: 'rn',
    87: 'fr',
    88: 'ra',
    104: 'rf',
    105: 'db',
    106: 'sg',
    107: 'bh',
    108: 'hs',
    109: 'mt',
    57: 'la',
    58: 'ce',
    59: 'pr',
    60: 'nd',
    61: 'pm',
    62: 'sm',
    63: 'eu',
    64: 'gd',
    65: 'tb',
    66: 'dy',
    67: 'ho',
    68: 'er',
    69: 'tm',
    70: 'yb',
    71: 'lu',
    89: 'ac',
    90: 'th',
    91: 'pa',
    92: 'u',
    93: 'np',
    94: 'pu',
    95: 'am',
    96: 'cm',
    97: 'bk',
    98: 'cf',
    99: 'es',
    100: 'fm',
    101: 'md',
    102: 'no',
    103: 'lr',
}
