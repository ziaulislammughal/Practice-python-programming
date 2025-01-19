# # Get user input for name and age
# name = input("Enter your name: \n")
# age = int(input("Enter your age: \n"))

# # Check if the user is eligible for an identification card
# if age >= 18:
#     print(f"Hello, {name} you are eligible to submit an application for an identification card.")
# else:
#     print(f"Sorry, {name} you are not eligible to submit an application for an identification card as you are below 18 years old.")

# # Define university name with extra spaces
# uni_name = "           University of Azad Jammu Kashmir, King Abdullah Campus        "

# # Print university name before and after removing extra spaces
# print("\nUniversity Name (Before):")
# print(uni_name)
# print("-------------------------------")
# print("University Name (After):")
# print(uni_name.strip())

# # Print reversed university name after removing extra spaces
# print("\nReversed University Name (After):")
# print(uni_name.strip()[::-1])







# Get user input for name and age
name = input("Enter your name: \n")
age = int(input("Enter your age: \n"))

# Check if the user is eligible for an identification card
if age >= 18:
    print(f"Hello, {name} you are eligible to submit an application for an identification card.")
else:
    print(f"Sorry, {name} you are not eligible to submit an application for an identification card as you are below 18 years old.")

# Define university name with extra spaces
uni_name = "           University of Azad Jammu Kashmir, King Abdullah Campus        "

# Print university name before and after removing extra spaces
print("\nUniversity Name (Before):")
print(uni_name)
print("-------------------------------")
print("University Name (After):")
print(uni_name.strip())

# Print reversed university name after removing extra spaces
print("\nReversed University Name (After):")
print(uni_name.strip()[::-1])

# Define a string
original_string = "Hello, World!"
print("\nOriginal String:")
print(original_string)
print("-----------------------------")

# Replace a substring in the string
new_string = original_string.replace("World", "Pakistan")
print("String after replacement:")
print(new_string)

# replacing 

string = "Hello, World!"
print(string)
print("-----------------------------")
string = string.replace("World","Pakistan")
print(string)