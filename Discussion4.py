# Setup
rounds = int(input('How many holes will you play? '))
par = int(input('What is the par for the course? '))
hole = 1
score = []

# The Loop
for i in range(rounds, 0, -1):
    # Capture input as an integer
    score_input = int(input(f'What did you score on {hole}? '))
    
    # Add to our list
    score.append(score_input)
    hole = hole + 1
    while hole <= rounds:
        print(f'Onto hole {hole}!') 
        break
    # Move to the next hole
   

# Results
print(f'For {rounds} holes today you scored {sum(score)}')
if sum(score) < par:
    print(f'You beat par by {par - sum(score)}!')
elif sum(score) > par:
    print(f'You were {sum(score) - par} over par.')
print("Hope you had a great day on the course!")