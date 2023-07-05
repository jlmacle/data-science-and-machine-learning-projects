import numpy as np
from ds_ml_utils.plotting import Plotting  as plotting_class

plotting = plotting_class()

# A dataset about classifying even and odd numbers
# Numpy arrays with data
training_set_x = np.arange(0,21)
training_set_y = np.array([1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])

# Plotting the dataset
plotting.plot_dataset(training_set_x, training_set_y, "Training set", "x", "y")


