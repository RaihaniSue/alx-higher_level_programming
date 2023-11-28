#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        output= f"{i}{j}"
        if i != 8 or j != 9:
            output += ","
        else:
            output += "\n"
        print(output, end="")
