import sys

def main():
    print("hello")
    names = ["Tomas", "Jack", "Brian"]

    isThereNamesStartingWithT = any(name[0] == "T" for name in names)

    print(f"is there names starting with T: {isThereNamesStartingWithT}")
    print("A", end="")
    #print("B", end="")
    #print(" ", end="")

if __name__ == "__main__":
    main()
