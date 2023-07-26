# Morselang Compiler

## Introduction

Morselang is a compiled programming language. \
\
The compiler allows many settings on how you wish to compile your Morselang program.
### First: Available Output Languages:

- Python
- Lua
- C
- C++
- C# (DotNet Framework)
- Java
- Kotlin

**Choose language and output file.**

```
$ morse-lang -f mycode.morse -l python -o output.py
$ morse-lang -f mycode.morse -l lua -o output.lua
$ morse-lang -f mycode.morse -l c -o output.c
$ morse-lang -f mycode.morse -l cpp -o output.cpp
$ morse-lang -f mycode.morse -l cs -o output.cs
$ morse-lang -f mycode.morse -l java -o output.java
$ morse-lang -f mycode.morse -l kotlin -o output.kt
```

**NOTE:** The name of the language is not case-sensitive, for example it would still take ```PYtHoN``` as a valid argument for a language.

### Secondly: You can output the compiler output as a string of text in your terminal:

```
$ morse-lang -f mycode.morse -l terminal_string

HELLO WORLD
```

**NOTE:** The -o argument is not required, because it isn't being written to a file. \
If you want to write the output to a file. There is the feature to write the output of a command to a file in every popular shell. Just try that.

### Third: Spaces, ending a letter/number, other
\
**Spaces:**

To set a space as the compiler output, you'll need to add 7 spaces between the two letters/numbers, between which you want to place a space. \
Why?

In Morse code, if you want to set a space, you'll silently wait the duration of 7 dots. \
\
**Ending a letter/number:**
\
To state that you are done with a letter/number, set a space after the morse code of the letter/number you want to seperate from the next one. \
\
Hello World Example:

```
.... . ._.. ._.. ___       .__ ___ ._. ._.. _..
```
\
**New lines and carriage returns.**

Due to the supported letters of the international morse code, new lines (\n) and carriage returns (\r) are sadly not supported.

## Installation

**INFO:** You can run the raw Python files, but it is not recommended if you want for example add morselang to your System's PATH, etc. \
**IMPORTANT NOTE:** Please keep your terminal open the entire time until you are finished, do not close it, if you don't know how to work with a terminal.


1. Install dependencies

- Python 3 (Newest recommended.)
- pip (Usually comes bundled with Python)
- git (Preinstalled on most Linux distros, usually needs manual installation on other Operating systems.)
- pyinstaller:

```
pip install pyinstaller
```

2. Cloning source

```
git clone https://github.com/Simoso68/Morselang
cd Morselang
```

3. Building

You can manually build it with a PyInstaller Command, but I wrote a build script. \
I recommend to use that, because the installation from now on depends on the output of THIS script. \
If you don't want to, feel free to read the code of the script and understanding what it does. \
I won't give an in-depth explanation what it does.

On Windows:

```batch
python build.py
```

On Linux or MacOS:

```bash
python3 build.py
```

4. Adding to PATH

The PATH allows you to execute any file from anywhere in your terminal, it is pretty useful.

On Windows: \
**IMPORTANT:** Now, no mindless copying. Do it one by one, because if you don't, it wont work.
```powershell
powershell
New-Item -Path $Env:LOCALAPPDATA -Name "Morselang" -ItemType "directory"
Copy-Item -Path "out/morselang.exe" -Destination "$Env:LOCALAPPDATA/Morselang"
[Environment]::SetEnvironmentVariable("Path", $Env:PATH + ";" + $Env:LOCALAPPDATA + "/Morselang;")
```

On Linux (and maybe MacOS, but not tested):

```
sudo cp /out/morselang /usr/bin/morselang
sudo chmod +x /usr/bin/morselang
```

On MacOS: \
There are no installation instructions for MacOS specifically, but you can try the Linux Installation instructions, due to both systems being Unix-like.

## Using it

### Arguments

```
morselang -f {file-containing-morsecode} -l {targeted-output-language} -o {names-of-the-output-files}
```

Example:

```
morselang -f MyCode.morse -l c -o firstFile.c secondFile.c
```

## License

Morselang is licensed under the GNU GPL Version 3. \
For more information, read the License file.
