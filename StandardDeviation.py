# Python 3 code
# Bruce Adams
# austingamestudios.com
# ezaroth@gmail.com

n = int(input())
nums = [int(x) for x in input().strip().split()]
print(round((sum([(x-(sum(nums) / n))**2 for x in nums])/n)**.5, 1))
