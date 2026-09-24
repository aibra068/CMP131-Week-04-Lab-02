# Student Name: Amaney Ibrahim
# Course Number: CMP 131
# Week Number: 4
# Lab Number: 2
# Assignment Title: Basic Arithmetic Operations
# Date: 09/24/2026

# Program title
print("========== BASIC ARITHMETIC OPERATIONS ==========")
print()

# User input
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Arithmetic calculations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
power = first_number ** second_number
average = (first_number + second_number) / 2

# Output
print()
print("========== RESULTS ==========")
print()
print(f"First Number: {first_number:.2f}")
print(f"Second Number: {second_number:.2f}")
print()
print(f"Addition: {addition:.2f}")
print(f"Subtraction: {subtraction:.2f}")
print(f"Multiplication: {multiplication:.2f}")
print(f"Division: {division:.2f}")
print(f"Power: {power:.2f}")
print(f"Average: {average:.2f}")