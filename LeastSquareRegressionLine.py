
# Python 3 code
# Bruce Adams
# austingamestudios.com
# ezaroth@gmail.com
# Program problem from Hackerrank.com 

x,y=[],[]
for i in range(5):
    student = [int(i) for i in input().split()]
    x+=[student[0]]
    y+=[student[1]]

mean_x = sum(x)/5
mean_y=sum(y)/5

x_squared,xy = sum([x[i]*x[i] for i in range(5)]),sum([x[i]*y[i] for i in range(5)])

b= (5*xy - sum(x)*sum(y))/(5*x_squared - sum(x)**2)
a = mean_y - b*mean_x

print(round(a+b*80,3))
