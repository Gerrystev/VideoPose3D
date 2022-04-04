import numpy as np
# save np.load
np_load_old = np.load

# modify the default parameters of np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

data = np.load('data_3d_humaneva15.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])