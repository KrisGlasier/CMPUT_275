## count_upper.py
# This program will conut the number of uppercase letters in a given string
# ie 'HEllo' will output 2, whereas 'hello' will output 0.

def counter(x):
    count = 0
    for i in x:
        if i.isupper():
            count += 1
    return count

string = input()
print(counter(string))
