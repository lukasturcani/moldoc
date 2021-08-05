from typing import Optional, Iterable

from .color import color_to_javascript
from .material import material_to_javascript
from ..molecule import Atom, Molecule, MoleculeConfig


def get_mesh_config(
    molecule: Molecule,
) -> str:

    mesh_config = []
    atoms = molecule.get_atoms()

    atom_size_function = _get_atom_size_function(atoms)
    if atom_size_function is not None:
        mesh_config.append(atom_size_function)

    atom_color_function = _get_atom_color_function(atoms)
    if atom_color_function is not None:
        mesh_config.append(atom_color_function)

    molecule_config = molecule.get_config()
    if molecule_config is not None:
        atom_scale = molecule_config.get_atom_scale()
        if atom_scale is not None:
            mesh_config.append(f'atomScale:{atom_scale}')

        material = molecule_config.get_material()
        if material is not None:
            mesh_config.append(material_to_javascript(material))

    return ",".join(mesh_config)


def _get_atom_size_function(
    atoms: Iterable[Atom],
) -> Optional[str]:

    atom_size_cases = tuple(_get_atom_size_cases(atoms))
    if atom_size_cases:
        return (
            'atomSize:atom=>{switch(md.id(atom)){'
            f'{"".join(atom_size_cases)}'
            'default:return md.size(md.chemicalSymbol(atom));'
            '}}'
        )

    return None


def _get_atom_size_cases(
    atoms: Iterable[Atom],
) -> Iterable[str]:

    for atom_id, atom in enumerate(atoms):
        config = atom.get_config()
        if config is not None:
            size = config.get_size()
            if size is not None:
                yield f'case {atom_id}:return {size};'


def _get_atom_color_function(
    atoms: Iterable[Atom],
) -> Optional[str]:

    atom_color_cases = tuple(_get_atom_color_cases(atoms))
    if atom_color_cases:
        return (
            'atomColor:atom=>{switch(md.id(atom)){'
            f'{"".join(atom_color_cases)}'
            'default:return md.color(md.chemicalSymbol(atom));'
            '}}'
        )
    return None


def _get_atom_color_cases(
    atoms: Iterable[Atom],
) -> Iterable[str]:

    for atom_id, atom in enumerate(atoms):
        config = atom.get_config()
        if config is not None:
            color = config.get_color()
            if color is not None:
                color_js = color_to_javascript(color)
                yield f'case {atom_id}:return {color_js};'


def _molecule_config_to_javascript(
    config: Optional[MoleculeConfig],
) -> Optional[str]:

    if config is None:
        return None

    javascript = []

    material = config.get_material()
    if material is not None:
        javascript.append(material_to_javascript(material))

    if javascript:
        return ','.join(javascript)

    return None
