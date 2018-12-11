#                                            -------------------------------
#                                                 | WNS Python Training |
#                                            ------------------------------
### Day-1: Session Starts!#####
############################### 

### 1. Strings 
############
#Printing the text
print("This is my first line of code in python")


# Next line command with print function
print("Hello Everyone,\n\nThis is in the next line")

# Storing Text(In Python terms "String")
name = "Jolly Nate"

# Checking the type of variable
type(name)
# Tip-1:Any string or character in python will be written with the double Quote("") or Single Quote('')


### 2. Integer and Numeric Type
###############################
# Printing integer
print(7)

# Integer Type 
first_int = 7
type(first_int)

# Numeric Type(In Python, it's FLOAT)
float_var = 7.1
type(float_var)


### 3. Arithmetic Operations 
############################

# Adding two integers 
a = 16
b = 3

# Addition
a+b

# Addition of two text strings
print("RAM" + " Shyam")

# Subtraction 
a-b

# Multiplication 
a*b

# Division 
a/b

# // (divide and floor) or int() can also give the same result
a//b 

# % (modulo)[Remainder]
a%b

# ** Square 
a**b

#BODMAS: Question
((4/5)-1+(10/2*2)+4)


# Python shortcuts
# Addition shortcut
num = 5
num += 1
num

# Subtraction shortcut
num -= 1
print(num)


### 4. Logical Operators
########################
# Comparing two integers
print(3 < 4)

# Printing results of AND,OR AND NOT and ! operators 
print(True and False) 
print(True or False)
print(True and not False)


# Changing text to Upper Case or Lower Case
small = "i am upper cased"
print(small.upper())

large = "I AM LOWER CASED"
print(large.lower())

# Removing blank spaces from the end of the text
some_sentence = "There is a space at the end    "
print(some_sentence)
print(some_sentence.strip())


# Right Strip
some_sentence.rstrip()

# Striping "%" from the string 
increment = '4%'
print(increment.strip('%')) 

# Left Strip 
start = "   There is space at the start"
print(start)
print(start.lstrip())

# Striping from both the end 
spaces = "   Trim whitespaces  "
print(spaces)
print(spaces.strip())

# Striping more than 1 special characters from the text
num_with_chars = '*444#'
print(num_with_chars.rstrip('#').lstrip('*'))


# Special case of adding string texts: The format method (Its a new way of optimising the python codes)
# we may want to construct strings from combination of information. This is where the format() method is useful.
# For Example-1, 

Age = 24
Name = "Chiranjeev"
print("My name is {1} and I am {0} years old".format(Age,Name))

# Example-2
X1 = "Chiranjeev"
X2 = "Rohan"
X3 = 24
X4 = 27
X5 = "WNS"

print("{0} and {1} both are engaged with {4}. {1}'s age is {3} and {0}'s age is {2}".format(X1,X2,X3,X4,X5))


# Type Conversion
# Sometimes it is necessary to convert one data type into another. This can be done by using typecasting 
# Converting string to numeric float type 
float("3.145")

# Converting string to numeric int type 
int("3")


### 5. Problem Solving Skills: Business Problem
###############################################

# A marketing person wants to send an automatic personalise email to few target customers: 
# He wants to promote some of the companies products such as computer in INR 30000, DSLR in INR 15000 
# or Iphone in INR 22000. 

# Below is a Subject and mail body resp, to be sent through an email:

# Subject 
'''
Hurry Up! [customer_name] - This offer available to you only!
'''

# Mail Body
'''
Good Morning [Customer_Name], 

I have a great deal for you today! 
We are selling [Product_Name] in INR [Product_Price] to you with [offer_percentage] discount. Please visit our website now to get more
information!

Thanks, 
Raj
'''

# Now, you need to send this email to: Rohan and sale him computer in 30000 with 6000 discount:

# Input Variables 
Customer_Name = 'Rohan'
Product_Price = 40000
offer_amount = 6000
Product_Name = 'Computer'

# Solutions
Subject = ### Write your Answer ###
mail_body = ### Write Your Answer ###

print(mail_body)

### 6. Outlook Application # - Optional Exercise
############################

# Outlook Setup 
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')

mail = outlook.CreateItem(0)
mail.To = 'chiranjeev.patidar@wns.com'
mail.Subject = Subject
mail.Body = mail_body

# Mail Displaying 
mail.display()

# Sending email
mail.Send()


### 7. Lists #
############## 
# Data structures are a special way of storing and accessing data and 
# play an important role in manipulations as well. 
# We will be covering the most widely used python data structures starting with lists. 
# Function Type: []

# Example-1
initial_list = []
print(initial_list)

# Example-2
list_1 = [1,2,4]
print(list_1)

# Example-3
Prog_language = ['R','Python', 'SAS', 'Scala', 42]
print(Prog_language)

# Subseting, Slicing, Dicing Lists 
# Printing first element of list 'Prog_language'
print(Prog_language[4])
print(type(Prog_language[4]))
print(type(Prog_language[2]))

print(Prog_language[1:3])

print(Prog_language[0:2])


# Appending two lists 
list_1 = [1,2,34]
list_2 = ['ram','romeo','ravan']
list_2.append(list_1)
print(list_2)

# Adding two lists elements in one list
list_1 = [1,2,34]
list_2 = ['ram','romeo','ravan']
print(list_1+list_2)

# Or extend() can also help us join two lists elementwise
list_2.extend(list_1)
list_2

# Subtracting common elements from 1st list
list_1 = ['Ram',"Raj","Rome","Rahul"]
list_2 = ['Rome','Ram',12,34]

