from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    #upper_case = int(request.GET.get('upper_case'))#int(input('Enter number of uppercase letters: '))
    #lower_case = int(request.GET.get('lower_case'))#int(input('Enter number of lowercase letters: '))
    #numerals = int(request.GET.get('numerals'))#int(input('Enter number of digits: '))
    #special_char = int(request.GET.get('special_char'))#int(input('Enter number of special characters: '))
    return render(request, 'generator/home.html')



def password(request):
    upper_case = int(request.GET.get('upper_case'), 2)#int(input('Enter number of uppercase letters: '))
    lower_case = int(request.GET.get('lower_case'), 2)#int(input('Enter number of lowercase letters: '))
    numerals = int(request.GET.get('numerals'), 2)#int(input('Enter number of digits: '))
    special_char = int(request.GET.get('special_char'), 2)#int(input('Enter number of special characters: '))

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
    list1 = [num for num in range(33,48)]+[num for num in range(58,65)]+[num for num in range(91,97)]+[num for num in range(123,127)]+[num for num in range(145,149)]+[152]

    #Generating random characters from the numbers in the list
    for num in range(special_char):
        special_char_list.append(chr(random.choice(list1)))

    password_char = upper_list + lower_list + numerals_list + special_char_list
    random.shuffle(password_char)
    result = ''.join(item for item in password_char)

    thepassword = result
    return render(request, 'generator/password.html', {'password': thepassword})
