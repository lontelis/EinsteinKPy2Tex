r"""
Schwarzschild Metric Tensor Calculator with Weyl Tensor
========================================================
Author: P. Ntelis
Version: 2.0
Date: 2026-06-11
GitHub: https://github.com/lontelis/EinsteinKPy2Tex

Now computes:
- Christoffel symbols
- Riemann curvature tensor
- Ricci tensor and scalar
- Einstein tensor
- Geodesic equations
- Kretschmann scalar (R_μνρσ R^μνρσ)
- Ricci squared (R_μν R^μν)
- Gauss–Bonnet scalar (R^2 -4 R_μν R^μν + R_μνρσ R^μνρσ)
- Weyl tensor (non‑zero components)
- Weyl squared scalar (C_μνρσ C^μνρσ)
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
    WeylTensor,           # <-- added
)

# Version and citation information
__version__ = "2.0.0"
__author__ = "P. Ntelis"
__github_repo__ = "https://github.com/lontelis/EinsteinKPy2Tex"

def print_citation():
    r"""Print citation information for this code"""
    citation = r"""
    ============================================================================
    Schwarzschild Metric Tensor Calculator v2.0 (with Weyl tensor)
    ============================================================================
    If you use this code in your research, please cite:
    
    [1] Einstein, A. (1915). Die Feldgleichungen der Gravitation.
        Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften, 
        844-847.
    
    [2] Ribeiro, S., et al. (2020). EinsteinPy: A Python Package for General Relativity.
        Journal of Open Source Software, 5(51), 2356.
    
    [3] P. Ntelis (2026). EinsteinKPy2Tex: Schwarzschild Metric Tensor Calculator (Version 2.0).
        GitHub. https://github.com/lontelis/EinsteinKPy2Tex
    ============================================================================
    """
    print(citation)

def generate_bib_file():
    r"""Generate a BibTeX file with all citations"""
    bib_content = r"""% BibTeX citations for EinsteinKPy2Tex project (Schwarzschild with Weyl)
% Generated on 11 June 2026

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

