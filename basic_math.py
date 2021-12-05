'''
Copyright (c) 2021, Tyler Chapp
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
'''
# simple python program that prompts user for a number to input,
# and performs several basic math calculations.
def main():
    # asking user for a number for the calculations
    number_in = int(input("What number do you want to use? "))
    simple_math(number_in)

#prints that number, that number squared, and that number cubed.
def simple_math(number):
    print(f'The number you chose was: {number}')
    print(f'{number} squared is: {number**2}')
    print(f'{number} cubed is: {number**3}')
   
main()
