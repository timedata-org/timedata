"""
Convert back and forth between colors and string names.
"""

import numbers
from . import table
from . table import COLOR_DICT


def name_to_color(name):
    """
    :param str name: a string identifying a color.  It might be a color name;
                     or it might be a list of numeric r, g, b values separated
                     by commas.
    :returns: a color as an RGB 3-tuple
    """
    def to_color(name):
        name = name.lower()
        if ',' in name:
            if name.startswith('(') and name.endswith(')'):
                name = name[1:-1]
            if name.startswith('[') and name.endswith(']'):
                name = name[1:-1]

            r, g, b = name.split(',')
            return _from_number(r), _from_number(g), _from_number(b)

        try:
            n = _from_number(name)
        except:
            color = table.get_color(name)
            if color:
                return color
            raise ValueError

        return table.to_triplet(n)

    try:
        color = to_color(name)
    except:
        raise ValueError('Unknown color name %s' % str(name))

    if not all(0 <= i <= 255 for i in color):
        raise ValueError('Component out of range: %s' % color)

    return color


def color_to_name(color, use_hex=False):
    """
    :param tuple color: an RGB 3-tuple of integer colors
    :returns: a string name for this color

    ``name_to_color(color_to_name(c)) == c`` is guaranteed to be true (but the
    reverse is not true, because name_to_color is a many-to-one function).
    """
    if isinstance(color, list):
        color = tuple(color)
    elif not isinstance(color, tuple):
        raise ValueError('Not a color')

    if use_hex:
        return '#%02x%02x%02x' % color

    return table.get_name(color) or str(color)


def toggle(s):
    """
    Toggle back and forth between a name and a tuple representation.

    :param str s: a string which is either a text name, or a tuple-string:
                  a string with three numbers separated by commas

    :returns: if the string was a text name, return a tuple.  If it's a
              tuple-string and it corresponds to a text name, return the text
              name, else return the original tuple-string.
    """
    is_numeric = ',' in s or s.startswith('0x') or s.startswith('#')
    c = name_to_color(s)
    return color_to_name(c) if is_numeric else str(c)


def _from_number(s):
    s = s.strip()
    for prefix in '0x', '#':
        if s.startswith(prefix):
            return int(s[len(prefix):], 16)

    return int(s)


def to_color(c):
    """Try to coerce the argument into a color - a 3-tuple of numbers-"""
    if isinstance(c, numbers.Number):
        return c, c, c

    if not c:
        raise ValueError('Cannot create color from empty "%s"' % c)

    if isinstance(c, str):
        return name_to_color(c)

    if isinstance(c, list):
        c = tuple(c)

    if isinstance(c, tuple):
        if len(c) > 3:
            return c[:3]
        while len(c) < 3:
            c += (c[-1],)
        return c

    raise ValueError('Cannot create color from "%s"' % c)
