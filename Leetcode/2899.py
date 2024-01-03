words = list(input().split())

def previous_elements(words):
    pointer = -1
    stack = []
    nums = []
    for i in words:
        if i == "prev":
            if pointer < 0:
                stack.append(-1)
            else:
                stack.append(nums[pointer])
                pointer -=1  
        else:
            nums.append(int(i))
            pointer = len(nums)-1
    return stack

print(previous_elements(words))