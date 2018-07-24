def geo_dist(p, n):
    result = (1-p)**(n-1)*p
    return("%.3f" % result)

a = input().split(" ")
a = list(map(int, a))
n = int(input())

print(geo_dist(a[0]/a[1],n))
