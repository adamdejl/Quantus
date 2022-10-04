"""This module contains constants and simple methods to retreive the available metrics, perturbation-,
similarity-, normalisation- functions and explanation methods in Quantus."""

from typing import List, Dict
from ..metrics import *
from .normalise_func import *
from .perturb_func import *
from .similarity_func import *
from .loss_func import *


AVAILABLE_METRICS = {
    "Faithfulness": {
        "Faithfulness Correlation": FaithfulnessCorrelation,
        "Faithfulness Estimate": FaithfulnessEstimate,
        "Pixel-Flipping": PixelFlipping,
        "Region Segmentation": RegionPerturbation,
        "Monotonicity-Arya": Monotonicity,
        "Monotonicity-Nguyen": MonotonicityCorrelation,
        "Selectivity": Selectivity,
        "SensitivityN": SensitivityN,
        "IROF": IROF,
        "ROAD": ROAD,
        "Infidelity": Infidelity,
        "Sufficiency": Sufficiency,
    },
    "Robustness": {
        "Continuity Test": Continuity,
        "Local Lipschitz Estimate": LocalLipschitzEstimate,
        "Max-Sensitivity": MaxSensitivity,
        "Avg-Sensitivity": AvgSensitivity,
        "Consistency": Consistency,
    },
    "Localisation": {
        "Pointing Game": PointingGame,
        "Top-K Intersection": TopKIntersection,
        "Relevance Mass Accuracy": RelevanceMassAccuracy,
        "Relevance Rank Accuracy": RelevanceRankAccuracy,
        "Attribution Localisation ": AttributionLocalisation,
        "AUC": AUC,
        "Focus": Focus,
    },
    "Complexity": {
        "Sparseness": Sparseness,
        "Complexity": Complexity,
        "Effective Complexity": EffectiveComplexity,
    },
    "Randomisation": {
        "Model Parameter Randomisation": ModelParameterRandomisation,
        "Random Logit": RandomLogit,
    },
    "Axiomatic": {
        "Completeness": Completeness,
        "NonSensitivity": NonSensitivity,
        "InputInvariance": InputInvariance,
    },
}


AVAILABLE_PERTURBATION_FUNCTIONS = {
    "baseline_replacement_by_indices": baseline_replacement_by_indices,
    "baseline_replacement_by_shift": baseline_replacement_by_shift,
    "baseline_replacement_by_blur": baseline_replacement_by_blur,
    "gaussian_noise": gaussian_noise,
    "uniform_noise": uniform_noise,
    "rotation": rotation,
    "translation_x_direction": translation_x_direction,
    "translation_y_direction": translation_y_direction,
    "no_perturbation": no_perturbation,
    "noisy_linear_imputation": noisy_linear_imputation,
}


AVAILABLE_SIMILARITY_FUNCTIONS = {
    "correlation_spearman": correlation_spearman,
    "correlation_pearson": correlation_pearson,
    "correlation_kendall_tau": correlation_kendall_tau,
    "distance_euclidean": distance_euclidean,
    "distance_manhattan": distance_manhattan,
    "distance_chebyshev": distance_chebyshev,
    "lipschitz_constant": lipschitz_constant,
    "abs_difference": abs_difference,
    "difference": difference,
    "cosine": cosine,
    "ssim": ssim,
    "mse": mse,
}

AVAILABLE_NORMALISATION_FUNCTIONS = {
    "normalise_by_negative": normalise_by_negative,
    "normalise_by_max": normalise_by_max,
    "denormalise": denormalise,
}


AVAILABLE_XAI_METHODS = {
    "Gradient",
    "Saliency",
    "GradientShap",
    "IntegratedGradients",
    "InputXGradient",
    "Occlusion",
    "FeatureAblation",
    "GradCam",
    "Control Var. Sobel Filter",
    "Control Var. Constant",
    "Control Var. Random Uniform",
}


def available_categories() -> List[str]:
    """
    Retrieve the available metric categories in Quantus.

    Returns
    -------
        List[str]: With the available metric categories in Quantus.
    """
    return [c for c in AVAILABLE_METRICS.keys()]


def available_metrics() -> Dict[str, str]:
    """
    Retrieve the available metrics in Quantus.

    Returns
    -------
        Dict[str, str]: With the available metrics, under each category in Quantus.
    """
    return {c: list(metrics.keys()) for c, metrics in AVAILABLE_METRICS.items()}


def available_methods() -> List[str]:
    """
    Retrieve the available explanation methods in Quantus.

    Returns
    -------
        List[str]: With the available explanation methods in Quantus.
    """
    return [c for c in AVAILABLE_XAI_METHODS.keys()]


def available_perturbation_functions() -> List[str]:
    """
    Retrieve the available perturbation functions in Quantus.

    Returns
    -------
        List[str]: With the available perturbation functions in Quantus.
    """
    return [c for c in AVAILABLE_PERTURBATION_FUNCTIONS.keys()]


def available_similarity_functions() -> List[str]:
    """
    Retrieve the available similarity functions in Quantus.

    Returns
    -------
        List[str]: With the available similarity functions in Quantus.
    """
    return [c for c in AVAILABLE_SIMILARITY_FUNCTIONS.keys()]


def available_normalisation_functions() -> List[str]:
    """
    Retrieve the available normalisation functions in Quantus.

    Returns
    -------
        List[str]: With the available normalisation functions in Quantus.
    """
    return [c for c in AVAILABLE_NORMALISATION_FUNCTIONS.keys()]
