import pandas as pd

data1 = pd.read_csv("nato_phonetic_alphabet.csv")
# data_dict = data1.to_dict()
# print(data_dict)

phonetic_dict = {row.letter : row.code for (index,row) in data1.iterrows()}
print(phonetic_dict)

name = input("Enter the name: ").upper()
for x in name:
    # print(x)
    if x in phonetic_dict.keys():
        print(x,"-",phonetic_dict[x])