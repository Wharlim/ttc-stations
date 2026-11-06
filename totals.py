import sys

def main():
    total = 0
    for line in sys.stdin:
        line = line.removesuffix('\n')
        total = total + float(line)
    print("total:", total)


if __name__ == "__main__":
    main()