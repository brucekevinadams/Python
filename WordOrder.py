
# Python 3 code
# Bruce Adams
# austingamestudios.com
# ezaroth@gmail.com

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
