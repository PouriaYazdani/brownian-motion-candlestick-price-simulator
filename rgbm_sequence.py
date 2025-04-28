import numpy as np
import matplotlib.pyplot as plt

def rgbm_sequence(popen, pclose, phigh, plow) :
    """
    Simulate and plot synthetic price path from a Reflected Geometric Brownian Motion(rgbm) sequence and 
    rescale it to match provided market bounds.

    This method generates a sequence of prices using a Geometric Brownian Motion (GBM) model 
    based on the given open, close, high, and low prices. The generated sequence is rescaled 
    to ensure the prices remain within the given bounds.

    Args:
        popen (float): Opening price of the asset.
        pclose (float): Closing price of the asset.
        phigh (float): Highest price of the asset.
        plow (float): Lowest price of the asset.

    Notes:
        - The method uses 60 timesteps to simulate 1 minute of price data.
        - The generated price sequence starts at the popen price and ends at the pclose price.
        - Rescaling ensures that the simulated sequence adheres to the given high (phigh) 
        and low (plow) prices.

    Sample Implementation:
        https://www.kaggle.com/code/mikolajhojda/geometric-brownian-motion-simulation-for-s-p500
    
    """
    # Constants for the GBM model
    T, N = 60, 60  # Total duration and number of time steps
    dt = 1 / T  # Time step size

    # Parameters for GBM
    mu = np.log(pclose / popen)  # Drift
    sigma = (phigh - plow) / popen  # Volatility

    # Time and Brownian motion
    t = np.linspace(0, 1, N)
    W = np.cumsum(np.random.standard_normal(size=N)) * np.sqrt(dt)  # Brownian motion
    # import ipdb; ipdb.set_trace()  # Debugging line to inspect S_rescaled

    # GBM computation
    X = (mu - 0.5 * sigma**2) * t + sigma * W
    S = popen * np.exp(X)  # Geometric Brownian motion

    # Rescaling to match the candle bounds
    S_shifted = S - S.min()
    S_scaled  = S_shifted * ((phigh - plow) / S_shifted.max())
    S_scaled += plow
    idx_max = np.argmax(S_scaled)
    idx_min = np.argmin(S_scaled)
    S_scaled[idx_max] = phigh
    S_scaled[idx_min] = plow
    S_rescaled = S_scaled
    S_rescaled[0] = popen
    S_rescaled[-1] = pclose

    plt.style.use('dark_background')

    time_steps = np.arange(len(S_rescaled))

    plt.figure(figsize=(10, 5))
    plt.plot(time_steps, S_rescaled, marker='o', linestyle='-', label='Simulated Price', color="white")
    plt.axhline(y=phigh, linestyle='--', label='phigh', color='lightgreen')
    plt.axhline(y=plow,  linestyle='--', label='plow', color='tomato')
    plt.axhline(y=popen,  linestyle='--', label='popen', color='white')
    plt.axhline(y=pclose,  linestyle='--', label='pclose', color='white')
    plt.title('GBM-Interpolated Intra-Minute Price Path', color='white')
    plt.xlabel('Time (seconds)', color='white')
    plt.ylabel('Price', color='white')
    plt.ylim(plow - 0.1, phigh + 0.1)
    plt.tick_params(colors='white')
    plt.legend()
    plt.tight_layout()

    plt.show()

rgbm_sequence(popen=1002, pclose=1003, phigh=1003.4, plow=1001.8) # bullish
rgbm_sequence(popen=1001, pclose=1000.5, phigh=1001.2, plow=1000.3)  # bearish

