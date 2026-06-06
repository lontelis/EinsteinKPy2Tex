"""
txyzS_EinsteinKPy2Tex: Entropy as Extra Dimension Metric Calculator
=====================================================================
Author: P. Ntelis
Code date: 6 June 2026
Version: 1.0
GitHub: https://github.com/lontelis/EinsteinKPy2Tex

CITATION INFORMATION
====================
If you use this code in your research, please cite:

1. The Einstein paper (original theory)
2. The EinsteinPy library (Ribeiro et al. 2020)
3. Advanced Manifold-Metric Pairs (Ntelis 2025)
4. This software (txyzS_EinsteinKPy2Tex)
"""

import sympy as sp
import numpy as np
import argparse
from einsteinpy.symbolic import (
    MetricTensor,
    ChristoffelSymbols,
    RiemannCurvatureTensor,
    RicciTensor,
    RicciScalar,
    EinsteinTensor,
)

__version__ = "1.0.0"
__author__ = "P. Ntelis"
__date__ = "6 June 2026"
__github_repo__ = "https://github.com/lontelis/EinsteinKPy2Tex"

def print_citation():
    citation = """
    ============================================================================
    txyzS_EinsteinKPy2Tex v1.0
    Author: P. Ntelis
    Date: 6 June 2026
    ============================================================================
    If you use this code in your research, please cite:
    
    [1] Einstein, A. (1915). Die Feldgleichungen der Gravitation.
    [2] Ribeiro, S., et al. (2020). EinsteinPy. JOSS, 5(51), 2356.
    [3] Ntelis, P. (2025). Advanced Manifold-Metric Pairs. Mathematics, 13(15), 2510.
    [4] P. Ntelis (2026). txyzS_EinsteinKPy2Tex. GitHub.
    ============================================================================
    """
    print(citation)

def generate_bib_file():
    bib_content = """% BibTeX citations for txyzS_EinsteinKPy2Tex

@article{Einstein1915,
    title = {Die Feldgleichungen der Gravitation},
    author = {Einstein, Albert},
    journal = {Sitzungsberichte der K{\"o}niglich Preu{\ss}ischen Akademie der Wissenschaften},
    pages = {844--847},
    year = {1915}
}

@article{EinsteinPy2020,
    title = {EinsteinPy: A Python Package for General Relativity},
    author = {Ribeiro, Shreyas and others},
    journal = {Journal of Open Source Software},
    volume = {5},
    number = {51},
    pages = {2356},
    year = {2020},
    doi = {10.21105/joss.02356}
}

@article{Ntelis2025_AMMP,
    author = {Ntelis, P.},
    title = {Advanced Manifold--Metric Pairs},
    journal = {Mathematics},
    volume = {13},
    number = {15},
    pages = {2510},
    year = {2025},
    doi = {10.3390/math13152510}
}

@software{txyzS_EinsteinKPy2Tex2026,
    author = {P. Ntelis},
    title = {txyzS_EinsteinKPy2Tex: Entropy as Extra Dimension Metric Calculator},
    year = {2026},
    url = {https://github.com/lontelis/EinsteinKPy2Tex},
    version = {1.0}
}
"""
    with open("citations_txyzS.bib", "w") as f:
        f.write(bib_content)
    print("✓ BibTeX citation file 'citations_txyzS.bib' generated!")

# Parse arguments
parser = argparse.ArgumentParser(description='txyzS Entropy Extra-Dimensional Metric Calculator')
parser.add_argument('--cite', action='store_true', help='Display citation information')
parser.add_argument('--generate_bib', action='store_true', help='Generate BibTeX citation file')
parser.add_argument('--version', action='store_true', help='Show version information')
args = parser.parse_args()

if args.version:
    print(f"txyzS_EinsteinKPy2Tex version {__version__}")
    print(f"Author: {__author__}")
    print(f"Date: {__date__}")
    exit()

if args.cite:
    print_citation()
    exit()

if args.generate_bib:
    generate_bib_file()
    exit()

# ============================================================================
# 1. Define coordinates for 4D spacetime (t, x, y, z, S)
# ============================================================================
# 4 spatial? No: t (time) + x,y,z (space) + S (entropy) = 5D total
t, x, y, z, S = sp.symbols("t x y z S")
coords = [t, x, y, z, S]
coord_names = ['t', 'x', 'y', 'z', 'S']

print("\n" + "="*60)
print("txyzS_EinsteinKPy2Tex: Entropy as Extra Dimension")
print("="*60)
print(f"\nCoordinates: {coord_names}")
print("Interpretation:")
print("  - t: Time (conventional)")
print("  - x, y, z: Spatial dimensions (3D)")
print("  - S: Entropy (extra dimension)")
print("\nTotal dimensions: 5D")

# Metric functions
c = sp.Symbol("c", positive=True, real=True)
a = sp.Function("a")(t)           # spatial scale factor
f_S = sp.Function("f_S")(t, S)    # entropy dimension scale factor

print("\n✓ Metric functions defined:")
print("   - a(t): spatial scale factor")
print("   - f_S(t,S): entropy dimension scale factor")

