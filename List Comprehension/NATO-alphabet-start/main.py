import pandas

##TODO 1. Create a dictionary in this format:
NATO_data = pandas.read_csv('nato_phonetic_alphabet.csv')

NATO_dictionary = {row.letter:row.code for (index, row) in NATO_data.iterrows()}
print(NATO_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic_alphabet():
    answer = input("Would you like to read the NATO dictionary? ").upper()
    try:
        result = [NATO_dictionary[n] for n in answer]
    except KeyError as result:
        print("Sorry, Only letters from the alphabet please")
        generate_phonetic_alphabet()
    else:
        print(result)

generate_phonetic_alphabet()