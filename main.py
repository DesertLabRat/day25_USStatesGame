#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    template = letter_file.read()

with open("Input/Names/invited_names.txt", "r") as name_file:
    names = name_file.readlines()

for name in names:
    clean_name = name.strip()
    personalized_letter = template.replace("[name]", clean_name)

    output_path = f"Output/ReadyToSend/{personalized_letter}.txt"
    with open(output_path, "w") as output_file:
        output_file.write(personalized_letter)
