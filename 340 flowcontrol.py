#Anthony Foretich
#Flow Control


x = int(input('Are you a numbers person or a words person? type 1 for numbers or 2 for words'))
if x == 1:
    for i in range (10):
        print(i)
    decision = input(' Would you like to see some more numbers? type y for yes or n for no ')
    if decision == "y":
        i = 0
        while i<8:
            print('heres another number:', i)
            i += 1
    else:
        print('Well then thats too bad mister numbers')
    
if x == 2:
    tony = ['Words', 'People','Buildings']
    print (tony)
    whatnow = input(' would you like to see some numbers now? y or n')
    if whatnow == "y":
        i = 0
        while i<20:
            print('heres a number:', i)
            i += 1
    else:
        print(' Well then thats too bad mister words ')
        
        

    
