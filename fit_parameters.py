"""Fit parameters"""
from typing import Dict
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import least_squares


def lhhw_model(data: Dict[str, np.ndarray]) -> np.ndarray:
    """LHHW model"""

    r_t = 8.314 * data["T"]
    num = 71.82 * np.exp(7867 / r_t) * data["p_meoh"] ** 2
    den = (
        1
        + 3.9471e-4 * np.exp(37835 / r_t) * np.sqrt(data["p_meoh"])
        + 5.6057e-6 * np.exp(47468 / r_t) * data["p_h2o"]
    )
    return num / (den**4)


def power_model(
    data: Dict[str, np.ndarray], params: Dict[str, float]
) -> np.ndarray:
    """Power model"""
    r_t = 8.314 * data["T"]
    p_meoh_alpha = data["p_meoh"] ** params["alpha"]
    p_h20_beta = data["p_h2o"] ** params["beta"]
    return (
        params["k0"] * np.exp(-params["Ea"] / r_t) * p_meoh_alpha * p_h20_beta
    )


PARAM_NAMES = ["k0", "Ea", "alpha", "beta"]


def residual(params: np.ndarray, data: Dict[str, np.ndarray]) -> np.ndarray:
    """Return the residual value"""
    params = dict(zip(PARAM_NAMES, params))
    return power_model(data, params) - lhhw_model(data)


def create_mesh(
    temp: np.ndarray, p_meoh: np.ndarray, p_h2o: np.ndarray
) -> Dict[str, np.ndarray]:
    """Return mesh grid with data"""
    vals = np.meshgrid(temp, p_meoh, p_h2o)
    return {
        "T": vals[0].reshape((vals[0].size,)),
        "p_meoh": vals[1].reshape((vals[1].size,)),
        "p_h2o": vals[2].reshape((vals[2].size,)),
    }


# pylint: disable=invalid-name
n_temp = 76
n_p_meoh = 51
temp_vals = np.linspace(325, 400, n_temp)
p_meoh_vals = np.linspace(50, 100, n_p_meoh)
p_h2o_vals = np.linspace(50, 100, 51)
all_data = create_mesh(temp_vals, p_meoh_vals, p_h2o_vals)
param_0 = [71.82, 7867, 2, 0]

r_val = least_squares(lambda params: residual(params, all_data), param_0)
fit_params = dict(zip(PARAM_NAMES, r_val["x"]))

# Fix p_h2o
fix_p_h2o = 75
test_data = create_mesh(temp_vals, p_meoh_vals, fix_p_h2o)
r_lhhw = lhhw_model(test_data)
r_power = power_model(test_data, fit_params)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

test_data["T"] = test_data["T"].reshape(n_p_meoh, n_temp)
test_data["p_meoh"] = test_data["p_meoh"].reshape(n_p_meoh, n_temp)
r_lhhw = r_lhhw.reshape(n_p_meoh, n_temp)
r_power = r_power.reshape(n_p_meoh, n_temp)
ax.plot_surface(test_data["T"], test_data["p_meoh"], r_lhhw)
ax.plot_surface(test_data["T"], test_data["p_meoh"], r_power)
plt.show()
