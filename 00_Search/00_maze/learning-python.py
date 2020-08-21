import sys

def main():
    print("hello")
    names = ["Tomas", "Jack", "Brian"]

    # the (name[0]...) is a generator
    for item in (name[0] == "T" for name in names):
        print(item)

    # any can accept generators as parameters 
    isThereNamesStartingWithT = any(name[0] == "T" for name in names)

    print(f"is there names starting with T: {isThereNamesStartingWithT}")
    # print("A", end="")
    # print("B", end="")
    # print(" ", end="")
 
if __name__ == "__main__":
    main()
