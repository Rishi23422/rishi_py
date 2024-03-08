# Example1: ways of creating a string varable
# s='Welcome'
# st= "Welcome"
# stu = str('Welcome')
# stuv = str("Welcome")

#Empty string variables
# name= str()
# name= ""
# name= ''

#Example2:
#mutable - value of variable cannot be updated
#immutable - value of variable can be updated
#String is mutable or immutable - Ans: Strings are immutable
# str1= 'Welcome'
# print(id(str1)) #139878425781680
# print(str1)

# str1= str1 + "to Python"
# print(id(str1)) #140637967601536
# print(str1)

#If the value of id got changed - immutable

#Example3: + and * operators with Strings
# str= 'Welcome'
# print(str + ' Programming') #Concatenation
# print(str * 5)

#Example4: Slicing operator []
#Starting index - 0
# str= 'Welcome'
# print(str[1:3]) #el
# print(str[:3]) #Wel
# print(str[2:]) #lcome
# print(str[2:-1]) #lcom last character removed
# print(str[2:-2]) #lco last two character removed

#Example5: ord() and chr() functions for string
# print(ord('A')) #Print ASCII value of A
# print(ord('a')) #Print ASCII value of a

# print(chr(65))
# print(chr(97))

#Example6: max(), min(), len()
# print(max('abc')) #c
# print(min('abc')) #a
# print(len('abc')) #3

#Example7: in, not in operators - returns True or False
# s='Welcome'
# print("come" in s) #True
# print("rish" in s) #False

# print("come" not in s) #False
# print("rish" not in s) #True

#Example8: Strings comparison
# print("Tim" == "tim") #False
# print("free" != "freedom") #True
# print("arrow" > "aron") #True
# print("right" >= "left") #True
# print("teeth" < "tee") #False
# print("yellow" <= "fellow") #False
# print("abc" > "") #True

#Example9: Testing Strings functions- returns true or false
# s= '123'
# st= 'welcome to python'
# print(s.isalnum()) #True - because st contains numbers
# print(st.isalnum()) #False - because st contains alphabets

# print('Welcome'.isalpha()) #True - string contains only alphabets or not
# print('Welcome123'.isalpha()) #False - string contains number also

# print('2024'.isdigit()) #True
# print('Welcme'.isdigit()) #False

# print('first number print'.isidentifier()) #False - string contains some Python reserved Keyword or not
# print('print'.isidentifier()) #True

# print('elephant'.islower()) #True - checks if string contains all lowercase letters or not
# print('Elephant'.islower()) #False

# print('elephant'.isupper()) #False
# print('Elephant'.isupper()) #False
# print("ELEPHANT".isupper()) #True

# print("Welcome".isspace()) #False
# print(" ".isspace()) #True

#Example10: Searching for substrings
# s= "welcome to Python"
# print(s.endswith('thon')) #True
# print(s.startswith('good')) #False
# print(s.find('come')) #3
# print(s.find('become')) #-1 Not found
# print(s.count("o")) #3 Returns number of occurences of a substring in a string

#Example11: Converting Strings
s= "String in PYTHON"
# print(s.capitalize()) #String in python
# print(s.title()) #String In Python
# print(s.lower()) #string in python
# print(s.upper()) #STRING IN PYTHON
# print(s.swapcase()) #sTRING IN python
# print(s.replace('in', "on")) #Strong on PYTHON

#Example12: Reverse a String
#Method1- Looping Statement
# s='Welcome'
# print(s)
# revStr=''
# for i in s:
#     revStr = i+revStr
# print(revStr)

#Method2
s='Welcome'
revStr = s[::-1] #slicing operator s[start:end:-1] s[0,7,-1]
print(revStr)