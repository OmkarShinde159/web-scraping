'''
Create a function that prints all the factors of a number less than the given
number. Eg: if your function name is factorial. Then factorial 2(4) should print –
24, 6, 2, 1
'''

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    print(fact)

def factorial2(num):
    while num>0:
            factorial(num)
            num -= 1
# Input
# factorial2(8) 
# factorial(8)      


'''
Create a function for calculating percentage of given number
Eg. input as A, B and output will be the percentage of input.

'''
def findPerc(*num):
    obt = sum(num)
    tot = len(num)*100
    x = obt/tot
    per = x*100
    print("Percentage of a given numbers is : ", per)

# Input
# a = int(input("Enter the value: "))
# b = int(input("Enter the value: "))
# # findPerc(a,b)
# findPerc(65,75,90,67)

'''
Create a function to display data type of given object
I. create object
II. display data type of object

'''

def display_data_type(object):
    print("Data type of an object is : ", type(object))


s = "python"
display_data_type(s)

i = 123
display_data_type(i)

b = True
display_data_type(b)

lst = [1,2,"string"]
display_data_type(lst)

tp = ( 1,2,"str")
display_data_type(tp)

st = {s,2,"str"}
display_data_type(st)

dt = {1:"str",2:"tup"}
display_data_type(dt)


























