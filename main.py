# this is my first question game
# welcome user to the game,
print('Hello, welcome to Collins game!')
# user get to answer questions,
answer = input('Are you ready to play ? (yes/no) :')
# user input response either yes/no
score = 0
total_q = 3
if answer.lower() == 'yes':
    answer = input('q 1: do you like sports ?')
if answer.lower() == 'yes':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')
answer = input('q 2: do you like candy ?')

if answer.lower() == 'yes':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

answer = input('q 3: do you like generations USA ?')
if answer.lower() == 'yes':
    score += 1
    print('correct')
else:
    print('Wrong Answer :(')

    print('bye, thank you!')