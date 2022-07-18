import sys
import pyfiglet


def main():
    if not(len(sys.argv) == 1 or len(sys.argv) == 3):
        sys.exit()

    figlet = pyfiglet.Figlet()

    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in figlet.getFonts():
            print("Invalid Usage")
            sys.exit()
        figlet.setFont(font=sys.argv[2])
    text = input("Input: ")
    print(figlet.renderText(text))


main()
