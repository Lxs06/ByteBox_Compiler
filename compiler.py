import os
import subprocess
import time

opcodes = {
    "load":"00001",
    "store":"00010",
    "add":"00011",
    "subtract":"00100",
    "increment":"00101",
    "decrement":"00110",
    "or":"00111",
    "and":"01000",
    "xor":"01001",
    "invert":"01010",
    "shiftup":"01011",
    "shiftdown":"01100",
    "video":"01101",
    "out":"01110",
    "in":"01111",
    "jump":"10000",
    "jumpif":"10001",
    "passth":"10010",
    "halt":"10011",
    "ldi":"10100",
    "sdi":"10101",
    "nor":"10110",
    "nand":"10111",
    "xnor":"11000",
    #"":"11001",
    "resetreg":"11010",
    #"":"11011",
    #"":"11100",
    #"":"11101",
    #"":"11110",
    #"":"11111"
}

line_count = 0
x_str = ""

try:
    in_file = open('input.txt', "r")
    lines = in_file.readlines()
except:
    print("error with input.txt file exiting in 10 seconds...")
    time.sleep(10)
    exit()

try:
    os.remove('output.txt')
except:
    print("output.txt file not found creating file")
out_file = open('output.txt', "a")

def error():
    line_count_str = str(line_count)
    print("There was an error in the code at line: " + line_count_str)
    in_file.close
    out_file.close
    os.remove('output.txt')
    time.sleep(10)
    exit()
    return
for line in lines:
    line_count += 1
    if line_count < 33:
        newline = ""
        words = line.split(' ')
        for x in words:
            print(x)
            if x.isnumeric() == True:
                x = int(x)
                if x < 256:
                    print(str(x))
                    x = format(x, '08b')
                else: 
                    if x != " ":
                        print("isnumeric error")
                        error()
            else:
                x.lower()
                try:
                    x = opcodes.get(x)
                except:
                    print("opcode error")
                    error()
            x_str = str(x)
            newline = newline + x_str
        if newline != None:
            newline = newline.replace("None", "")
            out_file.write(newline + '\n')
            print(newline)
    else:
        break

in_file.close
out_file.close
line_count_str = str(line_count)
print("Compiling Sucessfull (" + line_count_str + " lines)")
schem_question = input("Do you want to convert to a schematic(y/n): ")
if schem_question == "y" or schem_question == "Y":
    subprocess.run(["python", "out_to_mcschem.py"])
print("Exiting in 2 seconds...")
time.sleep(2)