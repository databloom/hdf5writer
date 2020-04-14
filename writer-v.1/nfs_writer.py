import numpy as np
import h5py
import time


d1 = np.random.random(size = (100000,250000))
d2 = np.random.random(size = (100000,250000))


timestr = time.strftime("%Y%m%d-%H%M%S")

hf = h5py.File('/gonzo/hdf5/'+timestr+'-data.h5', 'w')

hf.create_dataset('dataset_1', data=d1)
hf.create_dataset('dataset_2', data=d2)

hf.close()

