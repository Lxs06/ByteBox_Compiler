import os
import time

opcodes = {
    "load":"00001",
    "store":"00010",
    "add":"00011",
    "subtract":"00100",
    "load":"00101",
    "load":"00110",
    "load":"00111",
    "load":"01000",
    "load":"01001",
    "load":"01011",
    "load":"01100",
    "load":"01101",
    "load":"01111",
    "load":"10000",
    "load":"10001",
    "load":"10011",
    "load":"10100",
    "load":"10101",
    "load":"10110",
    "load":"10111",
    "load":"11000",
    "load":"11001",
    "load":"10001",
    "load":"10001",
    "load":"10001",
    "load":"10001",
    "halt":"11111"
}

line_count = 0

in_file = open('input.txt', "r")
lines = in_file.readlines()

os.remove('output.txt')
out_file = open('output.txt', "a")

start_time = time.time
for line in lines:
    line_count += 1
    newline = ""
    words = line.split(' ')
    for x in words:
        if x.isnumeric:
            x = bin(x)
            x = x.removeprefix("0b")
            x = x.removeprefix("1b")
        else:
            x.capitalize
            if x in opcodes:
                x = opcodes.get(x)
            else:
                end_time = time.time
                total_time = end_time - start_time
                print("There was an error in the code at line: " + line_count)
                print("After " + total_time + " seconds")
                in_file.close
                out_file.close
                os.remove('output.txt')
                exit()
        newline += x
    out_file.write(newline + '\n')
    print(newline)

end_time = time.time
total_time = end_time - start_time

in_file.close
out_file.close
print("Compiling Sucessfull in " + total_time + "seconds")