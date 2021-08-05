from typing import Iterable

from ..molecule import Bond


def get_bond_array(
    bonds: Iterable[Bond],
) -> str:

    bonds_js = ','.join(map(_bond_to_javascript, bonds))
    return f'[{bonds_js}]'


def _bond_to_javascript(bond: Bond) -> str:
    return (
        'md.bond'
        f'({bond.get_order()})'
        f'({bond.get_atom1_id()})'
        f'({bond.get_atom2_id()})'
    )