# ============================================================================
# 2. Construct the 5D Metric (t, x, y, z, S)
# ============================================================================
# Signature: (-, +, +, +, +)  (one timelike, four spacelike)
metric_arr = [
    [-c**2, 0, 0, 0, 0],
    [0, a**2, 0, 0, 0],
    [0, 0, a**2, 0, 0],
    [0, 0, 0, a**2, 0],
    [0, 0, 0, 0, f_S**2],
]

metric = MetricTensor(metric_arr, coords, "ll", name="txyzS_Metric")

print("\n✓ Metric tensor defined:")
print("   ds² = -c² dt² + a(t)² (dx²+dy²+dz²) + f_S(t,S)² dS²")

# ============================================================================
# 3. Compute tensors
# ============================================================================
print("\nComputing tensors...")

ch = ChristoffelSymbols.from_metric(metric)
print("  ✓ Christoffel symbols")

riem = RiemannCurvatureTensor.from_metric(metric)
print("  ✓ Riemann tensor")

ric = RicciTensor.from_metric(metric)
print("  ✓ Ricci tensor")

rsc = RicciScalar.from_metric(metric)
print("  ✓ Ricci scalar")

ein = EinsteinTensor.from_metric(metric)
print("  ✓ Einstein tensor")

# ============================================================================
# 4. Geodesic equations
# ============================================================================
def compute_geodesic_equations(christoffel, coords):
    D = len(coords)
    velocities = [sp.Symbol(f"\\dot{{{coord}}}") for coord in ['t', 'x', 'y', 'z', 'S']]
    christoffel_arr = christoffel.tensor()
    
    geodesic_eqs = []
    for mu in range(D):
        eq = 0
        for nu in range(D):
            for rho in range(D):
                gamma = sp.simplify(christoffel_arr[mu, nu, rho])
                if gamma != 0:
                    eq += gamma * velocities[nu] * velocities[rho]
        geodesic_eqs.append(sp.Eq(sp.Symbol(f"\\ddot{{{coord_names[mu]}}}"), -eq))
    return geodesic_eqs

geodesic_eqs = compute_geodesic_equations(ch, coords)
print("  ✓ Geodesic equations")

