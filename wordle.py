import random

NO_EXIST = '⬜'
WRONG_SPOT = '🟨'
CORRECT = '🟩'
NUM_GUESSES = 6

def get_words_from_file(filename):
  words = []
  with open(filename, 'r') as file:
    for line in file:
      for word in line.split():
        words.append(word)
  return words

def choose_random_word(words):
  return words[random.randrange(len(words))]

def validate_guess(guess, wordlist):
  return (guess in wordlist)

def get_pattern(guess, answer):
  pattern = ''
  yellows = []
  for i in range(len(guess)):
    if guess[i] == answer[i]:
      pattern += CORRECT
    elif guess[i] in answer:
      yellows.append(guess[i])
      total_occurrences = answer.count(guess[i])
      existing_occurrences = yellows.count(guess[i])
      if existing_occurrences <= total_occurrences:
        pattern += WRONG_SPOT
      else:
        pattern += NO_EXIST
    else:
      pattern += NO_EXIST
  return pattern

def print_guesses(guesses):
  for guess in guesses:
    print(guess)

wordle_La = get_words_from_file('wordle-La.txt')
wordle_Ta = get_words_from_file('wordle-Ta.txt')
answer = choose_random_word(wordle_La)
guesses = []
victory = False

print("Welcome to Wordle!")
while (len(guesses) < NUM_GUESSES):
  guess = input("\nEnter a guess: ")
  if not validate_guess(guess, wordle_La + wordle_Ta):
    print("Invalid word, try again.\n")
    continue
  guesses.append(' ' + guess + " -> " + get_pattern(guess, answer))
  print_guesses(guesses)
  if guess == answer:
    victory = True
    print("You win! The word was:", answer, '\n')
    break

if not victory:
  print("Out of guesses! The word was:", answer)