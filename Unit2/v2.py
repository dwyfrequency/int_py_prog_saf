import scrabble, argparse, string
import numpy as np

def find_double_letter(letter):
    l2 = letter + letter
    for i in word_list:
        if l2 in i.lower():
            print(i.strip())

def no_dubs():
    """search for all the words that do not have an adjacent duplicate char"""
    for letter in string.ascii_lowercase:
        exists = False
        for word in scrabble.wordlist:
            if letter * 2 in word:
                exists = True
                break
        if not exists:
            print("There are no English words with a double", letter)

def all_vowels(word):
    v = "aeiou"
    for i in v:
        if i not in word:
            return False
    return True

def palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--double", action="store_true",
                        help="search scrabble dict for words with "
                        + "doubles")
    parser.add_argument("--list_no_dubs", action="store_true",
                        help="lists all words that do not "
                         + "do not contain double letters")
    parser.add_argument("--contain_all_v", action="store_true",
                        help="lists all words that contain"
                         + "all vowels")
    parser.add_argument("-p", action="store_true",
                        help="print all palindromes")
    parser.add_argument("-e", action="store_true",
                        help="enhanced palindrome finder")

    args = parser.parse_args()
    with open("sowpods.txt") as f:
        word_list = f.readlines()
        if args.double:
            find_double_letter(args.double)

        if args.list_no_dubs:
            no_dubs()

        if args.contain_all_v:
            for word in scrabble.wordlist:
                if all_vowels(word):
                    print(word)

        if args.p:
            total_count = 0
            longest = ""
            for word in scrabble.wordlist:
                if palindrome(word):
                    total_count += 1
                    if len(word) > len(longest):
                        longest = word
            print("Longest palindromes", longest)
            print("Total palindromes:", total_count)
        if args.e:
            longest = ""
            for word in scrabble.wordlist:
                # [::-1] -> reverses the list; give copy and stride by -1
                if word == word[::-1] and len(word) >len(longest):
                    longest = word
            print(longest)
