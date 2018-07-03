
# Python 3 code
# Bruce Adams
# austingamestudios.com
# ezaroth@gmail.com

from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
