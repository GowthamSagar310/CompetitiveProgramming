# https://leetcode.com/contest/weekly-contest-291/problems/remove-digit-from-number-to-maximize-result/

def removeDigit(number: str, digit: str) -> str:
    max_value = 0
    for i in range(len(number)):
        if i == 0 and number[i]==digit:
            if int(number[1:]) > max_value:
                max_value = int(number[1:])
        elif i == len(number)-1 and number[i] == digit:
            if int(number[:-1]) > max_value:
                max_value = int(number[:-1])
        elif number[i] == digit:
            if max_value < int(number[:i] + number[i+1:]):
                max_value = int(number[:i] + number[i+1:])
    return str(max_value)


number = input()
digit = input()
print(removeDigit(number, digit))
