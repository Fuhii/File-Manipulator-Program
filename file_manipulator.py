import sys

def main(arg):
    if arg[1] == "reverse":
        reverse(arg[2], arg[3])
    elif arg[1] == "copy":
        copy(arg[2], arg[3])
    elif arg[1] == "duplicate_contents":
        duplicate_contents(arg[2], arg[3])
    elif arg[1] == "replace_string":
        replace_string(arg[2], arg[3], arg[4])
    else:
        sys.stdout.write(b"Command not found")

def reverse(inputpath, outputpath):
    contents = ""

    with open(inputpath) as i:
        contents = i.read()
    reverse_contents = "".join(list(reversed(contents)))

    with open(outputpath, "w") as o:
        o.write(reverse_contents)

def copy(inputpath, outputpath):
    contents = ""

    with open(inputpath) as i:
        contents = i.read()

    with open(outputpath,  "w") as o:
        o.write(contents)

def duplicate_contents(inputpath, n):
    contents = ""

    with open(inputpath, "r+") as i:
        contents = i.read()
        i.write(contents*int(n))

def replace_string(inputpath, needle, newstring):
    contents = ""

    with open(inputpath, "r+") as i:
        contents  = i.read()
        i.write(contents.replace(needle, newstring))

if __name__ == "__main__":
    main(sys.argv)
