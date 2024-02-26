s = input()
k = int(input())

def characterReplacement(s: str, k: int) -> int:
    l = 0
    max_length = 0
    current_window = {}
    for r in range(len(s)):
        current_window[s[r]] = current_window.get(s[r], 0) + 1
        if (r-l+1) - max(current_window.values()) > k:
            current_window[s[l]] -= 1
            l += 1
        max_length = max(max_length, r-l+1)
    return max_length

print(characterReplacement(s, k))