"""
EinsteinKPy2Tex: Kretschmann Scalar Visualization
==================================================
Author: P. Ntelis
Date: 5 June 2026

Generates publication-quality plots of the Kretschmann scalar for:
- Schwarzschild metric with different masses
- FLRW metric with different scale factors (radiation, matter, Lambda domination)
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
    'savefig.pad_inches': 0.05
})

# Constants (in natural units where G = c = 1 for simplicity)
G = 1.0
c = 1.0

# ============================================================================
# Part 1: Schwarzschild Metric - Kretschmann Scalar K(r) = 12 R_s^2 / r^6
# ============================================================================

def schwarzschild_kretschmann(r, M):
    """
    Compute Kretschmann scalar for Schwarzschild metric.
    
    Parameters:
    r : array_like - Radial coordinate
    M : float - Black hole mass
    
    Returns:
    K : array_like - Kretschmann scalar
    """
    R_s = 2 * G * M / c**2  # Schwarzschild radius
    return 12 * R_s**2 / r**6

def plot_schwarzschild():
    """Plot Kretschmann scalar for different black hole masses"""
    
    # Masses to simulate (in solar masses, with G=c=1)
    masses = [0.5, 1.0, 2.0, 5.0]
    colors = ['blue', 'green', 'red', 'purple']
    line_styles = ['-', '--', '-.', ':']
    
    # Radial range: from just outside horizon to large distances
    r_min = 2.1  # Slightly outside r=2M for M=1
    r_max = 20.0
    r = np.linspace(r_min, r_max, 500)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Linear scale (focus on large r behavior)
    ax1 = axes[0]
    for M, color, ls in zip(masses, colors, line_styles):
        K = schwarzschild_kretschmann(r, M)
        R_s = 2 * M  # in natural units
        ax1.plot(r, K, color=color, linestyle=ls, linewidth=2, 
                label=f'M = {M} M$_\odot$, R$_s$ = {R_s:.1f}')
    
    ax1.set_xlabel('Radial coordinate r', fontsize=12)
    ax1.set_ylabel('Kretschmann scalar K(r)', fontsize=12)
    ax1.set_title('Schwarzschild: K(r) - Linear Scale', fontsize=14)
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 10)
    ax1.set_xlim(2, 20)
    
    # Plot 2: Log-log scale (show power law behavior)
    ax2 = axes[1]
    for M, color, ls in zip(masses, colors, line_styles):
        K = schwarzschild_kretschmann(r, M)
        ax2.loglog(r, K, color=color, linestyle=ls, linewidth=2,
                  label=f'M = {M} M$_\odot$')
    
    # Add reference line for r^{-6} scaling
    r_ref = np.logspace(np.log10(2.5), np.log10(20), 100)
    K_ref = 12 * (2*1)**2 / r_ref**6  # Reference for M=1
    ax2.loglog(r_ref, K_ref, 'k--', linewidth=1.5, alpha=0.5, 
              label='$r^{-6}$ scaling (reference)')
    
    ax2.set_xlabel('Radial coordinate r', fontsize=12)
    ax2.set_ylabel('Kretschmann scalar K(r)', fontsize=12)
    ax2.set_title('Schwarzschild: K(r) - Log Scale (Power Law)', fontsize=14)
    ax2.legend(loc='upper right')
    ax2.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    plt.savefig('schwarzschild_kretschmann.pdf', dpi=300, bbox_inches='tight')
    print("✓ Saved: schwarzschild_kretschmann.pdf")
    
    return fig

# ============================================================================
# Part 2: FLRW Metric - Kretschmann Scalar 
# K(t) = 12 (a² ä² + ȧ⁴) / (c⁴ a⁴)
# ============================================================================

def flrw_kretschmann(a, a_dot, a_ddot, c=1.0):
    """
    Compute Kretschmann scalar for FLRW metric.
    
    Parameters:
    a : array_like - Scale factor
    a_dot : array_like - First derivative of scale factor
    a_ddot : array_like - Second derivative of scale factor
    c : float - Speed of light (default 1 in natural units)
    
    Returns:
    K : array_like - Kretschmann scalar
    """
    return 12 * (a**2 * a_ddot**2 + a_dot**4) / (c**4 * a**4)

# Scale factor functions and their derivatives
def radiation_dominated(t, t0=1.0):
    """Radiation-dominated era: a(t) ∝ t^{1/2}"""
    a = np.sqrt(t / t0)
    a_dot = 0.5 / np.sqrt(t * t0)
    a_ddot = -0.25 / (t0 * t**(3/2))
    return a, a_dot, a_ddot

def matter_dominated(t, t0=1.0):
    """Matter-dominated era: a(t) ∝ t^{2/3}"""
    a = (t / t0)**(2/3)
    a_dot = (2/3) * t0**(-2/3) * t**(-1/3)
    a_ddot = (-2/9) * t0**(-2/3) * t**(-4/3)
    return a, a_dot, a_ddot

def lambda_dominated(t, H0=1.0, t0=1.0):
    """Lambda-dominated (de Sitter): a(t) ∝ e^{Ht}"""
    a = np.exp(H0 * (t - t0))
    a_dot = H0 * np.exp(H0 * (t - t0))
    a_ddot = H0**2 * np.exp(H0 * (t - t0))
    return a, a_dot, a_ddot

def plot_flrw():
    """Plot Kretschmann scalar for different cosmological eras"""
    
    # Time range: from early universe to present
    t = np.logspace(np.log10(0.05), np.log10(10), 500)  # log-spaced for better visualization
    
    # Compute Kretschmann for each era
    a_rad, adot_rad, addot_rad = radiation_dominated(t)
    K_rad = flrw_kretschmann(a_rad, adot_rad, addot_rad)
    
    a_mat, adot_mat, addot_mat = matter_dominated(t)
    K_mat = flrw_kretschmann(a_mat, adot_mat, addot_mat)
    
    a_lambda, adot_lambda, addot_lambda = lambda_dominated(t)
    K_lambda = flrw_kretschmann(a_lambda, adot_lambda, addot_lambda)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Linear scale (early times)
    ax1 = axes[0]
    t_early = t[t < 2.0]
    K_rad_early = K_rad[t < 2.0]
    K_mat_early = K_mat[t < 2.0]
    K_lambda_early = K_lambda[t < 2.0]
    
    ax1.plot(t_early, K_rad_early, 'r-', linewidth=2, label='Radiation-dominated ($a\\propto t^{1/2}$)')
    ax1.plot(t_early, K_mat_early, 'b-', linewidth=2, label='Matter-dominated ($a\\propto t^{2/3}$)')
    ax1.plot(t_early, K_lambda_early, 'g-', linewidth=2, label='$\\Lambda$-dominated ($a\\propto e^{Ht}$)')
    
    ax1.set_xlabel('Cosmic time t', fontsize=12)
    ax1.set_ylabel('Kretschmann scalar K(t)', fontsize=12)
    ax1.set_title('FLRW: Kretschmann Scalar (Early Universe)', fontsize=14)
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 50)
    ax1.set_xlim(0, 2)
    
    # Plot 2: Log-log scale (full range, show power laws)
    ax2 = axes[1]
    ax2.loglog(t, K_rad, 'r-', linewidth=2, label='Radiation-dominated ($K\\propto t^{-4}$)')
    ax2.loglog(t, K_mat, 'b-', linewidth=2, label='Matter-dominated ($K\\propto t^{-4}$)')
    ax2.loglog(t, K_lambda, 'g-', linewidth=2, label='$\\Lambda$-dominated ($K\\propto e^{-4Ht}$)')
    
    # Add reference lines for power laws
    t_ref = np.logspace(-1, 1, 100)
    K_ref_rad = 10 * t_ref**(-4)    # t^{-4} scaling
    K_ref_mat = 5 * t_ref**(-4)      # t^{-4} scaling
    
    ax2.loglog(t_ref, K_ref_rad, 'r--', linewidth=1, alpha=0.5, label='$t^{-6}$ scaling')
    ax2.loglog(t_ref, K_ref_mat, 'b--', linewidth=1, alpha=0.5, label='$t^{-4}$ scaling')
    
    ax2.set_xlabel('Cosmic time t', fontsize=12)
    ax2.set_ylabel('Kretschmann scalar K(t)', fontsize=12)
    ax2.set_title('FLRW: Kretschmann Scalar (Log-Log Scale)', fontsize=14)
    ax2.legend(loc='upper right', fontsize=8)
    ax2.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    plt.savefig('flrw_kretschmann.pdf', dpi=300, bbox_inches='tight')
    print("✓ Saved: flrw_kretschmann.pdf")
    
    return fig

# ============================================================================
# Part 3: Combined Comparison Plot (Singularity Behavior)
# ============================================================================

def plot_combined_comparison():
    """Combined plot showing singularity behavior for both metrics"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Schwarzschild (physical singularity at r=0)
    r = np.linspace(0.5, 10, 500)
    masses = [0.5, 1.0, 2.0]
    colors = ['blue', 'green', 'red']
    
    for M, color in zip(masses, colors):
        R_s = 2 * M
        K = 12 * R_s**2 / r**6
        ax1.plot(r, K, color=color, linewidth=2, label=f'M = {M} M$_\\odot$, R$_s$ = {R_s}')
    
    ax1.set_yscale('log')
    ax1.set_xlabel('Radial coordinate r', fontsize=12)
    ax1.set_ylabel('Kretschmann scalar K(r)', fontsize=12)
    ax1.set_title('Schwarzschild: Physical Singularity at $r=0$', fontsize=12)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.grid(True, alpha=0.3, which='both')
    ax1.set_xlim(0.5, 10)
    
    # FLRW (big bang singularity at t=0)
    t = np.linspace(0.2, 5, 500)
    
    # Radiation-dominated
    a_rad, adot_rad, addot_rad = radiation_dominated(t)
    K_rad = flrw_kretschmann(a_rad, adot_rad, addot_rad)
    ax2.plot(t, K_rad, 'r-', linewidth=2, label='Radiation-dominated')
    
    # Matter-dominated
    a_mat, adot_mat, addot_mat = matter_dominated(t)
    K_mat = flrw_kretschmann(a_mat, adot_mat, addot_mat)
    ax2.plot(t, K_mat, 'b-', linewidth=2, label='Matter-dominated')
    
    ax2.set_yscale('log')
    ax2.set_xlabel('Cosmic time t', fontsize=12)
    ax2.set_ylabel('Kretschmann scalar K(t)', fontsize=12)
    ax2.set_title('FLRW: Big Bang Singularity at $t=0$', fontsize=12)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.grid(True, alpha=0.3, which='both')
    ax2.set_xlim(0.2, 5)
    
    plt.tight_layout()
    plt.savefig('kretschmann_singularities.pdf', dpi=300, bbox_inches='tight')
    print("✓ Saved: kretschmann_singularities.pdf")
    
    return fig

