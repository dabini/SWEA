import numpy as np
import scipy.interpolate as ip
from scipy.interpolate import splrep, splev
import sys

n = int(input)
quantity_num = int(input)
quantity = [int(input) for _ in range(quantity_num)]
price_num = int(input)
price = [int(input) for _ in range(price_num)]

x0 = np.linspace(0, max(quantity_num), quantity_num)

for i in range(quantity_num):
    spl = splrep(quantity[i], price[i])

y1 = splev(n, spl)
print(y1)