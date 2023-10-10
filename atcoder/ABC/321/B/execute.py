"""
Title:
	Cutoff
URL:
	https://atcoder.jp/contests/abc321/tasks/abc321_b
Memo:
	わからんかった
	2通りの回答が存在する
    - 1 ~ 100まで順に計算する方法
    - 場合わけ
		
Run:
	>>> rye run python atcoder/ABC/321/B/execute.py < atcoder/ABC/321/B/input.txt
"""
N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
current_max = A[-1]
current_min = A[0]
sum_of_middle = sum(A[1:-1])

if 100 >= X - (current_min + sum_of_middle) >= 0:
    print(0)
elif current_min <= X - sum_of_middle <= current_max:
    print(X - sum_of_middle)
elif X - (sum_of_middle + current_max) <= 0:
    print(A[-1] + 1)
else:
    print(-1)
