from __future__ import annotations

from typing import Iterable, Optional


class Color:
    def __init__(self, red: int, green: int, blue: int) -> None:
        self._red = red
        self._green = green
        self._blue = blue

    def get_red(self) -> int:
        return self._red

    def get_green(self) -> int:
        return self._green

    def get_blue(self) -> int:
        return self._blue


class AtomConfig:
    def __init__(
        self,
        color: Optional[Color] = None,
        size: Optional[float] = None,
    ) -> None:

        self._color = color
        self._size = size

    def get_color(self) -> Optional[Color]:
        return self._color

    def get_size(self) -> Optional[float]:
        return self._size


class Atom:
    def __init__(
        self,
        atomic_number: int,
        position: tuple[float, float, float],
        config: Optional[AtomConfig] = None,
    ) -> None:

        self._atomic_number = atomic_number
        self._position = position
        self._config = config

    def get_atomic_number(self) -> int:
        return self._atomic_number

    def get_position(self) -> tuple[float, float, float]:
        return self._position

    def get_config(self) -> Optional[AtomConfig]:
        return self._config


class Bond:
    def __init__(
        self,
        atom1_id: int,
        atom2_id: int,
        order: int,
    ) -> None:

        self._atom1_id = atom1_id
        self._atom2_id = atom2_id
        self._order = order

    def get_atom1_id(self) -> int:
        return self._atom1_id

    def get_atom2_id(self) -> int:
        return self._atom2_id

    def get_order(self) -> int:
        return self._order


class Material:
    pass


class MeshLambertMaterial(Material):
    pass


class MeshNormalMaterial(Material):
    pass


class MeshPhongMaterial(Material):
    def __init__(
        self,
        shininess: Optional[float] = None,
        reflectivity: Optional[float] = None,
        flat_shading: Optional[bool] = None,
    ) -> None:

        self._shininess = shininess
        self._reflectivity = reflectivity
        self._flat_shading = flat_shading

    def get_shininess(self) -> Optional[float]:
        return self._shininess

    def get_reflectivity(self) -> Optional[float]:
        return self._reflectivity

    def get_flat_shading(self) -> Optional[bool]:
        return self._flat_shading


class MeshPhysicalMaterial(Material):
    def __init__(
        self,
        clearcoat: Optional[float] = None,
        clearcoat_roughness: Optional[float] = None,
        roughness: Optional[float] = None,
        metalness: Optional[float] = None,
        reflectivity: Optional[float] = None,
        flat_shading: Optional[bool] = None,
    ) -> None:

        self._clearcoat = clearcoat
        self._clearcoat_roughness = clearcoat_roughness
        self._roughness = roughness
        self._metalness = metalness
        self._reflectivity = reflectivity
        self._flat_shading = flat_shading

    def get_clearcoat(self) -> Optional[float]:
        return self._clearcoat

    def get_clearcoat_roughness(self) -> Optional[float]:
        return self._clearcoat_roughness

    def get_roughness(self) -> Optional[float]:
        return self._roughness

    def get_metalness(self) -> Optional[float]:
        return self._metalness

    def get_reflectivity(self) -> Optional[float]:
        return self._reflectivity

    def get_flat_shading(self) -> Optional[bool]:
        return self._flat_shading


class MeshStandardMaterial(Material):
    def __init__(
        self,
        metalness: Optional[float] = None,
        roughness: Optional[float] = None,
        flat_shading: Optional[bool] = None,
    ) -> None:

        self._metalness = metalness
        self._roughness = roughness
        self._flat_shading = flat_shading

    def get_metalness(self) -> Optional[float]:
        return self._metalness

    def get_roughness(self) -> Optional[float]:
        return self._roughness

    def get_flat_shading(self) -> Optional[bool]:
        return self._flat_shading


class MeshToonMaterial(Material):
    pass


class MoleculeConfig:
    def __init__(
        self,
        atom_scale: Optional[float] = None,
        material: Optional[Material] = None,
        background_color: Optional[Color] = None,
        is_outlined: Optional[bool] = None
    ) -> None:

        self._atom_scale = atom_scale
        self._material = material
        self._background_color = background_color
        self._is_outlined = is_outlined

    def get_atom_scale(self) -> Optional[float]:
        return self._atom_scale

    def get_material(self) -> Optional[Material]:
        return self._material

    def get_background_color(self) -> Optional[Color]:
        return self._background_color

    def is_outlined(self) -> Optional[bool]:
        return self._is_outlined


class Molecule:
    def __init__(
        self,
        atoms: Iterable[Atom],
        bonds: Iterable[Bond],
        config: Optional[MoleculeConfig] = None,
    ) -> None:

        self._atoms = tuple(atoms)
        self._bonds = tuple(bonds)
        self._config = config

    def get_atoms(self) -> tuple[Atom, ...]:
        return self._atoms

    def get_bonds(self) -> tuple[Bond, ...]:
        return self._bonds

    def get_config(self) -> Optional[MoleculeConfig]:
        return self._config
