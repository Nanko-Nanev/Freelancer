input_string = input().split()

string = []

for ch in input_string:
    string.append(ch)

result = ''

while string:
    result += string.pop() + " "

print(result)