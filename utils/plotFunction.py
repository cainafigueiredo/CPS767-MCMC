import numpy as np
import seaborn as sns
sns.set_style("whitegrid")

def plotFunction(f, a, b, n):
    x = np.array(range(n+1))/n * (b-a) + a
    y = np.array([f(k) for k in x])
    sns.lineplot(x=x, y=y, color = 'red')