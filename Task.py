'''#if Statement program
#Q1) write python program to check whether a user gets a verified badge.

eligible_account = True
Meta_verified_Subscription = True
if eligible_account and Meta_verified_Subscription:
    print("Verified Badge Granted")
else:
    print("None")

#if-else Statement Programs
#Q1)Write a python program to validate username and password

user_name = input("Username:")
password = input("password:")
if user_name == "admin" and password == "admin123":
    print("Login Successful")
else:
    print("Invalid Credentials")

#Q3)Write a python program to check whether a product exists in the available product list.

available_products = ["Laptop","Mobile","Watch"]
search_products = input("Enter product name to search:")
if search_products in available_products:
  print("product found")
else:
    print("product is not found")
    
#if-elif-else Statement programs
#Q4)write a python program to display greetings based on the current hour.
    
hour = int(input("Enter the value:"))
if 5 <= hour <= 11:
    print("Good Morning:")
elif 12 <= hour <= 16:
    print("Good Afternoon:")
elif 17 <= hour <= 20:
    print("Good Evening:")
else:
    print("Good Night:")

#Q5)write a python program to determine the hosting plan based on the customer's budget.

budget = int(input("Enter the value:"))
if budget>10000:
    print("plan:Cloud Hosting:")
elif budget>5000:
    print("plan:Business Hosting:")
elif budget>2000:
    print("plan:Premium Hosting:")
else:
    print("plan:Single Hosting:")

#Nested if programs
#Q6)write a python program to check whether a user can view a close friends story.
follows_account = True
close_friend = True
if follows_account:
    if close_friend:
        print("Story Visible")
    else:
        print("Not in close friend list")
else:
    print("Follow the Account First")

#Q7)write a python program to check whether a player can join a BGMI tournament.
registered = True
fee_paid = True
if registered:
    if fee_paid:
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registered Required")'''

#Q8)write a python program to check whether a user can access a shared file.
link_active = True
permission_granted = True
if link_active:
    if permission_granted:
        print("File Opened Successfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")
    

    
