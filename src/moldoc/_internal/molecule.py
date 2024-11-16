from dataclasses import dataclass


@dataclass(slots=True)
class Atom:
    """An atom.

    Parameters:
        atomic_number: The atomic number of the atom.
        position: The position of the atom.
    """

    atomic_number: int
    """The atomic number of the atom."""
    position: tuple[float, float, float]
    """The position of the atom."""


@dataclass(slots=True)
class Simple:
    """A simple bond.

    Parameters:
        order: The order of the bond.

    """

    order: float
    """The order of the bond."""


@dataclass(slots=True)
class Dative:
    """A dative bond."""


@dataclass(slots=True)
class Bond:
    """A bond.

    Parameters:
        atom1: The first atom of the bond.
        atom2: The second atom of the bond.
        type: The type of bond.
    """

    atom1: int
    """The first atom of the bond."""
    atom2: int
    """The second atom of the bond."""
    type: Simple | Dative
    """The type of bond."""


@dataclass(slots=True)
class Molecule:
    """A molecule to render.

    Parameters:
        atoms: The atoms of the molecule.
        bonds: The bonds of the molecule.
    """

    atoms: list[Atom]
    """The atoms of the molecule."""
    bonds: list[Bond]
    """The bonds of the molecule."""
