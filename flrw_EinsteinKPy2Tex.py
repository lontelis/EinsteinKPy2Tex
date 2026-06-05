"""
FLRW Metric Tensor Calculator
==============================
Author: P. Ntelis
Code date: 5 June 2026
Version: 1.0
GitHub: https://github.com/lontelis/EinsteinKPy2Tex

CITATION INFORMATION
====================
If you use this code in your research, please cite:

1. The Einstein paper (original theory):
   @article{Einstein1915,
       title = {Die Feldgleichungen der Gravitation},
       author = {Einstein, Albert},
       journal = {Sitzungsberichte der K{\"o}niglich Preu{\ss}ischen 
                  Akademie der Wissenschaften},
       pages = {844--847},
       year = {1915},
       url = {https://einsteinpapers.press.princeton.edu/vol6-doc/}
   }

2. The EinsteinPy library:
   @article{EinsteinPy2020,
       title = {EinsteinPy: A Python Package for General Relativity},
       author = {Ribeiro, Shreyas and Bapat, Aaryan and Tandon, Ayush 
                 and {EinsteinPy Developers}},
       journal = {Journal of Open Source Software},
       volume = {5},
       number = {51},
       pages = {2356},
       year = {2020},
       doi = {10.21105/joss.02356},
       url = {https://arxiv.org/abs/2005.11288}
   }

3. This software (FLRW Metric Tensor Calculator):
   @software{EinsteinKPy2Tex2026,
       author = {P. Ntelis},
       title = {EinsteinKPy2Tex: FLRW Metric Tensor Calculator},
       year = {2026},
       url = {https://github.com/lontelis/EinsteinKPy2Tex},
       version = {1.0},
       note = {Computes Christoffel symbols, Riemann, Ricci, and Einstein 
               tensors for the FLRW metric}
   }
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

# Version and citation information
__version__ = "1.0.0"
__author__ = "P. Ntelis"
__date__ = "5 June 2026"
__github_repo__ = "https://github.com/lontelis/EinsteinKPy2Tex"

def print_citation():
    """Print citation information for this code"""
    citation = """
    ============================================================================
    FLRW Metric Tensor Calculator v1.0
    Author: P. Ntelis
    Date: 5 June 2026
    ============================================================================
    If you use this code in your research, please cite:
    
    [1] Einstein, A. (1915). Die Feldgleichungen der Gravitation.
        Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften, 
        844-847.
    
    [2] Ribeiro, S., Bapat, A., Tandon, A., & EinsteinPy Developers (2020).
        EinsteinPy: A Python Package for General Relativity.
        Journal of Open Source Software, 5(51), 2356.
        https://doi.org/10.21105/joss.02356
        arXiv: https://arxiv.org/abs/2005.11288
    
    [3] P. Ntelis (2026). EinsteinKPy2Tex: FLRW Metric Tensor 
        Calculator (Version 1.0). GitHub.
        https://github.com/lontelis/EinsteinKPy2Tex
    
    BibTeX entries:
    -----------------
    @article{Einstein1915,
        title = {Die Feldgleichungen der Gravitation},
        author = {Einstein, Albert},
        journal = {Sitzungsberichte der K{\"o}niglich Preu{\ss}ischen 
                  Akademie der Wissenschaften},
        pages = {844--847},
        year = {1915}
    }
    
    @article{EinsteinPy2020,
        title = {EinsteinPy: A Python Package for General Relativity},
        author = {Ribeiro, Shreyas and Bapat, Aaryan and Tandon, Ayush 
                  and {EinsteinPy Developers}},
        journal = {Journal of Open Source Software},
        volume = {5},
        number = {51},
        pages = {2356},
        year = {2020},
        doi = {10.21105/joss.02356},
        url = {https://arxiv.org/abs/2005.11288}
    }
    
    @software{EinsteinKPy2Tex2026,
        author = {P. Ntelis},
        title = {EinsteinKPy2Tex: FLRW Metric Tensor Calculator},
        year = {2026},
        url = {https://github.com/lontelis/EinsteinKPy2Tex},
        version = {1.0}
    }
    ============================================================================
    """
    print(citation)

def generate_bib_file():
    """Generate a BibTeX file with all citations"""
    bib_content = """% BibTeX citations for EinsteinKPy2Tex project (FLRW Metric)
% Generated on 5 June 2026
% Author: P. Ntelis
% GitHub: https://github.com/lontelis/EinsteinKPy2Tex

@article{Einstein1915,
    title = {Die Feldgleichungen der Gravitation},
    author = {Einstein, Albert},
    journal = {Sitzungsberichte der K{\"o}niglich Preu{\ss}ischen 
              Akademie der Wissenschaften},
    pages = {844--847},
    year = {1915},
    url = {https://einsteinpapers.press.princeton.edu/vol6-doc/}
}

@article{EinsteinPy2020,
    title = {EinsteinPy: A Python Package for General Relativity},
    author = {Ribeiro, Shreyas and Bapat, Aaryan and Tandon, Ayush 
              and {EinsteinPy Developers}},
    journal = {Journal of Open Source Software},
    volume = {5},
    number = {51},
    pages = {2356},
    year = {2020},
    doi = {10.21105/joss.02356},
    url = {https://arxiv.org/abs/2005.11288}
}

@software{EinsteinKPy2Tex2026,
    author = {P. Ntelis},
    title = {EinsteinKPy2Tex: FLRW Metric Tensor Calculator},
    year = {2026},
    url = {https://github.com/lontelis/EinsteinKPy2Tex},
    version = {1.0},
    note = {Computes Christoffel symbols, Riemann, Ricci, and Einstein 
            tensors for the FLRW metric}
}
"""
    with open("citations.bib", "w") as f:
        f.write(bib_content)
    print("✓ BibTeX citation file 'citations.bib' generated successfully!")

# Parse command line arguments
parser = argparse.ArgumentParser(
    description='FLRW Metric Tensor Calculator',
    epilog='For citation information, use --cite or --generate_bib'
)
parser.add_argument('--cite', action='store_true', 
                   help='Display citation information')
parser.add_argument('--generate_bib', action='store_true',
                   help='Generate BibTeX citation file (citations.bib)')
parser.add_argument('--version', action='store_true',
                   help='Show version information')
args = parser.parse_args()

if args.version:
    print(f"EinsteinKPy2Tex version {__version__}")
    print(f"Author: {__author__}")
    print(f"Date: {__date__}")
    print(f"GitHub: {__github_repo__}")
    exit()

if args.cite:
    print_citation()
    exit()

if args.generate_bib:
    generate_bib_file()
    exit()

# 1. Coordinates and functions
t, x, y, z = sp.symbols("t x y z")
coords = [t, x, y, z]
coord_names = ['t', 'x', 'y', 'z']  # for LaTeX labels

a = sp.Function("a")(t)
c = sp.Symbol("c", positive=True, real=True)

# 2. Metric (4D)
metric_arr = [
    [-c**2, 0, 0, 0],
    [0, a**2, 0, 0],
    [0, 0, a**2, 0],
    [0, 0, 0, a**2],
]

metric = MetricTensor(metric_arr, coords, "ll", name="FLRWMetric")

# 3. Compute tensors
ch = ChristoffelSymbols.from_metric(metric)
riem = RiemannCurvatureTensor.from_metric(metric)
ric = RicciTensor.from_metric(metric)
rsc = RicciScalar.from_metric(metric)
ein = EinsteinTensor.from_metric(metric)

# 4. Compute geodesic equations
def compute_geodesic_equations(christoffel, coords):
    """
    Compute the geodesic equations: d²x^μ/dλ² + Γ^μ_{νρ} (dx^ν/dλ)(dx^ρ/dλ) = 0
    Returns a list of equations for each coordinate
    """
    D = len(coords)
    # Create symbols for velocities (first derivatives)
    velocities = [sp.Symbol(f"\\dot{{{coord}}}") for coord in ['t', 'x', 'y', 'z']]
    
    christoffel_arr = christoffel.tensor()
    
    geodesic_eqs = []
    for mu in range(D):
        eq = 0
        for nu in range(D):
            for rho in range(D):
                gamma = sp.simplify(christoffel_arr[mu, nu, rho])
                if gamma != 0:
                    eq += gamma * velocities[nu] * velocities[rho]
        geodesic_eqs.append(sp.Eq(sp.Symbol(f"\\ddot{{{coord_names[mu]}}} &"), -eq))
    
    return geodesic_eqs

geodesic_eqs = compute_geodesic_equations(ch, coords)

# 5. Compute Kretschmann scalar (COMPLETE - no simplification inside)
def compute_kretschmann_scalar(riemann, metric, coords):
    """
    Compute the Kretschmann scalar: K = R^{μνρσ} R_{μνρσ}
    Returns (full_expression, simplified_expression)
    """
    D = len(coords)
    
    # Get Riemann tensor from EinsteinPy (ordering: R^μ_νρσ)
    R_mixed = riemann.tensor()
    
    # Get metric and inverse metric
    g_matrix = sp.Matrix(metric.tensor())
    g_inv = g_matrix.inv()
    
    # Step 1: Lower first index to get fully covariant R_{μνρσ}
    # R_{μνρσ} = g_{μα} R^α_νρσ
    R_covariant = [[[[0 for _ in range(D)] for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for mu in range(D):
        for nu in range(D):
            for rho in range(D):
                for sigma in range(D):
                    total = 0
                    for alpha in range(D):
                        total += g_matrix[mu, alpha] * R_mixed[alpha, nu, rho, sigma]
                    R_covariant[mu][nu][rho][sigma] = total
    
    # Step 2: Raise all indices to get R^{αβγδ}
    # R^{αβγδ} = g^{αμ} g^{βν} g^{γρ} g^{δσ} R_{μνρσ}
    R_contravariant = [[[[0 for _ in range(D)] for _ in range(D)] for _ in range(D)] for _ in range(D)]
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
                                              R_covariant[mu][nu][rho][sigma])
                    R_contravariant[alpha][beta][gamma][delta] = total
    
    # Step 3: Contract to get Kretschmann scalar
    # K = R^{αβγδ} * R_{αβγδ}
    K_full = 0
    for alpha in range(D):
        for beta in range(D):
            for gamma in range(D):
                for delta in range(D):
                    K_full += R_contravariant[alpha][beta][gamma][delta] * R_covariant[alpha][beta][gamma][delta]

    
    # Return full expression and simplified expression separately
    return K_full, sp.simplify(K_full)

# Compute both full and simplified Kretschmann scalar
kretschmann_full, kretschmann_simplified = compute_kretschmann_scalar(riem, metric, coords)

# Helper: print non-zero components in LaTeX format
def latex_nonzero(tensor_obj, tensor_symbol, rank):
    """
    tensor_obj: EinsteinPy tensor object (e.g., ChristoffelSymbols)
    tensor_symbol: string for LaTeX (e.g., '\\Gamma', 'R')
    rank: 3 for Christoffel, 4 for Riemann, 2 for Ricci/Einstein
    """
    arr = tensor_obj.tensor()  # sympy Array or Matrix
    non_zero = []
    D_coords = np.size(coords)

    if rank == 2:
        # Ricci / Einstein (2D matrix)
        for i in range(D_coords):
            for j in range(D_coords):
                val = sp.simplify(arr[i, j])
                if val != 0:
                    label = f"{coord_names[i]}{coord_names[j]}"
                    non_zero.append(f"{tensor_symbol}_{{{label}}} &= {sp.latex(val)} \\\\")
    elif rank == 3:
        # Christoffel symbols: arr[i, j, k] -> Γ^i_{jk}
        for i in range(D_coords):
            for j in range(D_coords):
                for k in range(D_coords):
                    val = sp.simplify(arr[i, j, k])
                    if val != 0:
                        # Separate indices with spaces for better LaTeX parsing
                        upper = coord_names[i]
                        lower_j = coord_names[j]
                        lower_k = coord_names[k]
                        label = f"{{{upper}}}_{{{lower_j} {lower_k}}}"
                        non_zero.append(f"{tensor_symbol}^{label} &= {sp.latex(val)} \\\\")
    elif rank == 4:
        # Riemann: arr[i, j, k, l] -> R^i_{jkl}
        for i in range(D_coords):
            for j in range(D_coords):
                for k in range(D_coords):
                    for l in range(D_coords):
                        val = sp.simplify(arr[i, j, k, l])
                        if val != 0:
                            # Separate indices with spaces for better LaTeX parsing
                            upper = coord_names[i]
                            lower_j = coord_names[j]
                            lower_k = coord_names[k]
                            lower_l = coord_names[l]
                            label = f"{{{upper}}}_{{{lower_j} {lower_k} {lower_l}}}"
                            non_zero.append(f"{tensor_symbol}^{label} &= {sp.latex(val)} \\\\")
    else:
        return "Unsupported rank"
    
    return "\n".join(non_zero) if non_zero else "All components zero."

def latex_geodesic_equations(geodesic_eqs):
    """Format geodesic equations for LaTeX output"""
    latex_lines = []
    for eq in geodesic_eqs:
        latex_lines.append(sp.latex(eq) + " \\\\")
    return "\n".join(latex_lines)

# 6. Write to LaTeX file
filename = "flrw_EinsteinKPy2Tex.tex"
with open(filename, "w") as f:
    f.write("\\documentclass{article}\n")
    f.write("\\usepackage{amsmath}\n")
    f.write("\\usepackage{amssymb}\n")
    f.write("\\begin{document}\n\n")
    
    # Add citation notice in LaTeX
    f.write("% This LaTeX file was generated by EinsteinKPy2Tex v1.0\n")
    f.write("% Author: P. Ntelis\n")
    f.write("% Date: 5 June 2026\n")
    f.write("% GitHub: https://github.com/lontelis/EinsteinKPy2Tex\n")
    f.write("% Please cite: Einstein (1915), EinsteinPy (2020), and this software\n\n")
    
    f.write("\\title{Geometric Quantities for the FLRW Metric}\n")
    f.write("\\author{Generated by EinsteinKPy2Tex}\n")
    f.write("\\date{\\today}\n")
    f.write("\\maketitle\n\n")
    
    f.write("\\section{Citation Information}\n")
    f.write("If you use these results and code in your research, please cite:\n")
    f.write("\\begin{itemize}\n")
    f.write("\\item Einstein, A. (1915). Die Feldgleichungen der Gravitation. \n")
    f.write("      \\textit{Sitzungsberichte der K\\\"oniglich Preu\\ss ischen Akademie der Wissenschaften}, 844-847.\n")
    f.write("\\item Ribeiro, S., Bapat, A., Tandon, A., \\& EinsteinPy Developers (2020).\n")
    f.write("      EinsteinPy: A Python Package for General Relativity.\n")
    f.write("      \\textit{Journal of Open Source Software}, 5(51), 2356.\n")
    f.write("      \\texttt{https://doi.org/10.21105/joss.02356}\n")
    f.write("\\item P. Ntelis (2026). EinsteinKPy2Tex: FLRW Metric Tensor Calculator (Version 1.0).\n")
    f.write("      \\texttt{https://github.com/lontelis/EinsteinKPy2Tex}\n")
    f.write("\\end{itemize}\n\n")
    
    f.write("\\section{Geometric quantities for the FLRW metric}\n\n")
    f.write("The metric is given by\n")
    f.write("\\begin{align}\n")
    f.write("ds^2 = -c^2 dt^2 + a(t)^2 (dx^2+dy^2+dz^2) .\n")
    f.write("\\end{align}\n\n")
    
    f.write("\\subsection{Metric tensor $g_{\\mu\\nu}$}\n")
    f.write("\\begin{align} g_{\\mu\\nu}= \n")
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
    f.write("The geodesic equations are given by:\n")
    f.write("\\begin{align}\n")
    f.write(latex_geodesic_equations(geodesic_eqs))
    f.write("\n\\end{align}\n\n")
    f.write("where $\\lambda$ is an affine parameter and $\\dot{x}^\\mu = dx^\\mu/d\\lambda$.\n\n")
    
    f.write("\\subsection{Kretschmann scalar}\n")
    f.write("The Kretschmann scalar $K = R^{\\mu\\nu\\rho\\sigma} R_{\\mu\\nu\\rho\\sigma}$ is:\n\n")
    f.write("\\subsubsection*{Full expression (unsimplified)}\n")
    f.write("\\begin{align}\n")
    f.write(sp.latex(kretschmann_full))
    f.write("\n\\end{align}\n\n")
    f.write("\\subsubsection{Simplified expression}\n")
    f.write("\\begin{align} K = \n")
    f.write(sp.latex(kretschmann_simplified))
    f.write("\n\\end{align}\n\n")
    
    f.write("\\end{document}\n")

print(f"✓ LaTeX output written to {filename}")
print(f"\nTo cite this work, run: python {__file__} --cite")
print(f"To generate BibTeX file, run: python {__file__} --generate_bib")
print(f"\nGitHub repository: https://github.com/lontelis/EinsteinKPy2Tex")
print(f"Author: {__author__}")
print(f"Date: {__date__}")