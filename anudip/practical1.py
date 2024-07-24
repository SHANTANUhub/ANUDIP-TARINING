# convert the seconds given into the form of hr, min and sec
t = int(input("enter the time in seconds = "))
a = 0
b = 0
c = 0
if(t>0):
    if(t>=3600):
        a = t//3600 
        t = t%3600
    if(t>=60):
        b = t//60
        t = t%60
    if(t>0):
        c = t
    print("hr",a,"min",b,"sec",c)
else:
    print("invalid input")