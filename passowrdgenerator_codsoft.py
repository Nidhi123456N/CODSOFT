import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("PASSWORD GENERATOR")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length > 0:
            password = generate_password(length)
            print(f"Generated Password: {password}")
        else:
            print("Invalid length. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    password_generator()
