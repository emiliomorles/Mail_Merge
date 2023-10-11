PLACEHOLDER = "[name]"


with open("Input/Names/invited_names.txt") as open_file:
    names = open_file.readlines()
    # Names from invited_names.txt file are turned into a list of names
    # print(names)

with open("Input/Letters/starting_letter.txt") as letter_file:
    # It creates a letter using starting_letter.txt
    letter_contents = letter_file.read()
    for name in names:  # for each name in invited_names.txt it...
        stripped_name = name.strip()  # ...eliminates the "\n" after the name.
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # ...replaces the [name] placeholder with the actual name.
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)  # ...saves the letters in the folder "ReadyToSend".

# Methods used:
# 1: https://www.w3schools.com/python/ref_file_readlines.asp
# 2: https://www.w3schools.com/python/ref_string_replace.asp
# 3: https://www.w3schools.com/python/ref_string_strip.asp
