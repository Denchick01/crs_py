import sys

num_steps = int(sys.argv[1])

steps_count = num_steps

while steps_count > 0:
    steps_count -= 1
    stair = " " * steps_count + "#" * (num_steps - steps_count)
    print (stair)




