"""Local attention pooling operator for ESM-CDS (placeholder).

This module implements a local attention pooling operator for downsampling
residue tokens. The implementation is a placeholder; it should
compute a learned pooling over pairs of tokens using a lightweight
attention mechanism. This will be implemented in future work.
"""

def local_attn_pooling(hidden_states):
    """Perform local attention pooling on pairs of tokens.

    Args:
        hidden_states: Tensor of shape (B, L, D), where L is the
            number of residue tokens.

    Returns:
        Tensor of shape (B, L/2, D) after pooling.
    """
    raise NotImplementedError("Local attention pooling operator is not yet implemented.")
