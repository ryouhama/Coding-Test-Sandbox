S = str(input())

ans = [it for it in S if it not in ["a", "e", "i", "o", "u"]]
print("".join(ans))
