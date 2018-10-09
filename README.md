# simple-keyword-password-generator

Serves to generate bruteforce password dictionaries from victim's known info (keywords).

## Usage
'''
from pass_generator import PassGenerator

words = ['admin', 'john', 'moscow']
words_count = 3
pass_gen = PassGenerator(words, words_count)
'''

## Variables

**words** - known keywords (some data) about victim. E.g. phone number, birthday, so on.

**words_count** - deepest level of recursion you want. In other words the maximum number of words combined together.