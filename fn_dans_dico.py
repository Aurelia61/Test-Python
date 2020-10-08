def function_1(arg):
    print("In function_1")

def function_2(arg):
    print("In function_2")

def change_letter(fileName):
    print("changement de H ")
    # return print(fileName)


# def createDictionary():

touch_functions = {

    1 : function_1,
    2 : function_2,
    "K_SPACE" : change_letter,

}    
    # return dict

# dictionary = createDictionary()
touch_functions[2]("test""num""2")#pass any key value to call the method

