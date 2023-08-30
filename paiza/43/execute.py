"""
Title:
    S007:データヒストグラム
URL:

Memo:

Run:
    >>> rye run python paiza/43/execute.py < paiza/43/input.txt
"""
from pprint import pprint
S = input()

def check_char(it):
    if it.isalpha():
        return it, "A"
    elif it.isnumeric():
        return it, "N"
    elif it == '(':
        return None, "B_S"
    elif it == ")":
        return None, "B_E"

def check_string(value):
    vl = []
    is_num = False
    num = []
    is_block = False
    block = []

    for it in value:
        v, c = check_char(it)

        if is_block and c not in ["B_S", "B_E"]:
            block.append(v)
            continue

        if not is_num and len(num) >= 1:
            vl.append(int("".join(num)))
            num = []

        if c == 'A':
            vl.append(v)
        elif c == 'N':
            num.append(v)
        elif c =="B_S":
            is_num = False
            is_block = True
        elif c == "B_E":
            vl.append(check_string("".join(block)))
            block = []
            is_block = False

    return vl

pprint(check_string(S))