@software{EinsteinKPy2Tex2026,
    author = {P. Ntelis},
    title = {EinsteinKPy2Tex: Schwarzschild Metric Tensor Calculator with Weyl Tensor},
    year = {2026},
    url = {https://github.com/lontelis/EinsteinKPy2Tex},
    version = {2.0}
}
"""
    with open("citations.bib", "w") as f:
        f.write(bib_content)
    print("✓ BibTeX citation file 'citations.bib' generated successfully!")

# Command line arguments
parser = argparse.ArgumentParser(description='Schwarzschild Metric Tensor Calculator')
parser.add_argument('--cite', action='store_true', help='Display citation information')
parser.add_argument('--generate_bib', action='store_true', help='Generate BibTeX citation file')
parser.add_argument('--version', action='store_true', help='Show version information')
args = parser.parse_args()

if args.version:
    print(f"EinsteinKPy2Tex version {__version__}")
    print(f"GitHub: {__github_repo__}")
    exit()
if args.cite:
    print_citation()
    exit()
if args.generate_bib:
    generate_bib_file()
    exit()

# ============================================================================
# 1. Coordinates and metric (Schwarzschild)
# ============================================================================
t, r, theta, phi = sp.symbols("t r theta phi")
coords = [t, r, theta, phi]
coord_names = ['t', 'r', '\\theta', '\\phi']

G = sp.Symbol("G", positive=True, real=True)
M = sp.Symbol("M", positive=True, real=True)
c = sp.Symbol("c", positive=True, real=True)
R_s = sp.Symbol("R_s", positive=True, real=True)   # = 2GM/c²

schwarzschild_factor = 1 - R_s / r

metric_arr = [
    [-c**2 * schwarzschild_factor, 0, 0, 0],
    [0, 1 / schwarzschild_factor, 0, 0],
    [0, 0, r**2, 0],
    [0, 0, 0, r**2 * sp.sin(theta)**2],
]

metric = MetricTensor(metric_arr, coords, "ll", name="SchwarzschildMetric")

# ============================================================================
# 2. Compute all tensors
# ============================================================================
ch = ChristoffelSymbols.from_metric(metric)
riem = RiemannCurvatureTensor.from_metric(metric)
ric = RicciTensor.from_metric(metric)
rsc = RicciScalar.from_metric(metric)
ein = EinsteinTensor.from_metric(metric)
weyl = WeylTensor.from_metric(metric)          # <-- Weyl tensor

# ============================================================================
# 3. Geodesic equations
# ============================================================================
def compute_geodesic_equations(christoffel, coords):
    D = len(coords)
    velocities = [sp.Symbol(f"\\dot{{{coord}}}") for coord in ['t', 'r', '\\theta', '\\phi']]
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

# ============================================================================
# 4. Kretschmann scalar (as before)
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

kretschmann_full, kretschmann_simplified = compute_kretschmann_scalar(riem, metric, coords)

# ============================================================================
# 5. Ricci squared (R_μν R^μν)
# ============================================================================
def ricci_squared(ricci_tensor, metric, coords):
    D = len(coords)
    R_down = ricci_tensor.tensor()
    g_matrix = sp.Matrix(metric.tensor())
    g_inv = g_matrix.inv()
    R_up = [[0 for _ in range(D)] for _ in range(D)]
    for mu in range(D):
        for nu in range(D):
            s = 0
            for alpha in range(D):
                for beta in range(D):
                    s += g_inv[mu, alpha] * g_inv[nu, beta] * R_down[alpha, beta]
            R_up[mu][nu] = s
    ric2 = 0
    for mu in range(D):
        for nu in range(D):
            ric2 += R_down[mu, nu] * R_up[mu][nu]
    return sp.simplify(ric2)

ric2 = ricci_squared(ric, metric, coords)

# ============================================================================
# 6. Gauss-Bonnet scalar
# ============================================================================
def gauss_bonnet_scalar(rscalar, ric2, kretschmann):
    return sp.simplify(rscalar**2 - 4 * ric2 + kretschmann)

gb = gauss_bonnet_scalar(rsc.expr, ric2, kretschmann_simplified)

# ============================================================================
# 7. Weyl squared (C_μνρσ C^μνρσ)
# ============================================================================
def compute_weyl_squared(weyl_tensor, metric, coords):
    """
    Compute C^2 = C_{μνρσ} C^{μνρσ} using the same method as for Kretschmann.
    Assumes weyl_tensor.tensor() returns C^μ_νρσ (mixed indices).
    """
    D = len(coords)
    C_mixed = weyl_tensor.tensor()
    g_matrix = sp.Matrix(metric.tensor())
    g_inv = g_matrix.inv()

    # Lower first index: C_{μνρσ} = g_{μα} C^α_νρσ
    C_cov = [[[[0 for _ in range(D)] for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for mu in range(D):
        for nu in range(D):
            for rho in range(D):
                for sigma in range(D):
                    total = 0
                    for alpha in range(D):
                        total += g_matrix[mu, alpha] * C_mixed[alpha, nu, rho, sigma]
                    C_cov[mu][nu][rho][sigma] = total

    # Raise all indices: C^{αβγδ} = g^{αμ} g^{βν} g^{γρ} g^{δσ} C_{μνρσ}
    C_con = [[[[0 for _ in range(D)] for _ in range(D)] for _ in range(D)] for _ in range(D)]
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
                                              C_cov[mu][nu][rho][sigma])
                    C_con[alpha][beta][gamma][delta] = total

    # Contract: C^2 = C^{αβγδ} * C_{αβγδ}
    C2 = 0
    for alpha in range(D):
        for beta in range(D):
            for gamma in range(D):
                for delta in range(D):
                    C2 += C_con[alpha][beta][gamma][delta] * C_cov[alpha][beta][gamma][delta]
    return sp.simplify(C2)

weyl_squared = compute_weyl_squared(weyl, metric, coords)

# ============================================================================
# 8. LaTeX output helpers (unchanged)
# ============================================================================
def latex_nonzero(tensor_obj, tensor_symbol, rank):
    arr = tensor_obj.tensor()
    non_zero = []
    D = len(coords)
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
# 9. Write LaTeX file
# ============================================================================
filename = "schw_EinsteinKPy2Tex.tex"
with open(filename, "w") as f:
    f.write("\\documentclass{article}\n")
    f.write("\\usepackage{amsmath,amssymb}\n")
    f.write("\\begin{document}\n\n")
    f.write("% This LaTeX file was generated by EinsteinKPy2Tex v2.0\n")
    f.write("% GitHub: https://github.com/lontelis/EinsteinKPy2Tex\n\n")
    f.write("\\title{Geometric Quantities for the Schwarzschild Metric (with Weyl Tensor)}\n")
    f.write("\\author{Generated by EinsteinKPy2Tex}\n")
    f.write("\\date{\\today}\n")
    f.write("\\maketitle\n\n")

    f.write("\\section{Citation Information}\n")
    f.write("... (same as before) ...\n\n")

    f.write("\\section{Geometric quantities for the Schwarzschild metric}\n\n")
    f.write("The Schwarzschild metric is given by\n")
    f.write("\\begin{align}\n")
    f.write("ds^2 = -\\left(1-\\frac{2GM}{c^2 r}\\right) c^2 dt^2 + \\left(1-\\frac{2GM}{c^2 r}\\right)^{-1} dr^2 + r^2 d\\theta^2 + r^2 \\sin^2\\theta d\\phi^2 .\n")
    f.write("\\end{align}\n\n")

    f.write("\\subsection{Metric tensor $g_{\\mu\\nu}$}\n")
    f.write("\\begin{align}\n")
    f.write(sp.latex(metric.tensor()))
    f.write("\n\\end{align}\n\n")

    f.write("\\subsection{Christoffel symbols $\\Gamma^{\\mu}_{\\nu\\rho}$ (non-zero)}\n")
    f.write("\\begin{align}\n")
    f.write(latex_nonzero(ch, r"\Gamma", 3))
    f.write("\n\\end{align}\n\n")

    f.write("\\subsection{Riemann curvature tensor $R^{\\mu}_{\\ \\nu\\rho\\sigma}$ (non-zero)}\n")
    f.write("\\begin{align}\n")
    f.write(latex_nonzero(riem, "R", 4))
    f.write("\n\\end{align}\n\n")

    f.write("\\subsection{Weyl curvature tensor $C^{\\mu}_{\\ \\nu\\rho\\sigma}$ (non-zero)}\n")
    f.write("\\begin{align}\n")
    f.write(latex_nonzero(weyl, "C", 4))
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
    f.write("where $\\lambda$ is an affine parameter and $\\dot{x}^\\mu = dx^\\mu/d\\lambda$.\n\n")

    f.write("\\subsection{Kretschmann scalar $R_{\\mu\\nu\\rho\\sigma}R^{\\mu\\nu\\rho\\sigma}$}\n")
    f.write("\\subsubsection*{Full expression}\n")
    f.write("\\begin{align}\n")
    f.write(sp.latex(kretschmann_full))
    f.write("\n\\end{align}\n\n")
    f.write("\\subsubsection*{Simplified expression}\n")
    f.write("\\begin{align}\n")
    f.write(sp.latex(kretschmann_simplified))
    f.write("\n\\end{align}\n\n")

    f.write("\\subsection{Ricci squared $R_{\\mu\\nu}R^{\\mu\\nu}$}\n")
    f.write("\\begin{align}\n")
    f.write(sp.latex(ric2))
    f.write("\n\\end{align}\n\n")

    f.write("\\subsection{Gauss-Bonnet scalar $\\mathcal{R}_{GB} = R^2 - 4R_{\\mu\\nu}R^{\\mu\\nu} + R_{\\mu\\nu\\rho\\sigma}R^{\\mu\\nu\\rho\\sigma}$}\n")
    f.write("\\begin{align}\n")
    f.write(sp.latex(gb))
    f.write("\n\\end{align}\n\n")

    f.write("\\subsection{Weyl squared scalar $C_{\\mu\\nu\\rho\\sigma}C^{\\mu\\nu\\rho\\sigma}$}\n")
    f.write("\\begin{align}\n")
    f.write(sp.latex(weyl_squared))
    f.write("\n\\end{align}\n\n")

    f.write("\\end{document}\n")

print(f"✓ LaTeX output written to {filename}")
print(f"\nTo cite this work, run: python {__file__} --cite")
print(f"To generate BibTeX file, run: python {__file__} --generate_bib")
print(f"\nGitHub repository: https://github.com/lontelis/EinsteinKPy2Tex")