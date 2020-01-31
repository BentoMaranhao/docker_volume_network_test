import datetime


def main():

    with open("/commom_volume/shared.txt", "a") as output:
        output.write(" ### test.py was here" + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    return


if __name__ == "__main__":
    main()