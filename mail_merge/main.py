#TOD: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("input/Names/invited_names.txt") as names:
    guests = names.readlines()

number = 0


with open("input/Letters/starting_letter.docx") as starting_letter:
    letter = starting_letter.read()
    for guest in guests:
        number += 1
        stripped_guest = guest.strip()
        target = letter.replace("[name]", stripped_guest)
        with open(f"output/ReadyToSend/target_{number}.docx", mode="w") as finish:
            finish.write(target)
        

