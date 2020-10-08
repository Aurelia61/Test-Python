def function_1(arg):
    print("In function_1")

def function_2(arg):
    print("In function_2")

def function_3(fileName):
    print("In function_3")
    return print(fileName)


def createDictionary():

    dict = {

        1 : function_1,
        2 : function_2,
        3 : function_3,

    }    
    return dict

dictionary = createDictionary()
dictionary[3]("test""num""2")#pass any key value to call the method
