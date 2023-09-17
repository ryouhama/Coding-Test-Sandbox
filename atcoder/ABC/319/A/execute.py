"""
Title:
    A - Legendary Players
URL:
    https://atcoder.jp/contests/abc319/tasks/abc319_a
Memo:

Run:
    >>> rye run python atcoder/ABC/319/A/execute.py < atcoder/ABC/319/A/input.txt
"""
p = input()
lating = {
    "tourist": 3858,
    "ksun48": 3679,
    "Benq": 3658,
    "Um_nik": 3648,
    "apiad": 3638,
    "Stonefeang": 3630,
    "ecnerwala": 3613,
    "mnbvmar": 3555,
    "newbiedmy": 3516,
    "semiexp": 3481,
}

print(lating.get(p))
