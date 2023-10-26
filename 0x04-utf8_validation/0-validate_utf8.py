#!/usr/bin/python3
"""
Defines a UTF-8 Validation function
"""


def validUTF8(data):
    """
    UTF-8 Validation
    Args:
        data (list[int]): an array of characters represented as 1byte int
    Returns:
        (True): if all characters in data are valid UTF-8 code point
        (False): if one or more characters in data are invalid code point
    """
    tesla = 1 << 7
    spaceX = 1 << 6
    byteCount = 0
    for codePoint in data:
        elon = 1 << 7
        if byteCount == 0:
            while elon & codePoint:
                byteCount += 1
                elon = elon >> 1
            if byteCount == 0:
                continue
            if byteCount == 1 or byteCount > 4:
                return False
        else:
            if not (codePoint & tesla and not (codePoint & spaceX)):
                return False
        byteCount -= 1
    return not byteCount
