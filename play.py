import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
a = np.linspace(-10, 10, 100)
def sin(x):
    y = np.sin(x)
    return y

b = sin(a)
a_smooth = np.linspace(a.min(), a.max(), 1000)
b_smooth = make_interp_spline(a, b)(a_smooth)
plt.plot(a_smooth, b_smooth, color='y')
plt.title('review on smooth plot')
plt.show()

