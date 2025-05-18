#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

## Opened the file and stores names as a list of strings
with open("Input/Names/invited_names.txt") as file1:
    names_list = file1.readlines()
    cleaned_list = [name.strip() for name in names_list] ## removed the \n character from the words
print(cleaned_list)

for x,item in enumerate(cleaned_list):
    ## Reading the main Template file
    with open("Input/Letters/starting_letter.txt",mode = "r") as file2 :
         content = file2.read()
         ## Replacing the [name] spot in the file with the actual name
         replaced_line = content.replace("[name]",item)
    f_name = f"example{x}.txt"
    with open(f"Output/ReadyToSend/{f_name}", mode = "w") as file:
        file.write(replaced_line)