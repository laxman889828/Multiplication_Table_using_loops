#Using While Loop
def Tables():
    x=int(input("enter your no."))
    y=(x*10)
    i=0
    while(i <= 100000000000):
        if i==y:
            break
        i=i+x
        print(i)
Tables()
Tables()
Tables()
Tables()    


#Using For Loop
def Tables():
    x=int(input("enter your no."))
    y=(x*10)
    for i in range (0,10000000000,x):
        if i==y:
            break
        i=i+x
        print(i)
    
Tables()
Tables()
Tables()
Tables()


