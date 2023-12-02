# first part
f = open("input.txt" ,'r')
lines = [line.strip() for line in f.readlines()]
digits = ["".join([l for l in line if l.isdigit()]) for line in lines]
print(sum([int(d[0] + d[-1]) for d in digits]))

# second part
keys = [
    ("zero", "0"), 
    ("one", "1"), 
    ("two", "2"), 
    ("three", "3"), 
    ("four", "4"), 
    ("five", "5"), 
    ("six", "6"), 
    ("seven", "7"), 
    ("eight", "8"), 
    ("nine", "9")
]
s = 0
for line in lines:
    current_index = 0
    while current_index < len(line):
        temp = line[current_index:]
        for i in range(10):
            if len(temp) >= len(keys[i][0]):
                if temp.startswith(keys[i][0]):
                    line = line.replace(keys[i][0], keys[i][1] + keys[i][0][-1])
        current_index += 1
    digits = "".join([l for l in line if l.isdigit()])
    digits = digits[0] + digits[-1]
    s += int(digits)
print(s)
