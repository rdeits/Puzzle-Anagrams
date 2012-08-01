import itertools
import nltk


def shuffle(s):
    for result in itertools.permutations(s):
        yield reduce(str.__add__, result)

morse_lengths = {'e': 1,
                 'i': 2,
                 's': 3,
                 't': 3,
                 'a': 4,
                 'h': 4,
                 'n': 4,
                 'd': 5,
                 'r': 5,
                 'u': 5,
                 'b': 6,
                 'f': 6,
                 'l': 6,
                 'm': 6,
                 'v': 6,
                 'g': 7,
                 'k': 7,
                 'w': 7,
                 'c': 8,
                 'p': 8,
                 'x': 8,
                 'z': 8,
                 'o': 9,
                 'j': 10,
                 'q': 10,
                 'y': 10}

old_morse_lengths_with_spaces = {'a': 4,
                                 'b': 8,
                                 'c': 6,
                                 'd': 6,
                                 'e': 1,
                                 'f': 7,
                                 'g': 7,
                                 'h': 7,
                                 'i': 3,
                                 'j': 9,
                                 'k': 7,
                                 'l': 4,
                                 'm': 5,
                                 'n': 4,
                                 'o': 4,
                                 'p': 9,
                                 'q': 8,
                                 'r': 6,
                                 's': 5,
                                 't': 2,
                                 'u': 6,
                                 'v': 8,
                                 'w': 7,
                                 'x': 8,
                                 'y': 8,
                                 'z': 8}

code_to_use = old_morse_lengths_with_spaces

def letters_with_length(l):
    return [key for key in code_to_use if code_to_use[key] == l]
# print letters_with_length(3)


def letters_from_numbers(numbers):
    # print "\n"
    # print numbers
    if numbers == []:
        return []
    n = numbers[0]
    following_letters = letters_from_numbers(numbers[1:])
    if following_letters == []:
        result = [[l] for l in letters_with_length(n)]
    else:
        result = []
        for l in letters_with_length(n):
            # print "letter", l
            result += [[l] + s for s in following_letters]
    # print numbers
    # print following_letters
    # print result
    return result

# print letters_from_numbers([1, 1, 1])
# print letters_from_numbers([1, 2, 1])
# print letters_from_numbers([3, 1, 3])

words = set(nltk.corpus.words.words())


def anagram_words(numbers):
    letter_sets = letters_from_numbers(numbers)
    tried_sets = []
    for s in letter_sets:
        s.sort()
        # print s
        if s not in tried_sets:
            for p in shuffle(s):
                if p in words:
                    # print p
                    yield p
            tried_sets.append(s)

def caesar_words(numbers):
    letter_sets = letters_from_numbers(numbers)
    for s in letter_sets:
        for x in range(26):
            potential_word = ''.join([caesar_shift(c, x) for c in s])
            if potential_word in words:
                yield x, potential_word


def caesar_shift(c, x):
    """
    Caesar shift letter c by amount x
    """
    if ord(c) > 96:
        # lowercase
        return chr(((ord(c) - 97 + x) % 26) + 97)
    elif ord(c) > 64:
        # uppercase
        return chr(((ord(c) - 65 + x) % 26) + 65)

# print [word for word in anagram_words([4, 6, 6])]

# Wrapping around newlines
# number_sets = [[4, 6, 6],
#                [7, 7, 8, 3, 4, 1, 2, 1, 5],
#                [9, 1, 7],
#                [5, 1, 8, 3, 7],
#                [9, 3, 6, 1, 4, 3, 2, 1, 6],
#                [8, 3, 9, 3, 8, 3, 5],
#                [5, 3, 2, 1, 5],
#                [4, 3, 6, 1, 6, 1, 6, 1, 9],
#                [5, 3, 7, 3, 8, 3, 4],
#                [5, 3, 8, 1, 8, 1, 2, 1, 6, 4, 2],
#                [5, 5, 7]]

# Breaking at newlines (incomplete)
number_sets = [[4, 6, 6],
               [7, 7, 8, 3, 4],
               [1, 2, 1, 5],
               [9, 1, 7],
               [5, 1, 8, 3, 7],
               [9, 3, 6],
               [1, 4, 3, 2, 1, 6],
               [8, 3],
               [9, 3, 8, 3, 5],
               [5, 3, 2]]


# number_sets = [[4, 3, 2, 3, 4, 3, 6, 1, 6],
#                [1, 6, 4, 5, 2, 3, 5, 8, 3],
#                [4, 3, 7, 8, 7, 7]]

# Each line wraps onto itself
# number_sets = [[4, 6, 6, 7, 7, 8, 3, 4],
#                [1, 2, 1, 5],
#                [9, 1, 7]]

# Columns
# number_sets = [[5, 3, 2, 3, 4],
#                [6, 3, 8],
#                [8, 1, 9]]

if __name__ == "__main__":
    for num_set in number_sets:
        print num_set
        # print set(anagram_words(num_set))
        # print [''.join(letter_set) for letter_set in letters_from_numbers(num_set)]
        print list(caesar_words(num_set))
        print "\n"
