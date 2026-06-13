import random
import string

# User input for password length
length = int(input("Enter the desired password length: "))

# Characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("Generated Password:", password)

output:
Enter the desired password length: 8
Generated Password: 123@Sriv
