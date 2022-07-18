TOP_COLORS = ['\033[38;2;143;8;8m','\033[38;2;157;67;0m','\033[38;2;151;114;0m','\033[38;2;121;158;0m','\033[38;2;0;200;0m','\033[38;2;0;255;255m']

class bcolors:
    CYAN = '\u001b[38;5;51;1m'
    GREEN = '\033[0;32m'
    RED = '\033[91m'
    BLUE = '\u001b[34m'
    YELLOW = '\u001b[38;5;226m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def printANSIColors():
    import sys
    for i in range(16):
        for j in range(16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print(u"\u001b[0m")
