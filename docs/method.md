# Method: Progressive Token Downsampling

This document elaborates on the method used by ESM-CDS to progressively downsample residue tokens into a fixed length interface.

## Token Handling

- Input sequence includes `[CLS]`, residue tokens, and `[EOS]`.
- Only residue tokens are downsampled. `[CLS]` and `[EOS]` are preserved and propagated unchanged.
- Downsampling reduces the number of residue tokens, but the semantic information is preserved.

## Schedule

- Downsampling occurs every 4 transformer layers.
- At each downsampling point, the number of residue tokens is halved.
- The process stops when the number of residue tokens is less than or equal to the target number `N`.
- In version v0, the downsampling is non-overlapping (pairs of adjacent tokens are merged without overlap).

## Downsampling Operators

We consider three operators for downsampling, each operating on pairs of tokens:

| Operator | Description | Trainable |
| --- | --- | --- |
| Mean Pooling | A simple average of two adjacent tokens. | No |
| Gated Merge (GM) | A learnable merge where a small MLP predicts a scalar gate to combine tokens. | Yes |
| Local Attention Pooling (LAP) | A learnable attention mechanism that computes a weighted combination of two tokens. | Yes |

Each operator produces a sequence half the length of the input residue tokens. `[CLS]` and `[EOS]` are concatenated appropriately.

## Implementation Notes

- The operators are implemented in the `esm_cds/downsampling` package.
- The model wrapper (`esm_cds/model.py`) orchestrates the downsampling schedule inside the transformer.
- This file focuses on describing the method conceptually; implementation details are marked as TODO in the code.
