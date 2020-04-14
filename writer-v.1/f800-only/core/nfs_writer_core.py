import numpy as np
import h5py


d1 = np.random.random(size = (100000,250000))
d2 = np.random.random(size = (100000,250000))


hf = h5py.File('/gonzo/hdf5/data-core.h5', 'w', driver='core', backing_store=True  )

hf.create_dataset('dataset_1', data=d1)
hf.create_dataset('dataset_2', data=d2)

hf.close()

