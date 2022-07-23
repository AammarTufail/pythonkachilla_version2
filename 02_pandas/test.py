import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.lineplot(x='day', y='total_bill', data=tips)