list_3 = list(set(list_1)- set(list_2))
print(list_3)


# Replacing elements values in the list 
print(list_1)
list_1[0] = "Shyam"
print(list_1)


# Splitting the text into list elements
mail = "Hi CP, this is to inform you that I'm not well today. I won't be coming to office, but I'm available on call. Thanks."

sentences_in_mail = mail.split('.')
print(sentences_in_mail)

# Counting total elements
len(sentences_in_mail)

# Joining all the list elements into a single element
mail = " ".join(sentences_in_mail)
print(mail)

# Slicing the string elements
val = "2 apples"
no_of_apples = val[0] 
print('Number of apples is', no_of_apples)

# Printing "apples"
print(val[7])
print(val[2:])
print(val[2:8])

#slicing by specifying start and end index
print(val[2:5])

# Example 
batch = "5 oranges 3 monkeys n"
fruits = batch[ :9]
print(fruits)

# deleting the last two characters from the string
print(batch[ :-2])

# Extracting only specific portion of data 
animals = batch[10:-2]
print(animals)


### 8. Problem Solving Skills: Business Problem (Continue...) Application of lists #
####################################################################################

# Old way of sending emails
# Input Variables 
Customer_Name = 'Rohan'
Product_Price = 40000
offer_amount = 6000
Product_Name = 'Computer'

# Now, we need to send an email to 4 person with different product config.
cust_info = [['Rohan',40000,6000,'Computer'],
             ['Chiranjeev',50000,5000,'DSLR'],
             ['Ram',70000,12000,'Apple Laptop'],
             ['Ravan',80000,5000,'Computer']]


# Below is a Subject and mail body resp, to be sent through an email:

# Subject 
'''
Hurry Up! [customer_name] - This offer available to you only!
'''

# Mail Body
'''
Good Morning [Customer_Name], 

I have a great deal for you today! 
We are selling [Product_Name] in INR [Product_Price] to you with [offer_percentage] discount. Please visit our website now to get more
information!

Thanks, 
Raj
'''


## Solution ##
##############

# First Customer
mail_body_cust1 = ("Good Morning {0},\n\nI have a great deal for you today! \nWe are selling {3} in INR {1} to you with {4}% discount. Please visit our website now to get more information \n\nThanks,\nRaj").format(cust_info[0][0],cust_info[0][1],cust_info[0][2],cust_info[0][3],(cust_info[0][2]/cust_info[0][1])*100)
print(mail_body_cust1)


# Second Customer
mail_body_cust2 =            ### Write your Answer ###

print(mail_body_cust2)


# Third Customer
mail_body_cust3 =            ### Write your Answer ### 
print(mail_body_cust3)


# Forth Customer
mail_body_cust4 = ("Good Morning {0},\n\nI have a great deal for you today! \nWe are selling {3} in INR {1} to you with {4}% discount. Please visit our website now to get more information \n\nThanks,\nRaj").format(cust_info[3][0],cust_info[3][1],cust_info[3][2],cust_info[3][3],int((cust_info[3][2]/cust_info[3][1])*100))
print(mail_body_cust4)

### 8. Tuples #
################
# Tuples are data structures that are similar to lists in all aspects except in the way 
# they are declared and how much they allow themselves to be modified.

# Example-1
first_tuple = ("Monty Python", 30, "Baker Street", 5.8)
print(first_tuple[0])

# Example-2
city_tuple = ("Mumbai", 18.9949521, 72.8141853) 
print(city_tuple)


# Tuples are immutable. We cann't change the values inside any tuple
new_tuple[1] = 13.8877

# Negative index in Tuples: Similar to Lists
b = city_tuple[:-1]
print(b)
print(len(b))

# Converting list to tuple
c = list(b)
print("c is: {0}".format(c))

c= tuple(c)
print("c is now a tuple: {0}".format(c))


# Appending of two or more tuples are not possible
d = ('12',"123")
c.extend(d)


# Addition of two tuples are possible 
print(c+d)


### 9. Dictionaries #
#####################

# Empty Dictionary
empty_dictionary = {}
print(type(empty_dictionary))

# Example-1 
bio_data = {'Name': 'Bob romeo', 'Age':35, 'Height':"5.6 ft", 'Hobby': 'Music'}
print(bio_data)

# Finding value assigns to "Hobby" key 
hobby = bio_data['Hobby']
print(hobby)

# Finding value assigns to "Age" key 
age = bio_data['Age']
print(age)
# OR 
age = bio_data.get('Age')
print(age)

# Changing Value in bio_data dictionary 
bio_data['Age'] = 36
print(bio_data)

#get list of keys
print(list(bio_data.keys()))

#get list of values
print(list(bio_data.values()))

# Creating new dictionary 
new_dictionary = dict(Country='Jamaica', Songs=['One Love','Misty Morning'])
print(new_dictionary)

# Updating the bio_data dictionary with additional information 
bio_data.update(new_dictionary)
print(bio_data)

# Example-2
students_data = { 1:['Shivam Bansal', 24] , 2:['Udit Bansal',25], 3:['Sonam Gupta', 26], 4:['Saif Ansari',24], 5:['Huzefa Calcuttawala',27]}
print(students_data)


# Printing length of dictionary i.e total count of keys in dict
print(len(students_data))

#see all the details of students in lists. 
print(list(students_data.values()))

# Adding 6th students details in student data dict
students_data[6] = ['Manasi Sharma', 22]
print(students_data)

# Deleting 2nd key of dictionary
del students_data[2]
print(students_data)

# Nested Dict.
Dictionary= {1: 'Geeks', 2: 'For', 3: {'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}}
print(Dictionary)