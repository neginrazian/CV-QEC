"""
utils.py — Shared functions for CV-QEC numerical simulations
Razian, Chang, Lau — SFU Physics
"""

import numpy as np

# ── Displacement distribution ─────────────────────────
def G(x, sigma):
    """Gaussian distribution as defined in the paper.
    G(x, sigma) = exp(-x^2/sigma^2) / (sqrt(pi) * sigma)
    """
    return np.exp(-x**2 / sigma**2) / (np.sqrt(np.pi) * sigma)

def P_2d(beta_q, beta_p, sigma):
    """2D displacement distribution."""
    return G(beta_q, sigma) * G(beta_p, sigma)

# ── Filter function ───────────────────────────────────
def filtered_distribution(beta_p, sigma, alpha, sign=+1):
    """Modified displacement distribution after qubit measurement."""
    return G(beta_p, sigma) * (1 + sign * np.sin(4 * alpha * beta_p))

def beta_mean(sigma, alpha, sign=+1):
    """Mean of the corrected distribution."""
    return sign * 2 * alpha * sigma**2 * np.exp(-4 * alpha**2 * sigma**2)

# ── Optimal parameters ────────────────────────────────
def alpha_opt(sigma):
    """Optimal conditional displacement strength."""
    return 1 / (np.sqrt(8) * sigma)

def zeta_opt():
    """Optimal squeezing parameter."""
    return (1/8) * np.log(1 - np.exp(-1))

# ── State overlap functions ───────────────────────────
def f_coherent(beta_q, beta_p):
    """Overlap function for coherent state."""
    return np.exp(-(beta_q**2 + beta_p**2))

def f_single_boson(beta_q, beta_p):
    """Overlap function for single-boson state |1>."""
    beta_sq = beta_q**2 + beta_p**2
    return np.exp(-beta_sq) * (1 - beta_sq)**2