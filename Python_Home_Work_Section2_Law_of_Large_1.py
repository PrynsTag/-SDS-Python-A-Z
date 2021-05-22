import numpy as np
from numpy.random import randn

counter = 0
num_tries = 10  # Sample Size

for i in randn(num_tries):
    if -1 <= i <= 1:
        counter += 1  # Increase counter by 1 when i falls between -1 and 1

percent_ans = np.mean(counter / num_tries) * 100
print(percent_ans)
