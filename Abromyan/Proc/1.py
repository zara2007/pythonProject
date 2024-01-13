def mean (x,y):
    AMean = (x+y)/2
    GMean = (x*y)**(1/2)
    print (AMean,GMean)

x,y = map(int,input().split())
mean(x,y)


