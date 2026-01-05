"""
Mean pooling downsampling for ESM-CDS.

This module implements a simple non-trainable mean pooling operator that reduces pairs of residue tokens by taking their average.
"""

from __future__ import annotations

from typing import Any


def mean_pooling(x: Any, kernel_size: int = 2) -> Any:
    """Apply mean pooling to reduce token length by kernel_size.

    Args:
        x: Input tensor of shape (..., L, d).
        kernel_size: Pooling width (default 2).

    Returns:
        Tensor with reduced length.
    """
    # TODO: Implement mean pooling (e.g., by reshaping and averaging)
    raise NotImplementedError
