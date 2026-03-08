# Estimating Continuous Treatment Effects with Two-Stage Kernel Ridge Regression

This repository contains code for the paper:

**Seok-Jin Kim, Kaizheng Wang**  
*Estimating Continuous Treatment Effects with Two-Stage Kernel Ridge Regression*

The goal is to estimate the continuous treatment effect (dose-response) curve $h(t) = \mathbb{E}[Y(t)]$ from observational data with confounding.

## Problem Setting

Given $n$ observational samples $\{(x_i, t_i, y_i)\}_{i=1}^n$ (covariates, continuous treatment, outcome), the goal is to estimate the population dose-response curve $h(t)=\mathbb{E}_x[Y(t)]$. Since treatment assignment $t_i$ depends on $x_i$, naive regression of $y_i$ on $t_i$ targets $\mathbb{E}[Y \mid T=t]$ and is generally biased for $h(t)$.

## Method Summary (Two-Stage KRR)

The proposed estimator uses two-stage kernel ridge regression:

1. **Stage 1 (nuisance model):** Fit $f(x,t) \approx \mathbb{E}[Y \mid X=x, T=t]$ on the joint space $(X,T)$.
2. **Stage 2 (target model):** Build pseudo-outcomes by averaging $\hat f(X_i, t)$ over empirical covariates and fit a 1D KRR smoother for $h(t)$.
3. **Model selection:** Use a split-sample proxy-validation rule to select the second-stage regularizer.


## Repository Layout

- `Demo_synthetic.ipynb`  
  Main synthetic benchmark runner (`ours` / `plugin` / `direct`).
- `Demo_semi-real.ipynb`  
  Main semi-real (Job Corps) benchmark runner (`ours` / `plugin` / `direct`).
- `KRR_methods/`  
  Core KRR estimators, kernels, synthetic DGPs, and length-scale selection notebooks.
- `DML_methods/`  
  DML baselines and auxiliary scripts used for semi-real comparisons.

## Quick Start

### 1) Environment

Recommended: Python 3.10+

```bash
pip install numpy scipy pandas scikit-learn matplotlib tqdm jupyter
```

Optional (for DML/GRF notebooks):

- `rpy2`
- R package `grf`
- PyTorch (for NN-based DML variants)

### 2) Synthetic Benchmark

Open and run:

- `Demo_synthetic.ipynb`

In the selector cell set:

- `ALGO` in `{ "ours", "plugin", "direct" }`
- `N_SAMPLES`
- `K_RUNS`
- `NOISE_STD`
- `FIRST_SEED`

Results are saved to:

- `KRR_methods/Results/`

Optional tuning notebook:

- `KRR_methods/length_selection_synthetic.ipynb`

### 3) Semi-real Job Corps Benchmark

Open and run:

- `Demo_semi-real.ipynb`

This notebook uses:

- `DML_methods/Data_and_Results/emp_app.csv`
- `DML_methods/Data_and_Results/semi-syn data grf.csv`
- `DML_methods/Data_and_Results/h_star_grf_empapp.csv`

Results are saved to:

- `KRR_methods/Results/`

Optional tuning notebook:

- `KRR_methods/length_selection_semi-real.ipynb`

### 4) DML Baselines (Semi-real)

Open and run:

- `DML_methods/DML_Semi-real_GRF.ipynb`
- `DML_methods/DML_Semi-real_LASSO,NN,KNN.ipynb`

## Experimental Config Notes

### Synthetic setup (paper-aligned)

- `ours`: proposed two-stage KRR estimator.
- `plugin`: plug-in estimator based on the first-stage fit.
- `direct` (Direct Regression): T-only KRR baseline that ignores covariates.
- In synthetic experiments, all three methods use Matérn-kernel KRR and are evaluated on the same fixed treatment grid for MISE.

### Semi-real setup (Job Corps)

- Ours / Plug-in first stage: tensor-product Laplace kernel (Matérn $\nu=0.5$).
- Ours second stage: Matérn kernel with $\nu=1.5$.
- Direct baseline: 1D KRR with a Laplace kernel.

<!-- ## Reported Results Snapshot

### Synthetic (MISE x 100, mean with SE)

| Method | n = 1000 | n = 500 |
|---|---:|---:|
| **Ours** | **6.22 (0.32)** | **8.40 (0.35)** |
| Plug-in | 9.87 (0.31) | 11.81 (0.28) |
| Direct Regression | 14.52 (0.31) | 14.84 (0.36) |

### Semi-real (Job Corps, MISE mean with SE)

| Method | Mean MISE (SE) |
|---|---:|
| **Ours** | **1.2466 (0.1209)** |
| Plug-in LOOCV | 1.6173 (0.1156) |
| Direct Regression | 1.6970 (0.1264) |
| DML (GRF) | 2.4230 (0.1837) |
| DML (NN) | 2.1065 (0.1454) |
| DML (LASSO) | 2.8732 (0.2391) |
| DML (KNN) | 2.9742 (0.2165) | -->
