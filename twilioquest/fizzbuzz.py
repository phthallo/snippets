import sys
numbers = sys.argv
numbers.pop(0)
#code beings
for i in numbers:
    if int(i) % 3 == 0 and int(i) % 5 != 0:
        print("fizz")
    elif int(i) % 3 == 0 and int(i) % 5 == 0:
        print("fizzbuzz")
    elif int(i) % 5 == 0 and int(i) % 3 != 0:
        print("buzz")
    elif int(i) % 3 != 0 and int(i) % 5 != 0:
        print(i)

