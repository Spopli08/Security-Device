import SD
import random

def average(tries):
    total = 0
    min = max = guess()
    for i in range(1, tries):
        count = guess()
        total += count

        if count < min:
            min = count
        if count > max:
            max = count

    print("Minimum: ", min)
    print("Maximum: ", max)
    print("Average: ", total/tries)

def guess():
    test = SD.SecurityDevice()
    count = 0
    while test.state != 6:
        val = random.randint(0, 9)
        test.enterval(val)
        count += 1

    return count

average(10)