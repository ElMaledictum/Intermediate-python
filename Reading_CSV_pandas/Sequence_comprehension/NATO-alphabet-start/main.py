# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}


import pandas as pd
import os
os.system("cls")

data = pd.read_csv("nato_phonetic_alphabet.csv")
codes = {row.letter:row.code for row in data.itertuples(index=False)}

string = input("Enter a word to convert: ").upper()
coded_message = [codes[l] for l in string]
print(coded_message)
