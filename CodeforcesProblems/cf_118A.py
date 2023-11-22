s = input().lower()
vowels = list("aeyiou")
stack = [l for l in s if l not in vowels]
if stack:
    print(".".join([""] + stack))