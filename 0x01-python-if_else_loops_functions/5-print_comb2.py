#!/usr/bin/python3
for i in range(100):
    output = f"{i:02}"
    if i != 99:
        output += ","
    else:
        output += "\n"
    print(output, end="")
