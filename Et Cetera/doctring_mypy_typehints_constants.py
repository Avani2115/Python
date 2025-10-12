def meow(n: int) -> str:  # type hint
    
    #restructured text
    #a type of markdown language for documentation. Docstrings
    
    """ 
    Meow three times. 

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: as str
    """
    return "meow" * n 

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
