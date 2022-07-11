# ecoo12r1p2 DNA Sequencing

import sys

from typing import List

def get_dna()->str:
    strands = []

    for i in range(3):

        strands.append(sys.stdin.readline())

    return strands

promoter = "TATAAT"

def reverse(entry_strand: str) ->str:

    """The strands are reversed with their complementary bases"""

    opponents = {'A':'T', 'C':'G'}

    entry_strand = list(entry_strand)

    entry_strand = ''.join(entry_strand.reverse())

    entry_strand = entry_strand.replace('A', opponents['A'])

    entry_strand = entry_strand.replace('C', opponents['C'])

    return entry_strand


