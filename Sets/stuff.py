from difflib import SequenceMatcher as sm
from random import randint


words_dict = {
    1: {
        'P_i_ant_o_i_t': 'Philantropist'},
    2: {
        'T_b_e': 'Table'}
}


dict_item_count = len(words_dict)
key = randint(1, dict_item_count)
item = words_dict[key]

words_list = list(item.keys())

word = words_list[0]
answer = words_dict[key][word].lower()

submission = input(f"Type in the complete word, {word}\n>")

match_proportion = sm(None, submission, answer).ratio()

if submission == answer:
    print('Correct Answer! :)')
elif match_proportion >= 0.7:
    print("Oops! You may have spelled Incorrectly")
else:
    print('Wrong Answer! :(')

