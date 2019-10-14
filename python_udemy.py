import pandas as pd
import numpy as np

#array1 = np.zeros(4)
#array2 = np.ones(4)

i=0

while(i<300):
    if(i%2==0):
        array1 = np.zeros((i+2)//2)
        print(array1)
    else:
        array2 = np.ones((i+1)*2)
        print(array2)
    i=i+1
