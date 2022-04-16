#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from pathlib import Path
name_folder = Path("/Python_programs/Intermediate-python/Mail_merge/Mail Merge Project Start/Input/Names")
letter_folder = Path("/Python_programs/Intermediate-python/Mail_merge/Mail Merge Project Start/Input/Letters")
output_folder = Path("/Python_programs/Intermediate-python/Mail_merge/Mail Merge Project Start/Output/ReadyToSend")

def name_list():
    with open(name_folder / "invited_names.txt", "r") as names:
        n_list = names.readlines()
        new = []
        for i in n_list:
            j = i.strip()
            new.append(j)
        return new

with open(letter_folder / "starting_letter.txt", "r") as sample:
    l1 = sample.readline().strip()
    sample_content = sample.readlines()

for each_name in name_list():
    with open(output_folder / f"letter_for_{each_name}.txt", "w") as output:
        new_l1 = l1.replace("[name]", each_name)
        sample_content[0] = new_l1 + "\n\n"
        output.writelines(sample_content)
        