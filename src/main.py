from sys import argv, exit

if "--version" in argv or "-v" in argv:
    print("Morselang Version 1.0.0")
if "--help" in argv or "-h" in argv:
    print("""
[-v/--version]      Prints the current version of the Morselang compiler to the terminal
[-h/--help]         Prints the Morselang compiler help to the terminal
[-f] <filename>
[-l] <language>     Allows you to select the output language
[-o] <file>         Select output file name""")
      
while True:
    try: 
        argv.remove("-v")
    except ValueError:
        break

while True:
    try: 
        argv.remove("-h")
    except ValueError:
        break

while True:
    try: 
        argv.remove("--version")
    except ValueError:
        break

while True:
    try: 
        argv.remove("--help")
    except ValueError:
        break

outputnames = []

try:
    lang = argv[argv.index("-l") + 1]
except ValueError:
    print("morselang: no output language set.")
    exit()
except IndexError:
    print("morselang: no output language set.")
    exit()

if not lang.upper() in ["python".upper(), "lua".upper(), "c".upper(), "cpp".upper(),
                         "cs".upper(), "java".upper(), "kotlin".upper(), "terminal_string".upper()]:
    print(f"morselang: {lang} is not a supported language!")
    exit()

def getOutputNames():
    try:
        for name in argv[(argv.index("-o") + 1):]:
            if name == "-l" or name == "-f":
                break
            outputnames.append(name)
    except ValueError:
        print("morselang: no output file defined.")
        exit()
    except IndexError:
        print("morselang: no output file defined.")
        exit()
try:
    infile = open(argv[argv.index("-f") + 1], "r").read()
except ValueError:
    print("morselang: no input file provided.")
    exit()
except IndexError:
    print("morselang: no input file provided.")
    exit()

if not lang.upper() == "terminal_string".upper():
    getOutputNames()

ll = lang.lower()

from writefile import writefile
from str_compile import str_compile

if ll == "c":
    from c import com
    try:
        writefile(com(str_compile(infile)), outputnames)
    except PermissionError:
        print("morselang: error while file writing.")
        print("Not enough permission to write.")
elif ll == "cpp":
    from cpp import com
    try:
        writefile(com(str_compile(infile)), outputnames)
    except PermissionError:
        print("morselang: error while file writing.")
        print("Not enough permission to write.")
elif ll == "cs":
    from cs import com
    try:
        writefile(com(str_compile(infile)), outputnames)
    except PermissionError:
        print("morselang: error while file writing.")
        print("Not enough permission to write.")
elif ll == "java":
    from java import com
    try:
        writefile(com(str_compile(infile)), outputnames)
    except PermissionError:
        print("morselang: error while file writing.")
        print("Not enough permission to write.")
elif ll == "kotlin":
    from kotlin import com
    try:
        writefile(com(str_compile(infile)), outputnames)
    except PermissionError:
        print("morselang: error while file writing.")
        print("Not enough permission to write.")
elif ll == "lua":
    from lua import com
    try:
        writefile(com(str_compile(infile)), outputnames)
    except PermissionError:
        print("morselang: error while file writing.")
        print("Not enough permission to write.")
elif ll == "python":
    from python import com
    try:
        writefile(com(str_compile(infile)), outputnames)
    except PermissionError:
        print("morselang: error while file writing.")
        print("Not enough permission to write.")
elif ll == "terminal_string":
    print(str_compile(infile))