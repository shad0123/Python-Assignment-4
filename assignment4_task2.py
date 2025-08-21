user_input = input("Enter text to write to the file: ")

file = open('output.txt','w')
file.write(user_input)
file.write('\n')
file.close()
print("Data successfully written to output.txt.\n")

additional_data = input("Enter additional text to append: ")

file = open('output.txt','a')
file.write(additional_data)
file.close()
print("Data successfully appended.\n")

print("Final content of output.txt:")
file = open('output.txt','r')
print(file.read())
file.close()