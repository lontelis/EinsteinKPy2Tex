"""
Schwarzschild Metric Tensor Calculator
=======================================
Author: P. Ntelis
Version: 1.0
Date: 2026-06-05
GitHub: https://github.com/[YourUsername]/Einsteinpy_to_latex

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

3. This software (Schwarzschild Metric Tensor Calculator):
   @software{Einsteinpy_to_latex2026,
       author = {Your Name},
       title = {Einsteinpy_to_latex: Schwarzschild Metric Tensor Calculator},
       year = {2026},
       url = {https://github.com/[YourUsername]/Einsteinpy_to_latex},
       version = {1.0},
       note = {Computes Christoffel symbols, Riemann, Ricci, and Einstein 
               tensors for the Schwarzschild metric}
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
__author__ = "Your Name"
__github_repo__ = "https://github.com/[YourUsername]/Einsteinpy_to_latex"

def print_citation():
    """Print citation information for this code"""
    citation = """
    ============================================================================
    Schwarzschild Metric Tensor Calculator v1.0
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
    
    [3] Your Name (2026). Einsteinpy_to_latex: Schwarzschild Metric Tensor 
        Calculator (Version 1.0). GitHub.
        https://github.com/lontelis/Einsteinpy_to_latex
    
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
    
    @software{Einsteinpy_to_latex2026,
        author = P. Ntelis,
        title = {Einsteinpy_to_latex: Schwarzschild Metric Tensor Calculator},
        year = {2026},
        url = {https://github.com/lontelis/Einsteinpy_to_latex},
        version = {1.0}
    }
    ============================================================================
    """
    print(citation)

def generate_bib_file():
    """Generate a BibTeX file with all citations"""
    bib_content = """% BibTeX citations for Einsteinpy_to_latex project
% Generated on 2026-06-05
% GitHub: https://github.com/lontelis/Einsteinpy_to_latex

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

@software{Einsteinpy_to_latex2026,
    author = {Your Name},
    title = {Einsteinpy_to_latex: Schwarzschild Metric Tensor Calculator},
    year = {2026},
    url = {https://github.com/lontelis/Einsteinpy_to_latex},
    version = {1.0},
    note = {Computes Christoffel symbols, Riemann, Ricci, and Einstein 
            tensors for the Schwarzschild metric}
}
"""
    with open("citations.bib", "w") as f:
        f.write(bib_content)
    print("✓ BibTeX citation file 'citations.bib' generated successfully!")

# Parse command line arguments
parser = argparse.ArgumentParser(
    description='Schwarzschild Metric Tensor Calculator',
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
    print(f"Einsteinpy_to_latex version {__version__}")
    print(f"GitHub: {__github_repo__}")
    exit()

if args.cite:
    print_citation()
    exit()

if args.generate_bib:
    generate_bib_file()
    exit()

# 1. Coordinates and functions
t, r, theta, phi = sp.symbols("t r theta phi")
coords = [t, r, theta, phi]
coord_names = ['t', 'r', '\\theta', '\\phi']  # for LaTeX labels

# Schwarzschild parameters
G = sp.Symbol("G", positive=True, real=True)  # gravitational constant
M = sp.Symbol("M", positive=True, real=True)  # mass
c = sp.Symbol("c", positive=True, real=True)  # speed of light

# Schwarzschild metric components
schwarzschild_factor = 1 - 2 * G * M / (c**2 * r)

# 2. Metric (4D)
metric_arr = [
    [-c**2 * schwarzschild_factor, 0, 0, 0],
    [0, 1 / schwarzschild_factor, 0, 0],
    [0, 0, r**2, 0],
    [0, 0, 0, r**2 * sp.sin(theta)**2],
]
metric = MetricTensor(metric_arr, coords, "ll", name="SchwarzschildMetric")

# 3. Compute tensors
ch = ChristoffelSymbols.from_metric(metric)
riem = RiemannCurvatureTensor.from_metric(metric)
ric = RicciTensor.from_metric(metric)
rsc = RicciScalar.from_metric(metric)
ein = EinsteinTensor.from_metric(metric)

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
        for i in range(D_coords):
            for j in range(D_coords):
                val = sp.simplify(arr[i, j])
                if val != 0:
                    label = f"{coord_names[i]}{coord_names[j]}"
                    non_zero.append(f"{tensor_symbol}_{{{label}}} &= {sp.latex(val)} \\\ ")
    elif rank == 3:
        for i in range(D_coords):
            for j in range(D_coords):
                for k in range(D_coords):
                    val = sp.simplify(arr[i, j, k])
                    if val != 0:
                        label = f"{{{coord_names[i]}}}_{{{coord_names[j]}{coord_names[k]}}}"
                        non_zero.append(f"{tensor_symbol}^{label} &= {sp.latex(val)} \\\ ")
    elif rank == 4:
        for i in range(D_coords):
            for j in range(D_coords):
                for k in range(D_coords):
                    for l in range(D_coords):
                        val = sp.simplify(arr[i, j, k, l])
                        if val != 0:
                            label = f"{{{coord_names[i]}}}_{{{coord_names[j]}{coord_names[k]}{coord_names[l]}}}"
                            non_zero.append(f"{tensor_symbol}^{label} &= {sp.latex(val)} \\\ ")
    else:
        return "Unsupported rank"
    
    return "\n".join(non_zero) if non_zero else "All components zero."

# 4. Write to LaTeX file
filename = "schwarzschild_to_latex.tex"
with open(filename, "w") as f:
    f.write("\\documentclass{article}\n")
    f.write("\\usepackage{amsmath}\n")
    f.write("\\begin{document}\n\n")
    
    # Add citation notice in LaTeX
    f.write("% This LaTeX file was generated by Einsteinpy_to_latex v1.0\n")
    f.write("% GitHub: https://github.com/[YourUsername]/Einsteinpy_to_latex\n")
    f.write("% Please cite: Einstein (1915), EinsteinPy (2020), and this software\n\n")
    
    f.write("\\title{Geometric Quantities for the Schwarzschild Metric}\n")
    f.write("\\author{Generated by Einsteinpy\\_to\\_latex}\n")
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
    f.write("\\item P. Ntelis (2026). Einsteinpy\\_to\\_latex: Schwarzschild Metric Tensor Calculator (Version 1.0).\n")
    f.write("      \\texttt{https://github.com/lontelis/Einsteinpy\\_to\\_latex}\n")
    f.write("\\end{itemize}\n\n")
    
    f.write("\\section{Geometric quantities for the Schwarzschild metric}\n\n")
    f.write("The Schwarzschild metric is given by\n")
    f.write("\\begin{align}\n")
    f.write("ds^2 = -\\left(1-\\frac{2GM}{c^2 r}\\right) c^2 dt^2 + \\left(1-\\frac{2GM}{c^2 r}\\right)^{-1} dr^2 + r^2 d\\theta^2 + r^2 \\sin^2\\theta d\\phi^2 .\n")
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
    
    f.write("\\end{document}\n")

print(f"✓ LaTeX output written to {filename}")
print(f"\nTo cite this work, run: python {__file__} --cite")
print(f"To generate BibTeX file, run: python {__file__} --generate_bib")
print(f"\nGitHub repository: https://github.com/lontelis/Einsteinpy_to_latex")