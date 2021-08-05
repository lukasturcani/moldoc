from typing import Optional

from .color import color_to_javascript
from .bool import bool_to_javascript
from ..molecule import MoleculeConfig


def get_scene_config(
    container_id: str,
    molecule_config: Optional[MoleculeConfig],
) -> str:

    scene_config = {
        "containerId": f'"{container_id}"',
        **_get_scene_config(molecule_config)
    }

    return ",".join(
        f'{key}:{value}' for key, value in scene_config.items()
    )


def _get_scene_config(config: Optional[MoleculeConfig]) -> dict:
    result = {}

    if config is None:
        return result

    background_color = config.get_background_color()
    if background_color is not None:
        result['backgroundColor'] = color_to_javascript(
            color=background_color,
        )

    is_outlined = config.is_outlined()
    if is_outlined is not None:
        result['outline'] = bool_to_javascript(is_outlined)

    return result
