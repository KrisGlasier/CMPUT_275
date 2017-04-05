def FizzBuzzQ():
    """
    Write a program that prints the numbers from 1 to 100. But for multiples of
    three print "Fizz" instead of the number and for the multiples of five
    print "Buzz". For numbers which are multiples of both three and five print
    "FizzBuzz"
    """
    for i in range(1,101):
        if not i%4 and not i%3:
            print("FizzBuzz")
        elif not i%3:
            print("Fizz")
        elif not i%4:
            print("Buzz")
        else:
            print(i)

def Reverse():
    """
    Reverse a string from an input without any library finctions.
    """
    x = input()
    temp = ""
    for i in range(len(x)):
        j = len(x)-i-1
        temp += x[j]
    print(temp)
