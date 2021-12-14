# Example code for https://scicoding.com/waterfilling/

import numpy as np


# Number of channels 
N = 10
N0 = 1 # Normalized noise level
SNR_dB = 10 # The signal to noise ratio in dB
P = 10**(SNR_dB/10) # Sum power budget defined via the SNR

# The channel specific gains drawn from Gaussian distribution
g = np.abs(np.random.randn(N, 1)) 
G = np.diag(g[0:,0]) # Make gains a diagonal matrix

# Bisection search for alpha
alpha_low = min(N0/g) # Initial low
alpha_high = (P + np.sum(N0/g)) / N # Initial high

stop_threshold = 1e-5 # Stop threshold

# Iterate while low/high bounds are further than stop_threshold
while(np.abs(alpha_low - alpha_high) > stop_threshold):
    alpha = (alpha_low + alpha_high) / 2 # Test value in the middle of low/high

    # Solve the power allocation
    p = 1/alpha - N0/g 
    p[p < 0] = 0 # Consider only positive power allocation
    
    # Test sum-power constraints
    if (np.sum(p) > P): # Exceeds power limit => lower the upper bound
        alpha_low = alpha
    else: # Less than power limit => increase the lower bound
        alpha_high = alpha
        
# Print the achievable rate in nats/s
print(np.sum(np.log(1 + g*p/N0)))

