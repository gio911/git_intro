def visual():
    print('Hello from module')
    
print('Hi')

def summing(a,b):
    c=0
    c=a+b
    
    return c

import os
from dotenv import load_dotenv

load_dotenv()

val = os.environ.get('password')

print(val)


if __name__=='__main__':
    visual()
    