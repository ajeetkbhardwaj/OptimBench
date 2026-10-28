"""Classical benchmark functions for optimization algorithms."""

from .ackley import ackley_1, ackley_2, ackley_3, ackley_4
from .adjiman import adjiman
from .alpine import alpine_1, alpine_2
from .bartels_conn import bartels_conn
from .beale import beale
from .bird import bird
from .bohachevsky import bohachevsky_1
from .bohachevsky import bohachevsky_2, bohachevsky_3
from .booth import booth
from .brent import brent
from .deckkers_aarts import deckkers_aarts
from .gramacy_lee import gramacy_lee
from .himmelblau import himmelblau
from .mccormick import mccormick
from .rosenbrock import rosenbrock
3 # We needed to import the functions that optimizes them
# Category mappings based on Julia attributes
FUNCTION_CATEGORIES = {
    "ackley_1": ["nd", "continuous", "differentiable", "non-convex", "multimodal", "separable"],
    "ackley_2": ["2d", "continuous", "differentiable", "convex", "unimodal", "non-separable"],
    "ackley_3": ["2d", "continuous", "differentiable", "non-convex", "multimodal", "non-separable"],
    "ackley_4": ["nd", "continuous", "differentiable", "non-convex", "multimodal", "non-separable"],
    "adjiman": ["2d", "continuous", "differentiable", "non-convex", "multimodal", "non-separable"],
    "alpine_1": ["nd", "continuous", "differentiable", "non-convex", "multimodal", "separable"],
    "alpine_2": ["nd", "continuous", "differentiable", "non-convex", "multimodal", "separable"],
    "bartels_conn": ["2d", "continuous", "non-differentiable", "non-convex", "multimodal", "non-separable"],
    "beale": ["2d", "continuous", "differentiable", "non-convex", "unimodal", "non-separable"],
    "bird": ["2d", "continuous", "differentiable", "non-convex", "multimodal", "non-separable"],
    "bohachevsky_1": ["2d", "continuous", "differentiable", "convex", "unimodal", "separable"],
    "bohachevsky_2": ["2d", "continuous", "differentiable", "non-convex", "multimodal", "non-separable"],
    "bohachevsky_3": ["2d", "continuous", "differentiable", "non-convex", "multimodal", "non-separable"],
    "booth": ["2d", "continuous", "differentiable", "convex", "unimodal", "non-separable"],
    "brent": ["2d", "continuous", "differentiable", "convex", "unimodal", "non-separable"],
    "deckkers_aarts": ["2d", "continuous", "differentiable", "non-convex", "multimodal", "non-separable"],
    "himmelblau": ["2d", "continuous", "differentiable", "non-convex", "multimodal", "separable"],
    "mccormick": ["2d", "continuous", "differentiable", "convex", "multimodal", "separable"],
    "rosenbrock": ["nd", "continuous", "differentiable", "non-convex", "multimodal", "non-separable"],
    "gramacy_lee": ["1d", "continuous", "differentiable", "non-convex", "multimodal", ""],
}

__all__ = list(FUNCTION_CATEGORIES.keys())