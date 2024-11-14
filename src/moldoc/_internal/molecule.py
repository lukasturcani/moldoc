from collections.abc import Iterable


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
        color: Color | None = None,
        size: float | None = None,
    ) -> None:
        self._color = color
        self._size = size

    def get_color(self) -> Color | None:
        return self._color

    def get_size(self) -> float | None:
        return self._size


class Atom:
    def __init__(
        self,
        atomic_number: int,
        position: tuple[float, float, float],
        config: AtomConfig | None = None,
    ) -> None:
        self._atomic_number = atomic_number
        self._position = position
        self._config = config

    def get_atomic_number(self) -> int:
        return self._atomic_number

    def get_position(self) -> tuple[float, float, float]:
        return self._position

    def get_config(self) -> AtomConfig | None:
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


class MeshLambertMaterial:
    pass


class MeshNormalMaterial:
    pass


class MeshPhongMaterial:
    def __init__(
        self,
        shininess: float | None = None,
        reflectivity: float | None = None,
        flat_shading: bool | None = None,
    ) -> None:
        self._shininess = shininess
        self._reflectivity = reflectivity
        self._flat_shading = flat_shading

    def get_shininess(self) -> float | None:
        return self._shininess

    def get_reflectivity(self) -> float | None:
        return self._reflectivity

    def get_flat_shading(self) -> bool | None:
        return self._flat_shading


class MeshPhysicalMaterial:
    def __init__(  # noqa: PLR0913
        self,
        clearcoat: float | None = None,
        clearcoat_roughness: float | None = None,
        roughness: float | None = None,
        metalness: float | None = None,
        reflectivity: float | None = None,
        flat_shading: bool | None = None,
    ) -> None:
        self._clearcoat = clearcoat
        self._clearcoat_roughness = clearcoat_roughness
        self._roughness = roughness
        self._metalness = metalness
        self._reflectivity = reflectivity
        self._flat_shading = flat_shading

    def get_clearcoat(self) -> float | None:
        return self._clearcoat

    def get_clearcoat_roughness(self) -> float | None:
        return self._clearcoat_roughness

    def get_roughness(self) -> float | None:
        return self._roughness

    def get_metalness(self) -> float | None:
        return self._metalness

    def get_reflectivity(self) -> float | None:
        return self._reflectivity

    def get_flat_shading(self) -> bool | None:
        return self._flat_shading


class MeshStandardMaterial:
    def __init__(
        self,
        metalness: float | None = None,
        roughness: float | None = None,
        flat_shading: bool | None = None,
    ) -> None:
        self._metalness = metalness
        self._roughness = roughness
        self._flat_shading = flat_shading

    def get_metalness(self) -> float | None:
        return self._metalness

    def get_roughness(self) -> float | None:
        return self._roughness

    def get_flat_shading(self) -> bool | None:
        return self._flat_shading


type Material = (
    MeshLambertMaterial
    | MeshNormalMaterial
    | MeshPhongMaterial
    | MeshPhysicalMaterial
    | MeshStandardMaterial
)


class MoleculeConfig:
    def __init__(
        self,
        atom_scale: float | None = None,
        material: Material | None = None,
        background_color: Color | None = None,
        is_outlined: bool | None = None,
    ) -> None:
        self._atom_scale = atom_scale
        self._material = material
        self._background_color = background_color
        self._is_outlined = is_outlined

    def get_atom_scale(self) -> float | None:
        return self._atom_scale

    def get_material(self) -> Material | None:
        return self._material

    def get_background_color(self) -> Color | None:
        return self._background_color

    def is_outlined(self) -> bool | None:
        return self._is_outlined

    def update(self, other: "MoleculeConfig") -> "MoleculeConfig":
        atom_scale = (
            self._atom_scale
            if other.get_atom_scale() is None
            else other.get_atom_scale()
        )
        material = (
            self._material
            if other.get_material() is None
            else other.get_material()
        )
        background_color = (
            self._background_color
            if other.get_background_color() is None
            else other.get_background_color()
        )
        is_outlined = (
            self._is_outlined
            if other.is_outlined() is None
            else other.is_outlined()
        )
        return MoleculeConfig(
            atom_scale=atom_scale,
            material=material,
            background_color=background_color,
            is_outlined=is_outlined,
        )


class Molecule:
    def __init__(
        self,
        atoms: Iterable[Atom],
        bonds: Iterable[Bond],
        config: MoleculeConfig | None = None,
    ) -> None:
        self._atoms = tuple(atoms)
        self._bonds = tuple(bonds)
        self._config = config

    def get_atoms(self) -> tuple[Atom, ...]:
        return self._atoms

    def get_bonds(self) -> tuple[Bond, ...]:
        return self._bonds

    def get_config(self) -> MoleculeConfig | None:
        return self._config
