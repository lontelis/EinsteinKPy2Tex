"""
EinsteinKPy2Tex_simulations_flrw_txyzS.py
==========================================
Author: P. Ntelis
Date: 6 June 2026

Corrected version - fixed contourf dimension mismatch error.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Set publication-quality plot parameters
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',
    'mathtext.fontset': 'stix',
    'axes.labelsize': 14,
    'axes.titlesize': 14,
    'legend.fontsize': 10,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

c = 1.0  # natural units

# ============================================================================
# Scale factor functions
# ============================================================================

def scale_factor_matter_dominated(t):
    a = t**(2/3)
    a_dot = (2/3) * t**(-1/3)
    a_ddot = (-2/9) * t**(-4/3)
    return a, a_dot, a_ddot

def scale_factor_radiation_dominated(t):
    a = t**(1/2)
    a_dot = (1/2) * t**(-1/2)
    a_ddot = (-1/4) * t**(-3/2)
    return a, a_dot, a_ddot

def scale_factor_lambda_dominated(t, H0=1.0):
    a = np.exp(H0 * t)
    a_dot = H0 * np.exp(H0 * t)
    a_ddot = H0**2 * np.exp(H0 * t)
    return a, a_dot, a_ddot

def entropy_factor_exponential(t, S, beta=0.5):
    return np.exp(beta * t * S)

# ============================================================================
# Kretschmann scalar functions
# ============================================================================

def kretschmann_flrw(a, a_dot, a_ddot, c=1.0):
    term1 = (a_ddot / a)**2
    term2 = (a_dot / a)**4
    return 12 * (term1 + term2) / c**4

def kretschmann_txyzS(a, a_dot, a_ddot, f_S, f_S_dot, f_S_ddot, c=1.0):
    term1 = 4 * (f_S_ddot / f_S)**2
    term2 = 12 * (a_ddot / a)**2
    term3 = 12 * (a_dot / a)**2 * (f_S_dot / f_S)**2
    term4 = 12 * (a_dot / a)**4
    return (term1 + term2 + term3 + term4) / c**4

# ============================================================================
# Simulation
# ============================================================================

print("="*70)
print("txyzS Kretschmann Scalar Simulation")
print("="*70)

t = np.logspace(np.log10(0.01), np.log10(10), 500)
S_values = [0.0, 0.5, 1.0, 2.0]
colors_S = ['black', 'blue', 'green', 'red']

# Compute FLRW
a_mat, a_dot_mat, a_ddot_mat = scale_factor_matter_dominated(t)
K_flrw_mat = kretschmann_flrw(a_mat, a_dot_mat, a_ddot_mat, c)

a_rad, a_dot_rad, a_ddot_rad = scale_factor_radiation_dominated(t)
K_flrw_rad = kretschmann_flrw(a_rad, a_dot_rad, a_ddot_rad, c)

a_lambda, a_dot_lambda, a_ddot_lambda = scale_factor_lambda_dominated(t)
K_flrw_lambda = kretschmann_flrw(a_lambda, a_dot_lambda, a_ddot_lambda, c)

print("✓ FLRW simulations complete")

# Compute txyzS
results_txyzS = {}
for S in S_values:
    f_S = entropy_factor_exponential(t, S, beta=0.5)
    f_S_dot = 0.5 * S * f_S
    f_S_ddot = (0.5 * S)**2 * f_S
    
    K_mat = kretschmann_txyzS(a_mat, a_dot_mat, a_ddot_mat, f_S, f_S_dot, f_S_ddot, c)
    K_rad = kretschmann_txyzS(a_rad, a_dot_rad, a_ddot_rad, f_S, f_S_dot, f_S_ddot, c)
    K_lambda = kretschmann_txyzS(a_lambda, a_dot_lambda, a_ddot_lambda, f_S, f_S_dot, f_S_ddot, c)
    
    results_txyzS[S] = {'matter': K_mat, 'radiation': K_rad, 'lambda': K_lambda}
    print(f"✓ S = {S} complete")

# ============================================================================
# Plot 1: FLRW
# ============================================================================
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.loglog(t, K_flrw_rad, 'r-', linewidth=2, label='Radiation-dominated')
ax1.loglog(t, K_flrw_mat, 'b-', linewidth=2, label='Matter-dominated')
ax1.loglog(t, K_flrw_lambda, 'g-', linewidth=2, label='$\\Lambda$-dominated')
ax1.set_xlabel('Cosmic time $t$')
ax1.set_ylabel('Kretschmann scalar $K$')
ax1.set_title('FLRW: Kretschmann Scalar')
ax1.legend()
ax1.grid(True, alpha=0.3, which='both')
ax1.set_xlim(0.01, 10)
plt.tight_layout()
plt.savefig('fig1_flrw_kretschmann.pdf', dpi=300)
print("✓ Saved: fig1_flrw_kretschmann.pdf")

# ============================================================================
# Plot 2: txyzS vs FLRW (matter-dominated)
# ============================================================================
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.loglog(t, K_flrw_mat, 'k-', linewidth=3, label='FLRW')
for S, color in zip(S_values[1:], colors_S[1:]):
    ax2.loglog(t, results_txyzS[S]['matter'], color=color, linewidth=2, linestyle='--', label=f'txyzS, S = {S}')
ax2.set_xlabel('Cosmic time $t$')
ax2.set_ylabel('Kretschmann scalar $K$')
ax2.set_title('Matter-Dominated: FLRW vs txyzS')
ax2.legend()
ax2.grid(True, alpha=0.3, which='both')
ax2.set_xlim(0.01, 10)
plt.tight_layout()
plt.savefig('fig2_txyzS_vs_flrw_matter.pdf', dpi=300)
print("✓ Saved: fig2_txyzS_vs_flrw_matter.pdf")

# ============================================================================
# Plot 3: Ratio comparison
# ============================================================================
fig4, ax4 = plt.subplots(figsize=(10, 6))
for S, color in zip(S_values[1:], colors_S[1:]):
    ratio = results_txyzS[S]['matter'] / K_flrw_mat
    ax4.semilogx(t, ratio, color=color, linewidth=2, label=f'S = {S}')
ax4.axhline(y=1.0, color='k', linestyle=':', linewidth=1, alpha=0.5)
ax4.set_xlabel('Cosmic time $t$')
ax4.set_ylabel('$K_{txyzS} / K_{FLRW}$')
ax4.set_title('Ratio: txyzS / FLRW (Matter-Dominated)')
ax4.legend()
ax4.grid(True, alpha=0.3)
ax4.set_xlim(0.01, 10)
ax4.set_ylim(0.5, 5)
plt.tight_layout()
plt.savefig('fig4_ratio_comparison.pdf', dpi=300)
print("✓ Saved: fig4_ratio_comparison.pdf")

# ============================================================================
# Plot 4: Parameter scan (FIXED)
# ============================================================================
fig5, ax5 = plt.subplots(figsize=(10, 6))

S_scan = np.linspace(0, 2, 50)
t_scan = np.logspace(np.log10(0.05), np.log10(5), 50)
T_mesh, S_mesh = np.meshgrid(t_scan, S_scan)

ratio_scan = np.zeros_like(T_mesh)

# Pre-compute FLRW values
K_flrw_scan = np.zeros_like(t_scan)
for j, t_val in enumerate(t_scan):
    a, a_dot, a_ddot = scale_factor_matter_dominated(np.array([t_val]))
    K_flrw_scan[j] = kretschmann_flrw(a, a_dot, a_ddot, c)[0]

# Compute txyzS values
for i, S_val in enumerate(S_scan):
    for j, t_val in enumerate(t_scan):
        a, a_dot, a_ddot = scale_factor_matter_dominated(np.array([t_val]))
        f_S = entropy_factor_exponential(np.array([t_val]), S_val, beta=0.5)[0]
        f_S_dot = 0.5 * S_val * f_S
        f_S_ddot = (0.5 * S_val)**2 * f_S
        K_txyzS_val = kretschmann_txyzS(a, a_dot, a_ddot, 
                                         np.array([f_S]), np.array([f_S_dot]), 
                                         np.array([f_S_ddot]), c)[0]
        ratio_scan[i, j] = K_txyzS_val / K_flrw_scan[j]

im = ax5.contourf(T_mesh, S_mesh, ratio_scan, levels=20, cmap='RdYlBu_r')
ax5.set_xscale('log')
ax5.set_xlabel('Cosmic time $t$')
ax5.set_ylabel('Entropy coordinate $S$')
ax5.set_title('Parameter Scan: $K_{txyzS} / K_{FLRW}$')
cbar = plt.colorbar(im, ax=ax5)
cbar.set_label('Ratio $K_{txyzS}/K_{FLRW}$')
ax5.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('fig5_parameter_scan.pdf', dpi=300)
print("✓ Saved: fig5_parameter_scan.pdf")

# ============================================================================
# Plot 5: Early universe zoom
# ============================================================================
fig6, ax6 = plt.subplots(figsize=(10, 6))
t_early = t[t < 0.5]
K_flrw_mat_early = K_flrw_mat[t < 0.5]

ax6.plot(t_early, K_flrw_mat_early, 'k-', linewidth=3, label='FLRW')
for S, color in zip(S_values[1:], colors_S[1:]):
    K_txyzS_early = results_txyzS[S]['matter'][t < 0.5]
    ax6.plot(t_early, K_txyzS_early, color=color, linewidth=2, linestyle='--', label=f'txyzS, S = {S}')

ax6.set_xlabel('Cosmic time $t$ (early universe)')
ax6.set_ylabel('Kretschmann scalar $K$')
ax6.set_title('Early Universe: FLRW vs txyzS (Matter-Dominated)')
ax6.set_yscale('log')
ax6.legend()
ax6.grid(True, alpha=0.3)
ax6.set_xlim(0, 0.5)

plt.tight_layout()
plt.savefig('fig6_early_universe.pdf', dpi=300)
print("✓ Saved: fig6_early_universe.pdf")

print("\n" + "="*70)
print("SIMULATION COMPLETE!")
print("Generated: fig1, fig2, fig4, fig5, fig6")
print("="*70)