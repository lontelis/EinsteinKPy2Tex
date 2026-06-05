---
title: 'EinsteinKPy2Tex: A Python Tool for Computing and Exporting General Relativity Tensors to LaTeX'
tags:
  - Python
  - General Relativity
  - Schwarzschild metric
  - FLRW metric
  - Kretschmann scalar
  - Geodesic equations
  - Tensor calculus
  - LaTeX export
  - Symbolic computation
  - Cosmology
  - Black hole physics
authors:
  - name: Pierros Ntelis
    orcid: 0000-0002-7849-2418
    affiliation: "1, 2"
affiliations:
  - name: School of Physics, Harbin Institute of Technology, Harbin 150001, People's Republic of China
    index: 1
  - name: Institute of Theoretical Physics, National University of Uzbekistan, Tashkent 100174, Uzbekistan
    index: 2
date: 5 June 2026
bibliography: paper.bib

---

# Summary

EinsteinKPy2Tex is an open-source Python package that computes fundamental geometric quantities for the Friedmann-Lemaître-Robertson-Walker (FLRW) and Schwarzschild metrics using the EinsteinPy library. The code automatically calculates Christoffel symbols, Riemann curvature tensor, Ricci tensor, Ricci scalar, Einstein tensor, geodesic equations, and the Kretschmann scalar. Results are exported as professionally formatted LaTeX documents, facilitating direct inclusion in research papers and educational materials.

The FLRW implementation supports cosmological studies of the expanding universe, while the Schwarzschild implementation describes spacetime geometry around non-rotating black holes. The code includes built-in citations for Einstein (1915) and the EinsteinPy library (Ribeiro et al., 2020), ensuring proper academic attribution.

# Statement of need

General relativity (GR) calculations—particularly tensor computations like Christoffel symbols, Riemann curvature, and the Kretschmann scalar—are error-prone and time-consuming when performed manually. While symbolic computation packages like SymPy (Meurer et al., 2017) and EinsteinPy (Ribeiro et al., 2020) exist, there remains a gap between symbolic calculation and publication-ready output. Researchers often need to verify intermediate steps, derive geodesic equations, or compute curvature invariants, all while maintaining clear records for papers and theses.

EinsteinKPy2Tex fills this niche by providing:

- **Complete tensor calculations** for FLRW and Schwarzschild metrics (Christoffel, Riemann, Ricci, Einstein)
- **Geodesic equations** derived automatically from Christoffel symbols
- **Kretschmann scalar** $K = R^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}$ for singularity identification
- **LaTeX export** with only non-zero components and proper index spacing
- **Built-in citations** for proper academic attribution

The software is designed for educators, students, and researchers needing rapid, accurate tensor calculations with publication-ready output.

# Key features

## Metrics supported

1. **FLRW (cosmological)**: $ds^2 = -c^2 dt^2 + a(t)^2 (dx^2 + dy^2 + dz^2)$
2. **Schwarzschild (black hole)**: $ds^2 = -(1-2GM/c^2r)c^2dt^2 + (1-2GM/c^2r)^{-1}dr^2 + r^2d\theta^2 + r^2\sin^2\theta d\phi^2$

## Quantities computed

- Metric tensor $g_{\mu\nu}$
- Christoffel symbols $\Gamma^{\mu}_{\nu\rho}$ (non-zero only)
- Riemann curvature tensor $R^{\mu}_{\;\nu\rho\sigma}$ (non-zero only)
- Ricci tensor $R_{\mu\nu}$ (non-zero only)
- Ricci scalar $R$
- Einstein tensor $G_{\mu\nu}$ (non-zero only)
- Geodesic equations
- Kretschmann scalar $K = R^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}$

## Customizability

Users can easily modify the code for custom metrics by changing:
1. Coordinate definitions and symbols
2. The $4 \times 4$ metric tensor array

Examples are provided for Minkowski spacetime and general spherically symmetric metrics.

# Verification

We validate EinsteinKPy2Tex against known analytical results:

- **Schwarzschild**: $R_{\mu\nu} = 0$ (vacuum), $K = 48G^2M^2/c^4r^6$
- **FLRW**: $R = 6(\ddot{a}/a + \dot{a}^2/c^2)/a^2$, $K = 12(a^2\ddot{a}^2 + \dot{a}^4)/c^4a^4$

All tests confirm correctness.

# Acknowledgements

The author thanks the EinsteinPy development team and DeepSeek AI for assistance with code optimization.

# References