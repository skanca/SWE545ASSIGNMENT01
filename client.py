import xmlrpclib
import random

def list_functions():
    return 'LST : Select and Print Two Random Numbers \n' \
           'SUM : Print the sum of numbers \n' \
           'PRD : Print the product of numbers \n' \
           'EXT - Exits the client '

server = xmlrpclib.Server('http://www.advogato.org/XMLRPC')
global number01, number02
number01 = 0
number02 = 0
while True:
    print list_functions()
    input = raw_input("Please Enter a Command")
    if input == 'LST':
        number01 = random.randint(0,100)
        number02 = random.randint(0,100)
        print str(number01) + " " + str(number02)
    elif input == 'SUM':
        sum,product = server.test.sumprod(number01, number02)
        print sum
    elif input == 'PRD':
        sum,product = server.test.sumprod(number01, number02)
        print product
    elif input == 'EXT':
        break
    else:
        print 'UnDefined command'