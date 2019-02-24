#! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver'}

# Generate 3 quiz files.
for quizNum in range(3):
	
	# TODO: Create the quiz and answer key files.
	number = quizNum + 1
	quizFile = open(f'capitalsquiz{number}.txt', 'w')
	answerKey = open(f'capitalsquiz_answers{number}.txt', 'w')
	
	# TODO: Write out the header for the quiz.
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + f'State Capitals Quiz {number}')
	quizFile.write('\n\n')
	
	# TODO: Shuffle the order of the states.
	states = list(capitals.keys())
	random.shuffle(states)
	
	# TODO: Loop through 6 states, making a question for each.
	for questionNum in range(2):
	
	# Get right and wrong answers.
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
		
		# TODO: Write the question and answer options to the quiz file.
		a = states[questionNum]
		quizFile.write(f'{questionNum+1}. What is the capital of {a}?\n')
		for i in range(4):
			quizFile.write(' {0}. {1}\n'.format('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')
		
		# TODO: Write the answer key to a file.
		answerKey.write('{0}. {1}\n'.format(number, 'ABCD'[answerOptions.index(correctAnswer)]))

	quizFile.close()
	answerKey.close()