# ============================================================================
# 5. Kretschmann scalar
# ============================================================================
def compute_kretschmann_scalar(riemann, metric, coords):
    D = len(coords)
    R_mixed = riemann.tensor()
    g_matrix = sp.Matrix(metric.tensor())
    g_inv = g_matrix.inv()
    
    # Lower first index
    R_cov = [[[[0 for _ in range(D)] for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for mu in range(D):
        for nu in range(D):
            for rho in range(D):
                for sigma in range(D):
                    total = 0
                    for alpha in range(D):
                        total += g_matrix[mu, alpha] * R_mixed[alpha, nu, rho, sigma]
                    R_cov[mu][nu][rho][sigma] = total
    
    # Raise all indices
    R_con = [[[[0 for _ in range(D)] for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for alpha in range(D):
        for beta in range(D):
            for gamma in range(D):
                for delta in range(D):
                    total = 0
                    for mu in range(D):
                        for nu in range(D):
                            for rho in range(D):
                                for sigma in range(D):
                                    total += (g_inv[alpha, mu] * g_inv[beta, nu] * 
                                              g_inv[gamma, rho] * g_inv[delta, sigma] * 
                                              R_cov[mu][nu][rho][sigma])
                    R_con[alpha][beta][gamma][delta] = total
    
    # Contract
    K = 0
    for alpha in range(D):
        for beta in range(D):
            for gamma in range(D):
                for delta in range(D):
                    K += R_con[alpha][beta][gamma][delta] * R_cov[alpha][beta][gamma][delta]
    
    return K, sp.simplify(K)

K_full, K_simple = compute_kretschmann_scalar(riem, metric, coords)
print("  ✓ Kretschmann scalar")

# ============================================================================
# 6. LaTeX output helpers
# ============================================================================
def latex_nonzero(tensor_obj, tensor_symbol, rank):
    arr = tensor_obj.tensor()
    non_zero = []
    D = np.size(coords)
    
    if rank == 2:
        for i in range(D):
            for j in range(D):
                val = sp.simplify(arr[i, j])
                if val != 0:
                    label = f"{coord_names[i]}{coord_names[j]}"
                    non_zero.append(f"{tensor_symbol}_{{{label}}} &= {sp.latex(val)} \\\\")
    elif rank == 3:
        for i in range(D):
            for j in range(D):
                for k in range(D):
                    val = sp.simplify(arr[i, j, k])
                    if val != 0:
                        upper = coord_names[i]
                        lower_j = coord_names[j]
                        lower_k = coord_names[k]
                        label = f"{{{upper}}}_{{{lower_j} {lower_k}}}"
                        non_zero.append(f"{tensor_symbol}^{label} &= {sp.latex(val)} \\\\")
    elif rank == 4:
        for i in range(D):
            for j in range(D):
                for k in range(D):
                    for l in range(D):
                        val = sp.simplify(arr[i, j, k, l])
                        if val != 0:
                            upper = coord_names[i]
                            lower_j = coord_names[j]
                            lower_k = coord_names[k]
                            lower_l = coord_names[l]
                            label = f"{{{upper}}}_{{{lower_j} {lower_k} {lower_l}}}"
                            non_zero.append(f"{tensor_symbol}^{label} &= {sp.latex(val)} \\\\")
    return "\n".join(non_zero) if non_zero else "All components zero."

def latex_geodesic_equations(eqs):
    lines = []
    for eq in eqs:
        lines.append(sp.latex(eq) + " \\\\")
    return "\n".join(lines)

# ============================================================================
# 7. Write LaTeX file
# ============================================================================
filename = "txyzS_EinsteinKPy2Tex.tex"
with open(filename, "w") as f:
    f.write("\\documentclass{article}\n")
    f.write("\\usepackage{amsmath,amssymb}\n")
    f.write("\\begin{document}\n\n")
    
    f.write("% Generated by txyzS_EinsteinKPy2Tex v1.0\n")
    f.write("% Author: P. Ntelis, Date: 6 June 2026\n")
    f.write("% GitHub: https://github.com/lontelis/EinsteinKPy2Tex\n\n")
    
    f.write("\\title{Geometric Quantities for the txyzS Metric: Entropy as Extra Dimension}\n")
    f.write("\\author{Generated by txyzS\\_EinsteinKPy2Tex}\n")
    f.write("\\date{\\today}\n")
    f.write("\\maketitle\n\n")
    
    f.write("\\section{The txyzS Metric Ansatz}\n\n")
    f.write("The metric with entropy as an extra dimension is given by\n")
    f.write("\\begin{align}\n")
    f.write("ds^2 = -c^2 dt^2 + a(t)^2 (dx^2+dy^2+dz^2) + f_S(t,S)^2 dS^2\n")
    f.write("\\end{align}\n\n")
    f.write("where:\n")
    f.write("\\begin{itemize}\n")
    f.write("    \\item $t$ is time (conventional dimension)\n")
    f.write("    \\item $x, y, z$ are spatial dimensions\n")
    f.write("    \\item $S$ is entropy (extra thermodynamic dimension)\n")
    f.write("    \\item $a(t)$ is the cosmological scale factor\n")
    f.write("    \\item $f_S(t,S)$ is the entropy dimension scale factor\n")
    f.write("\\end{itemize}\n\n")
    
    f.write("\\subsection{Metric tensor $g_{\\mu\\nu}$}\n")
    f.write("\\begin{align}\n")
    f.write(sp.latex(metric.tensor()))
    f.write("\n\\end{align}\n\n")
    
    f.write("\\subsection{Christoffel symbols $\\Gamma^{\\mu}_{\\nu\\rho}$ (non-zero)}\n")
    f.write("\\begin{align}\n")
    f.write(latex_nonzero(ch, r"\Gamma", 3))
    f.write("\n\\end{align}\n\n")
    
    f.write("\\subsection{Riemann tensor $R^{\\mu}_{\\ \\nu\\rho\\sigma}$ (non-zero)}\n")
    f.write("\\begin{align}\n")
    f.write(latex_nonzero(riem, "R", 4))
    f.write("\n\\end{align}\n\n")
    
    f.write("\\subsection{Ricci tensor $R_{\\mu\\nu}$ (non-zero)}\n")
    f.write("\\begin{align}\n")
    f.write(latex_nonzero(ric, "R", 2))
    f.write("\n\\end{align}\n\n")
    
    f.write("\\subsection{Ricci scalar $R$}\n")
    f.write("\\begin{align}\n")
    f.write(sp.latex(rsc.expr))
    f.write("\n\\end{align}\n\n")
    
    f.write("\\subsection{Einstein tensor $G_{\\mu\\nu}$ (non-zero)}\n")
    f.write("\\begin{align}\n")
    f.write(latex_nonzero(ein, "G", 2))
    f.write("\n\\end{align}\n\n")
    
    f.write("\\subsection{Geodesic equations}\n")
    f.write("\\begin{align}\n")
    f.write(latex_geodesic_equations(geodesic_eqs))
    f.write("\n\\end{align}\n\n")
    
    f.write("\\subsection{Kretschmann scalar}\n")
    f.write("The Kretschmann scalar $K = R^{\\mu\\nu\\rho\\sigma} R_{\\mu\\nu\\rho\\sigma}$:\n\n")
    f.write("\\subsubsection*{Full expression}\n")
    f.write("\\begin{align}\n")
    f.write(sp.latex(K_full))
    f.write("\n\\end{align}\n\n")
    f.write("\\subsubsection*{Simplified expression}\n")
    f.write("\\begin{align}\n")
    f.write(sp.latex(K_simple))
    f.write("\n\\end{align}\n\n")
    
    f.write("\\end{document}\n")

print(f"\n✓ LaTeX output written to {filename}")
print(f"\nGitHub: {__github_repo__}")