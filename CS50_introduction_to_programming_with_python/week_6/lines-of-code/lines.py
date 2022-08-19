import sys
import os


def main():

    if len(sys.argv) != 2:
        print("program accept exactly one command-line argument")
        sys.exit()
    fname = sys.argv[1]
    validateFile(fname)
    noOfLines = countLines(fname)
    print(noOfLines)



def validateFile(fname):

    if not(os.path.isfile(fname)):
        print("File doesn't exist")
        sys.exit()
    
    if fname[len(fname) - 3: len(fname)] != ".py":
        print("File must end with .py")
        sys.exit()
    
    
def countLines(fname):
    
    with open(fname) as file:
        noOfLines = 0
        for line in file:
            if len(line.strip()) != 0 and line.strip()[0] != '#':
                noOfLines += 1
        return noOfLines


if __name__ == "__main__":
    main()