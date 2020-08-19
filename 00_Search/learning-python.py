import sys

def main():
    print("hello")
    names = ["Tomas", "Jack", "Brian"]

    isThereNamesStartingWithT = any(name[0] == "T" for name in names)

    print (isThereNamesStartingWithT)

if __name__ == "__main__":
    main()
