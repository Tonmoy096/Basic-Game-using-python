import random
import string

def pas_generator():
    length = int(input("Enter the desired length of password:"))
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation


    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    password = '' .join(random.choice(all_characters) for _ in range(length))

    print(f"Generated password: {password}")
    


    print(f"Generating password length {length}")
    print(f"Lowercase letters: {lowercase_letters}")
    print(f"Uppercase_letters:{uppercase_letters}")
    print(f"digits: {digits}")
    print(f"Symbolss : {symbols}")

if __name__ == "__main__":
    pas_generator()