# for py password generator for securing your accounts from hackers
import random
print("WELCOME TO PY . GENERATOR")
letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters_upper=[letter.upper() for letter in letters]
numbers = [1,2,3,4,5,6,7,8,9,]
symbols = ['!','@','#','$','%','^','&','*']
nr_letters=int(input("enter the number of letters :\n"))
nr_upper=int(input("enter the number of uppercase letters :\n"))
nr_symbols=int(input(f"enter the number of symbols :\n"))
nr_numbers=int(input(f"enter the number of numbers :\n"))
password_list=[]
for char in range(nr_letters):
    password_list.append(random.choice(letters))
for char in range(nr_upper):
    password_list.append(random.choice(letters_upper))
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
# print(password_list)
# password = ""
# for char in password_list:
#     password += char
password = "".join(str(char)for char in password_list)
print(f"your password is: {password}")


