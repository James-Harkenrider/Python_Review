import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_df)
nato_dict = {code.letter: code.code for (letter, code) in nato_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name_input = input("Enter your name: ")
nato_name = [nato_dict[letter.upper()] for letter in name_input]
print(nato_name)
