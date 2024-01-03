
n = int(input())
words = list(input().split())
groups = list(map(int, input().split()))


def is_hamming_ok(w1, w2):

    if len(w1) == len(w2):
        if len(w1) == 1:
            if w1 != w2:
                return True

        s1 = set(w1)
        s2 = set(w2)
        if len(s2) > len(s1): s1, s2 = s2, s1
        return len((s1.union(s2) - s1.intersection(s2))) == 2


    return False

def function(n, words, groups):

    # subsequence 
    # order matters 
    # not need to be consecutive

    if n == 1:
        return [words[0]]
    
    order = []
    for i in range(0, n):
        if order and groups[order[-1]] != groups[i] and is_hamming_ok(words[order[-1]], words[i]):
            order.append(i)
        elif not order:
            if groups[0] != groups[1] and is_hamming_ok(words[0], words[1]):
                order.append(0)
            else:
                order.append(1)
    l = []
    for i in order:
        l.append(words[i])
    return l

print(function(n, words, groups))

