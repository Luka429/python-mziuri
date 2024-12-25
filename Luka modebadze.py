#ამოცანა 1

def division(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("you can't divide numbers by zero")
    except TypeError:
        print("You must use real numbers")

print(division(10,"a"))

#ამოცანა 2


try:
    word = input("Enter a phrase that has 10 or more characters: ")
    print("The tenth character of this phrase is:",word[9])
except IndexError:
    print("Please enter a phrase that has 10 or more characters")

#ამოცანა 3

try:
    My_file = open("Myresult.txt",'r')
except FileNotFoundError:
    print("this file doesn't exist")




