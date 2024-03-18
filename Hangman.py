def welcome():
    print(r"""    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
                                            
""")



def choose_word(file_path, index):

    """
        a function that gets file path and int num and it
         returns the chosen word
        :param file_path: the path of the file that contains the text
        :param index: the number of the word that is in the file
        :type file_path: str
        :type index: int
        :return: it returns the chosen word
        :rtype: str
        """
    my_list, new_list, count_list, last_list = [], [], [], []

    with open(file_path, "r") as file1:
        for line in file1:
            my_list.append(line.strip())

    for element in my_list:
        new_list += element.split(' ')

    count, all_count = 0, 0
    for i in new_list:
        all_count += 1
        if i not in count_list:
            count += 1
            count_list.append(i)

    if index <= all_count:
        word = new_list[index - 1]
    else:
        diff = index // all_count
        index_count = index - (diff * all_count)
        word = new_list[index_count - 1]

    return word


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    a function that get list and str ,then checks if
     the letter is in the list and if its alphabet and 1 length long
    :param old_letters_guessed: the list that we
    get as input, and we check on it(list)
    :param letter_guessed: a str that we get as
     an input and checks it(letter, str)
    :type old_letters_guessed: list
    :type letter_guessed: str
    :return: it returns true/false depends on the rules
     that are written in the first line
    :rtype: return bool
    """
    letter_guessed = letter_guessed.lower()
    if (letter_guessed.isalpha()) and (len(letter_guessed) == 1) and \
            (letter_guessed not in old_letters_guessed):
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed, num_of_tries, secret_word):

    """
    a function that get list and str ,then checks if the letter
     is in the list and if its alphabet and 1 length long
    :param old_letters_guessed: the list that we get as input,
     and we check on it(list)
    :param num_of_tries: number that counts how many tries have the user tried
    :param letter_guessed: a str that we get as an
     input and checks it(letter, str)
    :param secret_word: the secret word that we want the user to guess
    :type old_letters_guessed: list
    :type num_of_tries: int
    :type letter_guessed: str
    :type secret_word: str
    :return: it returns true/false depends on the, and it returns
     flag true if the guessed letter was in the old_letters_guessed
     rules that are written in the first line
    :rtype: return bool
    """
    flag1 = False
    bool_answer = check_valid_input(letter_guessed, old_letters_guessed)
    letter_guessed = letter_guessed.lower()

    if bool_answer is True:
        old_letters_guessed += letter_guessed
        if letter_guessed in secret_word:
            return True, flag1
        else:
            old_letters_guessed = sorted(old_letters_guessed)
            print("X\n" + " -> ".join(old_letters_guessed))
            print_hangman(num_of_tries)
            return False, flag1
    else:
        if letter_guessed in old_letters_guessed:
            flag1 = True
        old_letters_guessed = sorted(old_letters_guessed)
        print("X\n" + " -> ".join(old_letters_guessed))
        if (flag1 is False) and (letter_guessed.isalpha()) and (len(letter_guessed) == 1):
            print_hangman(num_of_tries)
        return False, flag1


def check_win(secret_word, old_letters_guessed):

    """
    a function that gets a string and guessed letters,
     than it checks if all the secret_word letters are in the guessed letters
    :param secret_word: the string that we get randomly(str)
    :param old_letters_guessed: the letters that the player has typed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: it returns true when the secret_word
     letters are all in the guessed letters
    :rtype: bool
    """
    new_str = ""
    for element in secret_word:
        if element in old_letters_guessed:
            new_str += element
        else:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):

    """
    a function that gets a string and guessed letters and put
     the right guessed letters in the right place , and leaves
    the other(unGuessed letters) with _ in there place
    :param secret_word: the string that we get randomly(str)
    :param old_letters_guessed: the letters that the player has typed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: it returns the string that have the guessed letters and _ in it
    :rtype: str
    """

    new_str = ""
    for element in secret_word:
        if element in old_letters_guessed:
            new_str += element + ' '
        else:
            new_str += '_ '

    if new_str == "":
        new_str += " "

    if new_str[-1] == " ":
        new_str = new_str[:-1]

    return new_str


def print_hangman(num_of_tries):

    """
    a function that gets a int number and prints a
     picture depends on what is the number
    :param num_of_tries: a number that we get after (number) times
    :type num_of_tries: int
    :return: it returns the picture of the try
    :rtype: string
    """
    HANGMAN_PHOTOS = {0: """ x-------------x
    |
    |
    |
    |
    |""", 1: """x-------------x
    |       |
    |       0
    |
    |
    |""", 2: """x-------------x
    |       |
    |       0
    |       |
    |
    |""", 3: """x-------------x
    |       |
    |       0
    |      /|\\
    |
    |""", 4: """x-------------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 5: """x-------------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}

    print(HANGMAN_PHOTOS[num_of_tries])


def main():

    welcome()
    path1 = input("enter a path of file: ")
    index = int(input("enter the index of the word: "))
    print("""Let's Start!
    x-------x  """)
    old_letter_guessed, MAX_TRIES, num_of_tries = [], 6, 0
    is_win, is_valid, flag = False, False, False
    secret_word = choose_word(path1, index)
    print(show_hidden_word(secret_word, old_letter_guessed) + '\n')

    while num_of_tries < MAX_TRIES:
        guess = input("\nguess a letter: ")
        is_valid, flag = try_update_letter_guessed(guess, old_letter_guessed, num_of_tries, secret_word)
        if (flag is True) or (guess.isalpha() is False) or (len(guess) > 1):
            num_of_tries -= 1
        num_of_tries += 1

# if the guessed letter is valid than we don't have to add tries
        # , and i show the user the hidden word
        if is_valid:
            num_of_tries -= 1
            print(show_hidden_word(secret_word, old_letter_guessed))
        else:
            if flag is False:
                print(show_hidden_word(secret_word, old_letter_guessed))

# check if the user won
        is_win = check_win(secret_word, old_letter_guessed)
        if is_win:
            print("YOU WON")
            break
# check if the user ended up losing with 6 tries(not guessing the secret_word)
    if is_win is False:
        print(f"YOU LOST\nThe Word Is: {secret_word}")


if __name__ == "__main__":
    main()
