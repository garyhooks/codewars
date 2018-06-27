#!/usr/bin/env python

def main():
    mydict = {
        "apple" : "green",
        "banana" : "yellow",
        "strawberry" : "red"
    }

    #### ADD AN ITEM
    mydict["blueberry"] = "blue"

    #### REMOVE AN ITEM
    del(mydict["banana"])

    #### Length of dict
    length = len(mydict)
    print("length is now " + str(length))

    #### remove item and return it
    mydict.pop("strawberry")
    length = len(mydict)
    print("length is now " + str(length))


if __name__ == "__main__":
    main()