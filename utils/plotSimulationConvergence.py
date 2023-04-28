import numpy as np
import seaborn as sns
from tqdm import tqdm
from matplotlib import pyplot as plt

sns.set_style("whitegrid")

def plotSimulationConvergence(nList, samplerFunction, referenceValue = None):
    x = nList
    y = [samplerFunction(n) for n in tqdm(nList)]
    fig = sns.lineplot(x = x, y = y)
    plt.xlabel('n')
    plt.ylabel('Simulation Value')
    if referenceValue is not None:
        fig.axhline(referenceValue, color='red', linestyle='--')
        plt.legend(["Simulation", f"Reference: {referenceValue:.4f}"])
    return fig

def plotRelativeError(nList, samplerFunction, referenceValue):
    x = np.array(nList)
    y = np.array([samplerFunction(n) for n in tqdm(nList)])
    y = abs(y - referenceValue)/referenceValue
    fig = sns.lineplot(x = x, y = y)
    plt.xlabel('n')
    plt.ylabel('Relative Error')
    return fig