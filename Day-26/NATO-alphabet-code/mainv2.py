# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_word():
    try :
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except:
        print("Sorry try again.")
        generate_word()
    else:
        print(output_list)
generate_word()