import sys

digit_string = sys.argv[1]

res = 0;
for digit_char in digit_string:
    res += int(digit_char)

print(res)


