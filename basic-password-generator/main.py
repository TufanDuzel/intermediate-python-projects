import string, random

characters = string.ascii_letters + string.digits + string.punctuation

while True:
    length_str = input("Length of the password: ")

    if not length_str.isdigit():
        print("Please enter a digit value for the length of the password!")

        continue

    length = int(length_str)
    break

password = "".join(random.choice(characters) for _ in range(length))

print("Password: ", password)