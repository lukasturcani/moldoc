from typing import Optional, TypeVar

from .bool import bool_to_javascript
from ..molecule import (
    Material,
    MeshLambertMaterial,
    MeshNormalMaterial,
    MeshPhongMaterial,
    MeshPhysicalMaterial,
    MeshStandardMaterial,
    MeshToonMaterial,
)


def material_to_javascript(material: Material) -> str:
    # This is a type-safe switch
    return {  # type: ignore
        MeshLambertMaterial: _lambert_to_javascript,
        MeshNormalMaterial: _normal_to_javascript,
        MeshPhongMaterial: _phong_to_javascript,
        MeshPhysicalMaterial: _physical_to_javascript,
        MeshStandardMaterial: _standard_to_javascript,
        MeshToonMaterial: _toon_to_javascript,
    }[type(material)](material)


def _lambert_to_javascript(material: MeshLambertMaterial) -> str:
    return (
        'material:(color)=>'
        'new THREE.MeshLambertMaterial({color:color})'
    )


def _normal_to_javascript(material: MeshNormalMaterial) -> str:
    return 'material:(color)=>new THREE.MeshNormalMaterial()'


def _phong_to_javascript(
    material: MeshPhongMaterial,
) -> str:

    shininess = _property_to_javascript(
        property_name='shininess',
        property_value=material.get_shininess(),
    )
    reflectivity = _property_to_javascript(
        property_name='reflectivity',
        property_value=material.get_reflectivity(),
    )
    flat_shading = _property_to_javascript(
        property_name='flatShading',
        property_value=material.get_flat_shading(),
    )
    return (
        'material:'
        '(color)=>new THREE.MeshPhongMaterial({'
        'color:color'
        f'{"," if shininess else ""}{shininess}'
        f'{"," if reflectivity else ""}{reflectivity}'
        f'{"," if flat_shading else ""}{flat_shading}'
        '})'
    )


def _physical_to_javascript(
    material: MeshPhysicalMaterial,
) -> str:
    clearcoat = _property_to_javascript(
        property_name='clearcoat',
        property_value=material.get_clearcoat(),
    )
    clearcoat_roughness = _property_to_javascript(
        property_name='clearcoat_roughness',
        property_value=material.get_clearcoat_roughness(),
    )
    roughness = _property_to_javascript(
        property_name='roughness',
        property_value=material.get_roughness(),
    )
    metalness = _property_to_javascript(
        property_name='metalness',
        property_value=material.get_metalness(),
    )
    reflectivity = _property_to_javascript(
        property_name='reflectivity',
        property_value=material.get_reflectivity(),
    )
    flat_shading = _property_to_javascript(
        property_name='flat_shading',
        property_value=material.get_flat_shading(),
    )
    return (
        'material:'
        '(color)=>new THREE.MeshPhysicalMaterial({'
        'color:color'
        f'{"," if clearcoat else ""}{clearcoat}'
        f'{"," if clearcoat_roughness else ""}{clearcoat_roughness}'
        f'{"," if roughness else ""}{roughness}'
        f'{"," if metalness else ""}{metalness}'
        f'{"," if reflectivity else ""}{reflectivity}'
        f'{"," if flat_shading else ""}{flat_shading}'
        '})'
    )


def _standard_to_javascript(
    material: MeshStandardMaterial,
) -> str:
    metalness = _property_to_javascript(
        property_name='metalness',
        property_value=material.get_metalness(),
    )
    roughness = _property_to_javascript(
        property_name='roughness',
        property_value=material.get_roughness(),
    )
    flat_shading = _property_to_javascript(
        property_name='flatShading',
        property_value=material.get_flat_shading(),
    )
    return (
        'material:'
        '(color)=>new THREE.MeshStandardMaterial({'
        'color:color'
        f'{"," if metalness else ""}{metalness}'
        f'{"," if roughness else ""}{roughness}'
        f'{"," if flat_shading else ""}{flat_shading}'
        '})'
    )


def _toon_to_javascript(
    material: MeshToonMaterial,
) -> str:
    ...


T = TypeVar('T')


def _property_to_javascript(
    property_name: str,
    property_value: Optional[T],
) -> str:

    if property_value is None:
        return ''

    if isinstance(property_value, bool):
        return f'{property_name}:{bool_to_javascript(property_value)}'

    return f'{property_name}:{property_value}'
