import argparse
from random import randint 
from urllib import request


def ask(prompt, valid=None):
    if valid:
        while True:
          print(prompt)
          inp_word = input()
          if inp_word in valid:
              break
          else:
              print("Ваше слово должно быть из списка слов, повторите попытку")
    else:
        print(prompt)
        inp_word = input()
    return inp_word
    

def inform(format_string, bulls, cows):
    print(format_string.format(bulls, cows))

    
def bullscows(guess, secret):
    bulls = 0 
    cows = 0
    for g, s in zip(guess, secret):
        if g == s:
            bulls += 1
    set_guess = set(list(x for x in guess))
    set_secret = set(list(x for x in secret))

    for elem in set_guess:
        if elem in set_secret:
            cows += 1
    return bulls, cows 

def gameplay(ask, inform, words):

    #choosing random word from words
    len_w = len(words)-1
    chosen_index = randint(0, len_w)
    chosen_word = words[chosen_index]

    count_of_guesses = 0
    
    #asking player to have a guess
    while True:
        cur_guess = ask("Введите слово: ", words)
        count_of_guesses += 1
        bulls, cows = bullscows(cur_guess, chosen_word)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        if cur_guess == chosen_word:
            return count_of_guesses
        

def main():
    bullcow_parser = argparse.ArgumentParser()
    bullcow_parser.add_argument('dict', type=str)
    bullcow_parser.add_argument('length', nargs = '?', default=5, type=int)

    args = bullcow_parser.parse_args()
    path_to_dict = args.dict

    if path_to_dict.startswith('http'):
        #read dict from URL
        words = request.urlopen(path_to_dict).read()
        words = words.decode("utf-8").splitlines()
    else:
        #read dict from local file
        with open(path_to_dict) as file:
            words = file.readlines()
    
    #chosing only words with rigth length
    words = [word.strip() for word in words if len(word.strip()) == args.length]

    print(gameplay(ask, inform, words))

if __name__ == "__main__":
    main()