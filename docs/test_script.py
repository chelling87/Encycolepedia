"""
test_script - Python library for modules.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_modules(kind=None):
    """
    Return a list of random modules as strings.

    :param kind: Optional "kind" of module.
    :type kind: list[str] or None
    :raise test_script.InvalidKindError: If the kind is invalid.
    :return: The modules list.
    :rtype: list[str]
    """
    return ["R0", "SS", "R3"]
