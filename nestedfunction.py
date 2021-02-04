# must call function1 in order to call for function2

def function1():
    print("Hello from outer function")
    def function2():
        print("hi from innner function")
    function2()

function1()
