x=input("what is your age")
print(x)
print("your age is",x)
# == equal to
# != not equal to
# >= greater than equal to
# <= less than equal to
# > greater than
# < less than

x= 30
print(x==30)
print(x!=30)
print(x>=30)
print(x<=30)
print(x>30)
print(x<30)

# testing for the multiple condition
# and or not

x= 13
y= 34

print(x==13 and y==34)  # both the conditions need to be true simultaneously
print(x==13 and y!=34)
print(x==13 or y==34)   # either of the conditions can be true
print(x==13 or y!=34)
print(x==13 or not y==34)
print(x==13 and not y!=34)

# if else statements
# if, elif, else
# riding game in the park
age=input("what is your age:")
age=int(age)
if age<=5:
    print("you are not eligible to ride as you are underage")
elif age>5 and age<=21:
    print("you are eligible to ride")
else:
    print("you are not eligible to ride")

# for Loop
list_1=[1,2,3,4,5,6,7,8,9,0]
print(1 in list_1)
for q in list_1:
    print(q)
    print(q*"x")
# range function
for w in range(0,10):
    print(w)
