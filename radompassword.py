import random
import string

def generate_password(length=12):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits


    all_characters = lowercase + uppercase + numbers

  
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers)
    ]


    password += random.choices(all_characters, k=length - 3)


    random.shuffle(password)


    return ''.join(password)

print(generate_password(12))


