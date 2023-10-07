#!/usr/bin/python3
"""
Defines a function canUnlockAll that determines if a box can be unlock
"""


def canUnlockAll(boxes):
    """
    A  method that determines if all the boxes can be opened.
    Args:
        boxes (list of boxes)
    Returns:
        bool: True if all boxes can be unlock, else False
    """
    keys = set([0] + boxes[0])
    locked = set()
    for box in boxes:
        ibox = boxes.index(box)
        if ibox not in keys:
            if max(keys) > ibox:
                locked.add(ibox)
                continue
        keys |= set(box)
    for key in locked:
        if key in keys:
            keys |= set(boxes[key])
    return not bool(locked - keys)
