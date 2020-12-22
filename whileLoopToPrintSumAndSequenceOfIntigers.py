'''1.WAP in python to add natural numbers up to sum = 1+2+3+...+n

1+

1+2

1+2+3

1+2+3+4

1+2+3+4+5

………..

……..

…….

…..

1+2+3+4+5+6+7+8+9+10=

Total sum of 1 to 100 natural number is:55'''
# Program that prints the num of n natural numbers
# N is given by the user

#Solution:

number = int(input("Enter any number: "))

a = 2
numbers = "1"
total = 0

while a <= number:
    temp = a
    a = a + 1
    numbers = numbers + " + " + str(temp)
    total += temp
    print(numbers)

print("The sum of {0} from the given range of natural numbers {1} is {2}.".format(numbers, number, total + 1))

'''Output:

Enter any number: 10
1 + 2
1 + 2 + 3
1 + 2 + 3 + 4
1 + 2 + 3 + 4 + 5
1 + 2 + 3 + 4 + 5 + 6
1 + 2 + 3 + 4 + 5 + 6 + 7
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
The sum of 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 from the given range of natural numbers 10 is 55.

Process finished with exit code 0'''