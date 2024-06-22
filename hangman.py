#################################################################
# FILE : ex4.py
# WRITER : Jamil Barbara , jamil_barbara1 , 212695894
# EXERCISE :  ex4 2022
# DESCRIPTION: hangman game
#################################################################

from hangman_helper import *


def update_word_pattern(word, pattern, letter):
    """
    A function that receives a word,the current pattern
     and a letter, and returns a new pattern containing the same letter.
    :param word: a word
    :param pattern: the current pattern
    :param letter: a letter from a to z
    :return: a new pattern that contains the same letter."""
    new_pattern = ''
    index = 0
    for i in word:
        if i == letter:
            new_pattern += letter
        else:
            new_pattern += pattern[index]
        index += 1
    return new_pattern


def run_single_game(word_list, score):
    """
    A function that receives a list of words and a number of
    points, and runs one game The function return at the
    end the number of points of the player.
    :param word_list: a list of word
    :param score: the number of points
    :return: the number of points
    """
    word = get_random_word(word_list)
    wrong_guess = []
    pattern1 = "_"*len(word)
    msg = "Let's start the game!"
    while score > 0 and pattern1 != word:
        display_state(pattern1, wrong_guess, score, msg)
        choice = get_input()
        if choice[0] == LETTER:
            score, pattern1, wrong_guess, msg = choice_is_letter(score, pattern1, word, wrong_guess,choice)
        elif choice[0] == WORD:
            score -= 1
            if choice[1] == word:
                score, pattern1, msg = choice_is_word(score, pattern1, word, choice)
        elif choice[0] == HINT:
            msg = "You asked for a hint"
            choice_is_hint(word_list, pattern1, wrong_guess)
            score -= 1
    if score > 0:
        msg = "you have won the game. "
        display_state(pattern1, wrong_guess, score, msg)
    else:
        msg = f"you lost the game. the word is {word}"
        display_state(pattern1, wrong_guess, score, msg)
    return score


def main():
    """
    a function that didn't receives parameters and return values
    :return: none
    """
    word1 = load_words()
    score1 = run_single_game(word1, POINTS_INITIAL)
    number_of_games = 1
    while True:
        if score1 > 0:
            msg1 = f"your games number are {number_of_games}, your points are {score1} " \
                   f"and do you want to plat again?: "
            decision1 = play_again(msg1)
            if decision1:
                number_of_games += 1
                score1 = run_single_game(word1, score1)
            else:
                break
        else:
            msg2 = f"the number of games are {number_of_games}, your points are {score1}" \
                   f"do you want to play a new round?: "
            decision2 = play_again(msg2)
            if decision2:
                number_of_games = 1
                score1 = run_single_game(word1, POINTS_INITIAL)
            else:
                break


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    a function that receives as input a list of words, pattern,
    and a list of wrong guess

    :param words: a list of words
    :param pattern: the current pattern
    :param wrong_guess_lst: a list of wrong guess
    :return: a list that contains the words that fit to the
     pattern and the wrong guess.
    """
    new_lst = []
    for i in range(len(words)):
        if len(pattern) == len(words[i]) and filter_index_list(words[i], pattern) and filter_wrong_lst(words[i], wrong_guess_lst):
            if words[i] in new_lst:
                pass
            else:
                new_lst.append(words[i])
    return new_lst


def filter_index_list(word, pattern):
    """
    a function that receives as input a list of words, pattern
    and return True if the word match the pattern
    :param word: a list of words
    :param pattern: the current pattern
    :return: True or False
    """
    for j in range(len(pattern)):
        if pattern[j] != "_" and (word[j] != pattern[j] or word.count(word[j]) != pattern.count(word[j])):
            return False
    return True


def filter_wrong_lst(word1, wrong_guss_lst):
    """
    a function that return true if the word don't exist
    in the wrong guess lst.
    :param word1: a word
    :param wrong_guss_lst: a list of wrong guess
    :return: a boolean value
    """
    for i in range(len(word1)):
        if word1[i] in wrong_guss_lst:
            return False
    return True


def choice_is_letter(score, pattern1, word, wrong_guess, choice):
    """
    A function that check if the guess is letter
    :param choice: the choice of the user
    :param wrong_guess: a list of wrong guess
    :param pattern1: the current pattern.
    :param word: a random word from the words.txt
    :param score: the number of points
    :return: the number of points,the pattern, a list of wrong guss
    and a msg
    """
    msg = " "
    if len(choice[1]) > 1 or choice[1].isupper() or not (choice[1].isalpha()):
        msg = "this choice is invalid"
    elif choice[1] in wrong_guess:
        msg = "you already have chose this letter!"
    else:
        score -= 1
        if choice[1] in word:
            msg = "Good guess!"
            pattern1 = update_word_pattern(word, pattern1, choice[1])
            n = word.count(choice[1])
            points = (n * (n + 1) // 2)
            score += points
        else:
            msg = "The letter is wrong!!"
            wrong_guess.append(choice[1])
    return score, pattern1, wrong_guess, msg


def choice_is_hint(word_list, pattern1, wrong_guess):
    """
    a function that give the player hints
    :param pattern1: the current pattern
    :param word_list: a list of word
    :param wrong_guess: a list of wrong guess
    :return: the number of points, a massage and a list of words
    """
    lst_of_words = filter_words_list(word_list, pattern1, wrong_guess)
    if len(lst_of_words) > HINT_LENGTH:
        new_lst_word = []
        n = len(lst_of_words)
        for i in range(HINT_LENGTH):
            new_lst_word.append(lst_of_words[i * n // HINT_LENGTH])
        show_suggestions(new_lst_word)
    else:
        show_suggestions(lst_of_words)


def choice_is_word(score, pattern1, word, choice):
    """
    a function that check if the guess is word

    :param choice: the choice of the user
    :param score: the number of points
    :param word: a random word from the words.txt
    :param pattern1: the current pattern.
    :return: the number of points ,the pattern and a msg
    """
    msg = " "
    if choice[1] == word:
        n = pattern1.count("_")
        points1 = (n * (n + 1) // 2)
        score += points1
        pattern1 = word
    else:
        msg = "Your guess is wrong!"
    return score, pattern1, msg


if __name__ == "__main__":
    main()