# This is a placeholder for your code. No starter file is provided. 

# Follow the instructions and create comments for the
#  actions your program will perform. 

# Name: Paul Saini
# Date: July 14th, 2026
# Project: Project 1 - Sales Conversation with a Fake Sales ChatBot


# Introduce the chatbot and welcome the customer 
print("===============================")
print("WELCOME TO PIXEL PALACE GAMING!")
print("===============================")
print("Hello! My name is Pixel, your gaming sales assistant.")


# Ask if the customer wants to learn about the product 
learnProduct = input("Would you like to learn about our RetroBox controller? (yes/no)


if learnProduct == "yes":
    # Display the product description using tripple quotes 
    print("""
The RetroBox controller combines the comfortable shape of a
modern controller with the colorful style of classic gaming.

FEATURES:
- Works with Windows computers
- Comfortable grips and responsive buttons
- Includes a six-foot USB cable
- Colorful retro-inspired design

Whether you enjoy racing, action, or platform games, the
RetroBox controller makes playing your favorites comfortable
and fun. Best of all, it only costs $50.00!
""")


    # Ask whether the customer wants to purchase the product 
    purchase = input("Would you like to purchase a RetroBox controller? (yes/no): ")


    if purchase == "yes":
        print("Great choice! Let's complete your order.")


        # Collect the customer's information
        firstName = input("Enter your first name: ")
        lastName = input("Enter your last name: ")
        email = input("Enter your email address: ")
        phoneNumber = input("Enter your phone number: ")

        # Show the price and ask for the desired quantity
        itemPrice = 20.00
        print("Each RetroBox controller costs $20.00.")
        quantity = int(input("How many controllers would you like to purchase? "))

        # Calculate the subtotal, tax, and final total
        subtotal = itemPrice * quantity
        tax = subtotal * 0.10
        total = subtotal + tax

        # Display the completed receipt
        print("=====================")
        print("PIXEL PALACE RECEIPT")
        print("=====================")
        print("Customer:", firstName, lastName)
        print("Email:", email)
        print("Phone number:", phoneNumber)
        print("----------------------")
        print("Product: RetroBox Controller")
        print("Quantity:", quantity)
        print("Price per item: $", itemPrice)
        print("Subtotal: $", subtotal)
        print("Sales tax (10%): $", tax)
        print("Total amount due: $", total)
        print("=====================")

        # Thank the customer and end the conversation
        print("Thank you for shopping at Pixel Palace Gaming!")
        print("Pixel hopes you enjoy your new controller. Goodbye!")
      
