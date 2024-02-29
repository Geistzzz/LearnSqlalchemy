import time
import numpy as np
from tqdm import tqdm
# for i in tqdm(range(100)):
#     time.sleep(0.1)
import pandas as pd

t1 = time.time()
data = np.random.randint(1, 20, 1000000000)
t2 = time.time()
print(data)

t1 = time.time()
df = pd.DataFrame(data, columns=['DATA'])
t2 = time.time()

print(t2 - t1)

t1 = time.time()
tqdm(df.drop_duplicates(inplace=True))
t2 = time.time()

print(t2 - t1)
