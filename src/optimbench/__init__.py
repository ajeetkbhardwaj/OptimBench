"""Benchmark functions for optimization algorithms.

Classical and CEC (Real-World Multiobjective) benchmark function collections.

Usage:
    from benchmarks import (
        classical,  # Classical benchmark functions
        cec         # CEC Real-World Multiobjective problems
    )

    # Classical functions
    f = classical.rosenbrock([1, 2])
    
    # CEC problems
    f, g, h = cec.pressure_vessal([1, 2, 3, 4])
"""

from .classical import __all__ as classical_functions, FUNCTION_CATEGORIES as classical_categories
from .cec import __all__ as cec_functions

__all__ = ["classical", "cec"]