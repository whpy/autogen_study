# filename: generate_numbers.py

with open("numbers.txt", "w") as file:
    for i in range(1, 101):
        file.write(str(i) + "\n")