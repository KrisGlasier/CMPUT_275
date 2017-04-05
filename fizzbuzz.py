def FizzBuzzQ():
    """
    Write a program that prints the numbers from 1 to 100. But for multiples of
    three print "Fizz" instead of the number and for the multiples of five
    print "Buzz". For numbers which are multiples of both three and five print
    "FizzBuzz"
    """
    for i in range(1,101):
        x = ""
        if i%3 == 0:
            x += "Fizz"
        if i%4 == 0:
            x += "Buzz"
        if x == "":
            x = i
        print(x)

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
