# cte_jobcorps/__init__.py
"""
CTE estimation package for the Job Corps semi-synthetic experiments.

Submodules:
    - data_jobcorps   : data generation / preprocessing
    - kernels         : kernel functions (tensor-product etc.)
    - algorithms      : estimators and tuning routines
"""

# We intentionally avoid importing submodules here to prevent circular imports.
# Import directly from submodules, for example:
#
#   from cte_jobcorps.data_jobcorps import make_semi_jobcorps, make_Xss
#   from cte_jobcorps.algorithms.estimators_ours import run_ours_tensor_kernel
#   from cte_jobcorps.algorithms.estimators_plugin import run_plugin_loocv_on_original_grid
#   from cte_jobcorps.algorithms.length_selection import tune_length2d_and_beta_loocv_krr_nystrom
