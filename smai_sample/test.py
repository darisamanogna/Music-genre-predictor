print("Manogna") 
# print single string

print("Hi I am Manogna \nI am pursuing ECE in BTech 3rd year.")
# printing in two lines 

var1="Manogna"
print("I am " ,var1)
# printing the variables along with the string

var2=input("enter your age:")
print("my age is: ",var2)
# input function is used to take input as string or character from the user

var3=int(input("enter the class:"))
print(var3)

var4=float(input("enter your weight:"))
print(var4)
# To take the input in the form of other datatypes we need to "typecast"

# range(int_start_value,int_stop_value,int_step_value).....this is the basic pattern
# for returning the sequence of numbers

# display all even numbers between 1 to 100
print("all the even numbers in the range of 0 to 100:")
for i in range (0,101,2):
    print(i)
    
# for multi line comment 
# ...................
'''This is a
multi-line
comment'''
# ...................

# Escape sequence
# 1.Newline(\n)