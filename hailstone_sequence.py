######################
# Unit 0 Lab 5
# hailstone_sequence.py
#######################

print("--- Hailstone Sequence ---")
print()

num = int(input("Input a starting number: "))
steps_to_end = 0

while num != 1:
    if num%2 == 0:
        num = num//2
    else:
        num = num*3+1

    steps_to_end += 1

    print(num)

print("It took {} steps to complete the sequence".format(steps_to_end))