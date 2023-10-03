"""
Title:

URL:
    https://atcoder.jp/contests/abc322/tasks/abc322_a
Memo:

Run:
    >>> rye run python atcoder/322/A/execute.py < atcoder/322/A/input.txt
"""
import re

N = int(input())
S = input()

result = re.search("ABC", S)

print(result.start() + 1 if result else "-1")
