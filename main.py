import random

characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@'

number_of_passwords = int(input("number of passwords: "))
password_length = int(input('password length: '))

print("Password: \n")
for pwd in range(number_of_passwords):
    final_password = ''
    for number_chact in range(password_length):
        final_password += random.choice(characters)
    print(final_password)

print('\n')
