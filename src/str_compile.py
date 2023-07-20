from sys import exit

def str_compile(input: str):
    outputstr = input.replace("       ", " ! ")
    if outputstr.endswith(" "):
        outputstr = outputstr[:-1]
    compiled_str = []
    position = 0
    for letter in outputstr.split(" "):
        position += 1

        if letter == "._":
            compiled_str.append("A")
        elif letter == "_...":
            compiled_str.append("B")
        elif letter == "_._.":
            compiled_str.append("C")
        elif letter == "_..":
            compiled_str.append("D")
        elif letter == ".":
            compiled_str.append("E")
        elif letter == ".._.":
            compiled_str.append("F")
        elif letter == "__.":
            compiled_str.append("G")
        elif letter == "....":
            compiled_str.append("H")
        elif letter == "..":
            compiled_str.append("I")
        elif letter == ".___":
            compiled_str.append("J")
        elif letter == "_._":
            compiled_str.append("K")
        elif letter == "._..":
            compiled_str.append("L")
        elif letter == "__":
            compiled_str.append("M")
        elif letter == "_.":
            compiled_str.append("N")
        elif letter == "___":
            compiled_str.append("O")
        elif letter == ".__.":
            compiled_str.append("P")
        elif letter == "__._":
            compiled_str.append("Q")
        elif letter == "._.":
            compiled_str.append("R")
        elif letter == "...":
            compiled_str.append("S")
        elif letter == "_":
            compiled_str.append("T")
        elif letter == ".._":
            compiled_str.append("U")
        elif letter == "..._":
            compiled_str.append("V")
        elif letter == ".__":
            compiled_str.append("W")
        elif letter == "_.._":
            compiled_str.append("X")
        elif letter == "_.__":
            compiled_str.append("Y")
        elif letter == "__..":
            compiled_str.append("Z")
        elif letter == ".____":
            compiled_str.append("1")
        elif letter == "..___":
            compiled_str.append("2")
        elif letter == "...__":
            compiled_str.append("3")
        elif letter == "...._":
            compiled_str.append("4")
        elif letter == ".....":
            compiled_str.append("5")
        elif letter == "_....":
            compiled_str.append("6")
        elif letter == "__...":
            compiled_str.append("7")
        elif letter == "___..":
            compiled_str.append("8")
        elif letter == "____.":
            compiled_str.append("9")
        elif letter == "_____":
            compiled_str.append("0")
        elif letter == "!":
            compiled_str.append(" ")
        elif letter == "":
            print("morselang: error while compiling.")
            print(f"Empty token at position {position}")
            print("Empty tokens can appear when having too many spaces between tokens.")
            print("Quitting ...")
            exit()
        else:
            print("morselang: error while compiling.")
            print(f"Unknown token at position {position}")
            print("Quitting ...")
            exit()
    endstr = ""
    for compiled_token in compiled_str:
        endstr = endstr + compiled_token
    
    return endstr