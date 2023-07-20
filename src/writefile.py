def writefile(input: str, filenames: list):
    for file in filenames:
        with open(file, "w") as f:
            f.write(input)
            f.close()