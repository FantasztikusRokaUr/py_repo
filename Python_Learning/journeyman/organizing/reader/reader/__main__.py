import sys

import reader

r = reader.Reader(sys.argv[1])  # Here we create a reader object and passing our first command line argument to its initializer
try:
    print(r.read())             # use the read method from the class
finally:
    r.close()                   # use the close method from the class