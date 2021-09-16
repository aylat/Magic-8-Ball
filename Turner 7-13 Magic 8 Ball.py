# This program will generate a random response for a user question

import random   # Importing random module

def main():
    # Create a list with 12 spaces
    responses = [''] * 12

    # Open the file for processing
    response_file = open('8_ball_responses.txt', 'r')

    # Strip the newline character from the end and store each element
    index = 0
    for line in response_file:
        responses[index] = line.rstrip('\n')
        index += 1

    # Close the input file
    response_file.close()

    # Set flag to control the loop
    another_question = 'y'

    # Loop for questions and answers
    while another_question.lower() == 'y':

        # Get question from user
        question = input('Enter a yes/no question: ')

        # Generate and print a response
        print(responses[random.randint(0, len(responses)-1)])

        # Ask the user if they have another question
        another_question = input('Do you have another question? y/n ')

main()
    
    

