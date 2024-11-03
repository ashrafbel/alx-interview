#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    numBites = 0
    pattern1 = 1 << 7
    pattern2 = 1 << 6
    for num in data:
        num = num & 255
        if numBites == 0:
            mask = 1 << 7
            while num & mask:
                numBites += 1
                mask = mask >> 1
            if numBites == 0:
                continue
            if numBites == 1 or numBites > 4:
                return False
        else:
            if not (num & pattern1 and not (num & pattern2)):
                return False
        numBites -= 1
    return numBites == 0
