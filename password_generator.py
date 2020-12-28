import random

#inputs for number of each character type - upper case, lower case, numbers and special characters
upper_case = int(input('Enter number of uppercase letters: '))
lower_case = int(input('Enter number of lowercase letters: '))
numerals = int(input('Enter number of digits: '))
special_char = int(input('Enter number of special characters: '))

#Create empty lists for each character type
upper_list = []
lower_list = []
numerals_list = []
special_char_list = []

#Generate characters of each type and append to the respective empty list

for num in range(upper_case):
    upper_list.append(chr(random.randint(65,90)))

for num in range(lower_case):
    lower_list.append(chr(random.randint(97,122)))

for num in range(numerals):
    numerals_list.append(chr(random.randint(48,57)))

#Special characters do not have a continuous range in ASCII code, hence creating a list of the ASCII code for all characters, excluding spaces
list1 = [num for num in range(33,48)]+[num for num in range(58,65)]+[num for num in range(91,97)]+[num for num in range(123,127)]+[num for num in range(145,150)]+[152]

#Generating random characters from the numbers in the list
for num in range(special_char):
    special_char_list.append(chr(random.choice(list1)))

password_char = upper_list + lower_list + numerals_list + special_char_list
random.shuffle(password_char)
password = ''.join(item for item in password_char)
return(password)