# ============================================================================
# Part 4: 3D Surface Plot (Mass vs Radius)
# ============================================================================

def plot_3d_schwarzschild():
    """3D surface plot showing Kretschmann scalar as function of r and M"""
    
    from mpl_toolkits.mplot3d import Axes3D
    
    # Create meshgrid
    r = np.linspace(2.1, 10, 100)
    M = np.linspace(0.5, 5, 80)
    R, M_grid = np.meshgrid(r, M)
    
    # Compute Kretschmann
    R_s = 2 * M_grid
    K = 12 * R_s**2 / R**6
    
    # Remove very large values for better visualization
    K = np.clip(K, 0, 50)
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(R, M_grid, K, cmap='viridis', alpha=0.9, 
                           linewidth=0, antialiased=True)
    
    ax.set_xlabel('Radial coordinate r', fontsize=12)
    ax.set_ylabel('Black hole mass M', fontsize=12)
    ax.set_zlabel('Kretschmann scalar K(r,M)', fontsize=12)
    ax.set_title('Schwarzschild: Kretschmann Scalar Dependence on r and M', fontsize=14)
    
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='K(r,M)')
    
    plt.tight_layout()
    plt.savefig('schwarzschild_3d.pdf', dpi=300, bbox_inches='tight')
    print("✓ Saved: schwarzschild_3d.pdf")
    
    return fig

# ============================================================================
# Main Execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("EinsteinKPy2Tex: Kretschmann Scalar Visualization")
    print("Generating publication-quality plots...")
    print("="*60 + "\n")
    
    # Generate all plots
    plot_schwarzschild()
    plot_flrw()
    plot_combined_comparison()
    plot_3d_schwarzschild()
    
    print("\n" + "="*60)
    print("✓ All plots generated successfully!")
    print("Output files:")
    print("  - schwarzschild_kretschmann.pdf")
    print("  - flrw_kretschmann.pdf")
    print("  - kretschmann_singularities.pdf")
    print("  - schwarzschild_3d.pdf")
    print("="*60 + "\n")