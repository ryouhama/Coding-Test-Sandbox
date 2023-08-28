"""
Title:
    Chord
URL:
    https://atcoder.jp/contests/abc312/tasks/abc312_a
Memo:
    
Run:
    >>> rye run python atcoder/312/A/execute.py < atcoder/312/A/input.txt
"""
S = input()
print("Yes" if S in ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"] else "No")
