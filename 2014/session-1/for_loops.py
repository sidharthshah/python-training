def square(x):
    """
    Function with argument
    """
    return x*x

def hello():
    """
    Function without argument
    """
    print "Hello World!"

if __name__ == "__main__":

    #Simple FOR loop
    for i in range(100):
        print square(i)

    #Invocation of function
    hello()

    #Three main type of datastructures

    #List uses square brackets
    my_list = []

    #Dictionary uses curly braces
    names = {}

    #Tuple uses round brackets (non mutable)
    my_tuple = ()

    #You can append multiple types to list
    my_list.append(1)
    my_list.append("Yo Bro!")
    my_list.append(3.14)
    my_list.append([])

    print my_list

    #Slice elements of list
    print my_list[2:]
    print my_list[:3]
    print my_list[-2:]

    #Sorting
    my_nums = [9,6,7,1,0,100]
    my_nums.sort()
    print my_nums

    #Create dictionary
    names["Jimit"] = "Shah"
    names["Sidharth"] = "Shah"
    names["Prasen"] = "Revankar"

    #Get total number of elements in dictionary
    print len(names)

    #Check membership of an element in dictionary
    print names.has_key("Oankar")

    #Inline assignment of dictionary
    colors = {"Jimit": "Pink", "Sidharth": "White"}
    print colors

    #Create a file and write to file
    file_to_save = open("squares.txt", "w")
    for i in range(1,101):
        rec = "%s\n" % (str(i))
        file_to_save.write(rec)
    file_to_save.close()

    #Read file line by line
    file_to_read = open("squares.txt")
    for line in file_to_read.readlines():
        print line.strip()

    #String concatenation
    string_a = "Hello World"
    string_b = "Wow Wow"

    print string_a + " " + string_b
    print string_a, string_b

    #Searching within a string
    print string_a.find("Wor")
    print string_a.find("Wow")

    #Print all method/attributes within an object
    print dir(names)

    #If you need help with some module use help
    #print help(commands)

    #Iterating over list
    for element in my_list:
        print element

    #Use enumerate to find index and value of an element
    for i, element in enumerate(my_list):
        print i, "->", element

    #Iterating over a dict
    for k, v in names.items():
        print k, "=>", v

    #Only iterate over keys
    for k in names:
        print k, "=>" ,names[k]

    #Get all values
    print names.values()

    #You can join a list by your delimiter of choice
    print "\t".join(names.keys())
    print ",".join(names.keys())
    print ":_:".join(names.keys())

    #Split string into list
    even_number = "2,4,6,8,10"
    even_number_list = even_number.split(",")
    print even_number_list

    #Find datatype of an element
    print type(even_number_list[0])

    #map takes two arguments 1. function 2. list
    #outputs a list
    total = sum(map(int, even_number_list))
    print total

    #Inline functions can be created using lambdas
    str_len = lambda x: len(x)
    is_odd = lambda x: x%2 != 0
    names = ["Sidharth", "Sumam", "Vikram", "Oankar", "Prasen", "Gaurav", "Jose", "Aniket", "Jimit"]
    print sum(map(str_len, names))

    #Filter all lenghts that are odd
    print sum(filter(is_odd, map(str_len, names)))