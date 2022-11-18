# Adam Edwards-Uribe
# section 85214-66
# 9/21/22
# Project 4

#A program that takes a user's input and shows the output for 7 calculations
print('This program will let you enter two integer values then show you all the possible answers.')
#User greeting
print('Please enter only whole numbers')
print()

#User input is taken and converted into integers
first=input('Please enter the first number: ')
first=int(first)
second=input('Please enter the second number: ')
second=int(second)
print()

#7 calculations with user's input
additionAnswer = first + second
subtractionAnswer= first - second
multiplyAnswer= first * second
divisionAnswer= first / second
floordivAnswer= first // second
modulusAnswer= first % second
powerAnswer= first ** second

#Results of the 7 calculations
print(first, '+', second, '=', additionAnswer)
print(first, '-', second, '=', subtractionAnswer)
print(first, '*', second, '=', multiplyAnswer)
print(first, '/', second, '=', format(divisionAnswer, ',.2f'))
print(first, '//', second, '=', floordivAnswer)
print(first, '%', second, '=', modulusAnswer)
print(first, '**', second, '=', format(powerAnswer, ',.0f'))
print()

#Exit message
print('Have a great day!')
