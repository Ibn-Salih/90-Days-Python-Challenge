# - Topics:
# - Learn how to read and write files in Python using open(), read(), write().
# - Working with text and CSV files.
# - Project:
# - Write a script that reads a text file 
# and counts how many lines and words are in the file.



file_path = str(input("Enter the file path with no quote: "))

line = 0
word = 0

with open(file_path, "r", encoding="utf-8") as file:
    for lines in file:
        line += 1
        word += len(lines.split())  

print(f"Lines: {line}")
print(f"Word Count: {word}")
