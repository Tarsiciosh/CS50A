import sys
import csv

def main():

    """ 00 SEARCH """
    print("hello")
    names = ["Tomas", "Jack", "Brian"]

    # the (name[0]...) is a generator
    for item in (name[0] == "T" for name in names):
        print(item)

    # function any can accept generators as parameters 
    isThereNamesStartingWithT = any(name[0] == "T" for name in names)

    print(f"is there names starting with T: {isThereNamesStartingWithT}")

    shouldGivePermision = False
    permisionText = "yes, you can change settings"
    deniyalText = "No, you can't change settings"

    permision = permisionText if shouldGivePermision else deniyalText
    
    # equivalent in JavaScript: 
    # permision = shouldGivePermision ? permisionText : deniyalText  

    print(permision)

    myTuple = (["Pedro", "Pablo"], ["Hernandez", "Perez"])

    print(myTuple[0])
    print(myTuple[1])

    myList = ["one", "two", "three"]

    mySet = {"hello", "goodby"}

    myDictionary = {"myFirstKey": "myFistValue", "mySecondKe":"mySecondValue"}

    with open("test.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row["partNumber"])
            print(row["serialNumber"])
            print(row["price"]) 

    myTextNumber = "123"
    
    myNumber = int(myTextNumber) + 2 

    print (myNumber)
                    
if __name__ == "__main__":
    main()
