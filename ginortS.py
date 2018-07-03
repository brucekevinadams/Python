# Python 3 code
# Bruce Adams
# austingamestudios.com
# ezaroth@gmail.com

myList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
print(*sorted(input(), key = myList.index), sep ="")
