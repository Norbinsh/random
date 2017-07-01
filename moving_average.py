import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

def movingaverage(values, window):
    weights = np.repeat(1.0, window) / window
    sma = np.convolve(values, weights, 'valid')
    return sma

def percentchange(startingpoint, currentpoint):
    return (float(currentpoint) - startingpoint) / abs(startingpoint) * 100.00

# mva_array = movingaverage([random.randint(0,10000) for x in range(1, 100)], 2)
clean_array = [100,90,80,0,0,0,0,0,0,0,0,70,20,15,16,30,200,1000, 200,30,80,90,70,50,20,100,200,1000,2000]
mva_array = movingaverage(clean_array, 2)

d1 = np.r_[0, np.abs(mva_array[1:] - mva_array[:-1])]
d2 = np.r_[np.abs(mva_array[1:] - mva_array[:-1]), 0]

mask = (d1 < 200) | (d2 < 200)
print(len(mva_array[mask]))
print(len(mva_array))
plt.scatter(range(len(mva_array)), mva_array[mask], 'o')
# # plt.scatter(range(len(clean_array)), clean_array)
plt.show()

# for num in clean_array:
#     pc = percentchange(clean_array[0], num)
#     print(num, '/////', pc)



#
# print(type(mva_array))
# m_series = pd.Series(mva_array)
# pct_array = m_series.pct_change()
#
# for i in pct_array:
#     if i > 5:
#         print(i)
#         # this is where i want to go to the index i represents and remove it and its preceding digit from the original array.
