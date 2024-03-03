# if  if...el elif

#Example1: Print a person is eligible for vote or not
#age>=18

# age =18
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")

#Example2: 
# if True:
#     print("true condition")
# else:
#     print("false condition")

#Example3: 
# if 1:
#     print("one")
# else:
#     print("Not one")

#Example4: Find number is Even or Odd
# num = 10
# if num%2==0:
#     print(num, "is Even number")
# else:
#     print(num,"is Odd number")

#Example5: if..el in single line (Ternary operator)
# num=10
# print("Number is Even") if num%2==0 else print("Number is Odd")

#Example6: if..el multiple statements in single line
# a=9
# {print("Hello"), print("Python")} if a>=10 else {print("Hi"), print("Java")}

#Example7: Multiple conditions (elif)
weekno = 1
if weekno ==1:
    print("Sunday")
elif weekno ==2:
    print("Monday")
elif weekno ==3:
    print("Tuesday")
elif weekno ==4:
    print("Wednesday")
elif weekno ==5:
    print("Thursday")
elif weekno == 6:
    print("Friday")
elif weekno == 7:
    print("Saturday")
else:
    print("Invalid Week number")