#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
invited_names_path = "./Input/Names/invited_names.txt"
with open(invited_names_path, 'r') as guest_list:
    for line in guest_list.readlines():
        names.append(line.strip('\n'))

letter_contents = []
starting_letter = "./Input/Letters/starting_letter.txt"
with open(starting_letter, 'r') as letter:
    for line in letter.readlines():
        letter_contents.append(line)

for name in names:
    title = f"./Output/ReadyToSend/letter_for_{name}.txt"
    individual_letter = open(title, 'w')
    for line in letter_contents:
        if line.split(" ")[-1] == '[name],\n':
            line = f"Dear {name},\n"
        individual_letter.write(line)
    individual_letter.close()

