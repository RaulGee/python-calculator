#! /usr/bin/python3

import inquirer

num1 = input("Choose a number: ")
num2 = input("Choose another number: ")

questions = [
	inquirer.List("Operators",
		message = "What would you like to do with the numbers?",
		choices = ['Add', 'Subtract', 'Multiply', 'Divide']
	),
]
answers = inquirer.prompt(questions)


if answers == {'Operators': 'Add'}:
	print(float(num1) + float(num2))
elif answers == {'Operators': 'Subtract'}:
	print(float(num1) - float(num2))
elif answers == {'Operators': 'Multiply'}:
	print(float(num1) * float(num2))
elif answers == {'Operators': 'Divide'}:
	print(float(num1) / float(num2))
else:
	print("What is happening")

