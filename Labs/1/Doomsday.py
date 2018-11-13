def doomsday(y):
    
    """
    >>> doomsday(2012)
    3
    >>> doomsday(1899)
    2
    >>> doomsday(1923)
    3
    >>> doomsday(10000)
    -1
    >>> doomsday(1756)
    -1
    >>> type(doomsday(2010))
    <class 'int'>
    """
    
    # There are a number of alternative ways of performing this test, e.g.
    # if 1800 <= y < 1900:
    # if 1800 <= y and 1900 > y:
    # if y in range(1800,1900):
    #
    # Important points - use if, elif (else-if), and else, remember
    #    to use the == operator to test if values are equal, not =
    if y / 100 == 18:
        x = 5
    elif y / 100 == 19:
        x = 3
    elif y / 100 == 20:
        x = 2
    elif y / 100 == 21:
        x = 0
    else:
        # Returning early if the value is outside the range is neatest
        #   otherwise we need a lot of "if x != -1:" statements later 
        #   on
        return -1
    
    # Easist way to find the year in the century is to take the remainder
    #    after / by 100. A common alternative approach was to convert to
    #    a string, take the last two characters and convert back, but
    #    this is as elegant, or robust (e.g. depending on how it was
    #    implemented, may not work for years like 598). 
    w = y % 100
    
    a = w / 12
    b = w % 12
    c = b / 4
    # Remember brackets - this is not the same as d = a + b + c % 7
    #    - this would have failed one of the doctests
    d = (a + b + c) % 7
    
    # As above. Also, some solutions used:
    #    if (d + x) >= 7: d = d - 7
    # This works (since d must be < 7), but in my opinion is not
    # quite as elegant.
    #
    # Finally, note that we "return" the answer, not print it. This 
    #    makes the function more useful. If you failed the doctest:
    #
    # >>> type(doomsday(2010))
    # <class 'int'>
    #
    #    then you probably printed the result instead.    
    return (d + x) % 7
    
