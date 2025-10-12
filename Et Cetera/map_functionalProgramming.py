def main():
    yell("This" , "is" , "my" ,"code")
    #trying to replicate how print can take more than one argument at once.

def yell(*words):
    # this astrisk for more than one argument.
    uppercased = map(str.upper , words)
    print(*uppercased)
    # this astriks for unpacking.

main()