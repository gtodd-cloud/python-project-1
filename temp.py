# Ask the user what acronym they want to add
acronym = input('What acronym do you want to add?\n')
# Then ask the user for the deinition
definition = input('What is the deinition?\n')
# Open the file
with open('acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')
# Write the new acronym and definition to the file