if __name__ == '__main__':
  n = int(raw_input())
integer_list = map(int, raw_input().split())

for i in xrange(n):
  integer_list[i] = int(integer_list[i])
t = tuple(integer_list)
print hash(t)
