# Creación de folders para guardar los resultados y la data 
 
import os

os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)
os.makedirs('data/submissions', exist_ok=True)
os.makedirs('notebooks/manuel', exist_ok=True)
os.makedirs('notebooks/harvey', exist_ok=True)
os.makedirs('notebooks/anthony', exist_ok=True)
os.makedirs('notebooks/stephany', exist_ok=True)
os.makedirs('src', exist_ok=True)


# Notebook header

# %load_ext autoreload
# %autoreload 2
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'

# import os
# import numpy as np
# import pandas as pd
# import sklearn
# import matplotlib.pyplot as plt
# import seaborn as sns
# from tqdm import tqdm, tqdm_notebook
# from pathlib import Path
# import random


# seed = 2020
# random.seed(seed)

# pd.set_option('display.max_columns', 1000)
# pd.set_option('display.max_rows', 400)
# sns.set()

# os.chdir('..')

# DATA = Path('data')
# RAW  = DATA/'raw'
# PROCESSED = DATA/'processed'
# SUBMISSIONS = DATA/'submissions'    