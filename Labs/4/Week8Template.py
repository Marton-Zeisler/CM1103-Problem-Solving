"""
Does it work on files where no error checking is needed on the fields

>>> sumRows("rows1.csv") == {'tim': 36.0, 'bob': 11.0, 'anna': 54.0}
True

Does it ignore headers if requested?

>>> sumRows("rows1.csv", header=True) == {'tim': 36.0, 'anna': 54.0}
True

Is it returning the right type of result?
>>> type(sumRows("rows1.csv"))
<class 'dict'>

Does it work on files with empty fields or fields which aren't numbers?

>>> sumRows("rows2.csv") == {'tim': 24.0, 'bob': 11.0, 'anna': 13.0}
True

Does it sum columns correctly?
>>> sumColumns("columns.csv") == {'': 0, 'tim': 5.0, 'bob': 41.0, 'anna': 55.0}
True
"""

# *** DO NOT CHANGE CODE ABOVE THIS LINE ***
# *** DO NOT ADD ANY COMMENTS OF YOUR OWN IN THE SUBMITTED SOLUTION ***
import csv

def isNumber(string):
    try:
        float(string)
        return True
    except:
        return False

def sumRows(filename, header=False):
    dict = {}
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for index, each in enumerate(reader):
            if index == 0 and header:
                continue
            total = 0
            for each2 in range(1,len(each)):
                if isNumber(each[each2]):
                    total += float(each[each2])
                
            dict[each[0]] = total
        
    return dict
                        

def sumColumns(filename):
    dict = {}
    nameColumns = {}
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for index, each in enumerate(reader):
            if index == 0:
                for index2, each2 in enumerate(each):
                    dict[each2] = 0
                    nameColumns[index2] = each2
            
            else:
                for index2, each2 in enumerate(each):
                    if isNumber(each2):
                        dict[nameColumns[index2]] += float(each2)
            
            
            
    
    #print(dict)
    #print(nameColumns)
    return dict
    
#print(sumRows("rows.csv", False))
sumColumns("columns.csv")

