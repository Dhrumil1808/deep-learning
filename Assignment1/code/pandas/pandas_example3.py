import pandas as pd
import numpy as np

panel = np.random.rand(1,2,3)
panel = pd.Panel(panel)
print panel