import re


def strcmp(firstStr, secStr):

    return "OK" if (re.compile(secStr.replace("*", ".*"))).match(firstStr) else "KO"


def main():
    firstStr = input("Введите первую строку ")
    secStr = input("Введите вторую строку: ")
    print(strcmp(str(firstStr), str(secStr)))



if __name__ == "__main__":
    main()
