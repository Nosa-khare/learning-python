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

answer_set = set(answer)
submission_set = set(submission)

print(submission_set.intersection(answer_set))

# if submission == answer:
#     print('Correct Answer! :)')
# # if

# else:
#     print('Wrong Answer! :(')

