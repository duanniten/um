import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if finds := re.findall(r'(^|\W)um($|\W)', s, flags= re.IGNORECASE):
        return len(finds)
    return 0


if __name__ == "__main__":
    main()