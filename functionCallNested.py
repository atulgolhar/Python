#!/usr/bin/env python3
# functionCallNested.py

def goodie1():                              

    print('Hi def goodie1')
    def goodie2():
        print('Hi def goodie2')

    def goodie3():
        print('Hi def goodie3')
        def goodie4():
                print('Hi def goodie4 via goodie3')
        goodie4()

    def goodie5():
            print('Hi def goodie5')

    goodie2()
    goodie3()
    goodie5()    

    def goodie8():
        print('Hi goodie8 imbedded Defined->Call SHOULD WORK')

    goodie8()

def goodie6():
    
    def goodie7():
        print('Hi goodie7 via goodie6')
    
    print('Hi def goodie6')     
    goodie7()    

# goodie1()
# goodie6()
# print("ALL DONE then...")

# to run
# temp.goodie1()
# temp.goodie6()
