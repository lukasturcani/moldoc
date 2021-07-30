from __future__ import annotations

from typing import Iterable


class Atom:
    def __init__(
        self,
        atomic_number: int,
        position: tuple[float, float, float],
    ) -> None:

        self._atomic_number = atomic_number
        self._position = position

    def get_atomic_number(self) -> int:
        return self._atomic_number

    def get_position(self) -> tuple[float, float, float]:
        return self._position


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


class Molecule:
    def __init__(
        self,
        atoms: Iterable[Atom],
        bonds: Iterable[Bond],
    ) -> None:

        self._atoms = tuple(atoms)
        self._bonds = tuple(bonds)

    def get_atoms(self) -> tuple[Atom, ...]:
        return self._atoms

    def get_bonds(self) -> tuple[Bond, ...]:
        return self._bonds
