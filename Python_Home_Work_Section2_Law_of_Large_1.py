import numpy as np
from numpy.random import randn
counter = 0
num_tries = 10 # Sample Size

for i in randn(num_tries):
    if i >= -1 and i <= 1:
        counter += 1 # Increase counter by 1 when True

percent_ans = np.mean(counter/num_tries)*100
print(percent_ans)