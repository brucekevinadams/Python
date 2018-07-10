# Author: Bruce Adams
# email: ezaroth@gmail.com
# website: austingamestudios.com
# Python 3 code

def split_and_join(line):
    # write your code here
    return line.replace(" ","-")
	
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)	
