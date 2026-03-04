# --- Smart User Profile Generator ---

# Collecting Required BASIc User Information
name = input("Enter your Full Name: ")
age = input("Enter your Age: ")
city = input("Enter your City: ")
job = input("Enter your Profession / Field of Study: ")
language = input("Enter your Favorite Programming Language: ")
bio = input("Enter a Short Bio: ")

# Type Casting Concept (Converting age string to an integer)
age = int(age)

# Logic for Custom Welcome Message (Required)
if age < 18:
    welcome_msg = "🌟 Welcome, young coder! The future is yours."
elif age < 40:
    welcome_msg = " Welcome! Great to see a pro at work."
else:
    welcome_msg = " Welcome! Your experience is an inspiration."

# This Chunk is Displaying the Profile Summary
print("\n-----------------------------------")
print("        USER PROFILE SUMMARY")
print("-----------------------------------")

# Displaying the custom message first
print(f"Message: {welcome_msg}\n")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Profession: {job}")
print(f"Favorite Language: {language}")

print("\nBio:")
print(bio)
print("-----------------------------------")