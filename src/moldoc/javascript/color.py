from ..molecule import Color


def color_to_javascript(color: Color) -> str:
    red = f'{format(color.get_red(), "x")}'.rjust(2, '0')
    green = f'{format(color.get_green(), "x")}'.rjust(2, '0')
    blue = f'{format(color.get_blue(), "x")}'.rjust(2, '0')
    return f'0x{red}{green}{blue}'
