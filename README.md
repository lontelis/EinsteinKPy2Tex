# Einsteinpy_to_latex
Einsteinpy_to_latex  Python tool computing GR tensors (Christoffel, Riemann, Ricci, Einstein) for FLRW &amp; Schwarzschild metrics. Exports non-zero components to LaTeX. Includes citations for Einstein (1915) &amp; EinsteinPy (arXiv:2005.11288).

A Python tool for computing general relativity tensor quantities and exporting them to LaTeX format. Supports FLRW and Schwarzschild metrics.

## Citations

If you use this code in your research, please cite:

1. **Einstein, A. (1915)**. Die Feldgleichungen der Gravitation. *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften*, 844-847.

2. **Ribeiro, S., Bapat, A., Tandon, A., & EinsteinPy Developers (2020)**. EinsteinPy: A Python Package for General Relativity. *Journal of Open Source Software*, 5(51), 2356.

3. **Ntelis, P. (2026)**. Einsteinpy_to_latex: FLRW and Schwarzschild Metric Tensor Calculator (Version 1.0). GitHub. https://github.com/lontelis/Einsteinpy_to_latex

## Dependencies

- Python 3.7+
- IPython
- SymPy
- NumPy
- EinsteinPy

## Installation

```bash
pip install ipython sympy numpy einsteinpy
```

## Files

- `einstein_to_latex.py` - FLRW metric calculator
- `Sch_einsteinpy_to_latex.py` - Schwarzschild metric calculator

## Usage

### FLRW Metric (Cosmological)

Run the FLRW metric calculator:

```bash
python einstein_to_latex.py
```

This computes tensors for the metric:
```
ds^2 = -c^2 dt^2 + a(t)^2 (dx^2 + dy^2 + dz^2)
```

### Schwarzschild Metric (Black Holes)

Run the Schwarzschild metric calculator:

```bash
python Sch_einsteinpy_to_latex.py
```

This computes tensors for the metric:
```
ds^2 = -(1 - 2GM/(c^2 r)) c^2 dt^2 + (1 - 2GM/(c^2 r))^{-1} dr^2 + r^2 dθ^2 + r^2 sin^2θ dφ^2
```

### Compile LaTeX Output

After running either script, compile the generated LaTeX file:

```bash
latex einstein_to_latex.tex
```

Or use pdflatex for PDF output:

```bash
pdflatex einstein_to_latex.tex
```

## Customizing for Your Own Metric

To compute tensors for a **simple custom metric**, modify the following sections in `einstein_to_latex.py`:

### 1. Define coordinates and functions:
```python
# 1. Coordinates and functions
t, x, y, z = sp.symbols("t x y z")
coords = [t, x, y, z]
coord_names = ['t', 'x', 'y', 'z']  # for LaTeX labels

a = sp.Function("a")(t)  # Example: scale factor
c = sp.Symbol("c", positive=True, real=True)  # Speed of light
```

### 2. Define your metric components:
```python
# 2. Metric (4D)
metric_arr = [
    [-c**2, 0, 0, 0],      # g_tt component
    [0, a**2, 0, 0],       # g_xx component
    [0, 0, a**2, 0],       # g_yy component
    [0, 0, 0, a**2],       # g_zz component
]
```

### Example: Minkowski Metric (flat spacetime)
```python
# 1. Coordinates
t, x, y, z = sp.symbols("t x y z")
coords = [t, x, y, z]
c = sp.Symbol("c", positive=True, real=True)

# 2. Minkowski metric
metric_arr = [
    [-c**2, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]
```

### Example: Custom Spherically Symmetric Metric
```python
# 1. Coordinates
t, r, theta, phi = sp.symbols("t r theta phi")
coords = [t, r, theta, phi]
coord_names = ['t', 'r', '\\theta', '\\phi']

# 2. Define metric functions
A = sp.Function("A")(r)
B = sp.Function("B")(r)

# 3. Custom metric
metric_arr = [
    [-A(r), 0, 0, 0],
    [0, B(r), 0, 0],
    [0, 0, r**2, 0],
    [0, 0, 0, r**2 * sp.sin(theta)**2],
]
```

After modifying these sections, run the script to generate LaTeX output for your custom metric.

## Command Line Options

Both scripts support these options:

| Option | Description |
|--------|-------------|
| `--cite` | Display citation information |
| `--generate_bib` | Generate BibTeX citation file |
| `--version` | Show version and author info |

### Examples

```bash
# Show citations
python einstein_to_latex.py --cite

# Generate BibTeX file
python einstein_to_latex.py --generate_bib

# Check version
python einstein_to_latex.py --version
```

## Output

The scripts generate:
- `einstein_to_latex.tex` - LaTeX document with all tensor components (FLRW metric)
- `Sch_einsteinpy_to_latex.tex` - LaTeX document for Schwarzschild metric
- `citations.bib` - BibTeX citation file (when using `--generate_bib`)

## Tensor Quantities Computed

- Metric tensor $g_{\mu\nu}$
- Christoffel symbols $\Gamma^{\mu}_{\nu\rho}$ (non-zero only)
- Riemann curvature tensor $R^{\mu}_{\ \nu\rho\sigma}$ (non-zero only)
- Ricci tensor $R_{\mu\nu}$ (non-zero only)
- Ricci scalar $R$
- Einstein tensor $G_{\mu\nu}$ (non-zero only)

## Example Output

When you run `python einstein_to_latex.py`, the LaTeX file will contain:

```latex
\subsection{Christoffel symbols $\Gamma^{\mu}_{\nu\rho}$ (non-zero)}
\begin{align}
\Gamma^{x}_{tx} &= \frac{\dot{a}(t)}{a(t)} \\
\Gamma^{y}_{ty} &= \frac{\dot{a}(t)}{a(t)} \\
\Gamma^{z}_{tz} &= \frac{\dot{a}(t)}{a(t)} \\
\Gamma^{t}_{xx} &= \frac{a(t) \dot{a}(t)}{c^2} \\
\Gamma^{t}_{yy} &= \frac{a(t) \dot{a}(t)}{c^2} \\
\Gamma^{t}_{zz} &= \frac{a(t) \dot{a}(t)}{c^2}
\end{align}
```

## Code Structure

```python
# Import dependencies
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

# Define coordinates and metric
# Compute tensors
# Export to LaTeX


## License

MIT License

## Author

**P. Ntelis** (2026)

## Repository

https://github.com/lontelis/Einsteinpy_to_latex
```

This README provides all necessary information for users to install, run, cite, and understand your code. Remember to replace `[YourUsername]` with your actual GitHub username.

## Acknowledgments

Developed with assistance from DeepSeek AI. Citations, mathematics, and physics verified by author.
