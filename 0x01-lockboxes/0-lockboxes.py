#!/usr/bin/python3
"Lockboxes"


def canUnlockAll(boxes):
    """
    Determines if locked boxes can be opened with available keys.
    Solution to the lockboxes problem
    """
    n = len(boxes)
    o = [False] * n
    o[0] = True
    keys = boxes[0]
    i = 0

    while i < n:
        if o[i]:
            for key in boxes[i]:
                if key < n and not o[key]:
                    o[key] = True
                    keys.append(key)
        i += 1

    return all(o)
