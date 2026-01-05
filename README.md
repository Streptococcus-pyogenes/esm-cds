# ESM-CDS

ESM-CDS is a protein encoder built on top of ESM-C that progressively downsamples residue tokens into a fixed-length interface (N=64 in v0). It provides a length-invariant residue token interface and progressive downsampling inside the transformer. Designed as an encoder for Prot2Text.

## A. Title & Scope

ESM-CDS is a protein encoder built on top of ESM-C that progressively downsamples residue tokens into a fixed-length interface (N=64 in v0). It provides a length-invariant residue token interface and progressive downsampling inside the transformer. Designed as an encoder for Prot2Text.

## B. Problem Statement

Residue-level tokenization in transformer-based protein models leads to quadratic computational cost. Many downstream tasks do not require full residue-level resolution. Multimodal and LLM-style models need fixed-length token interfaces. These challenges motivate the design of ESM ‑CDS.

## C. Core Idea

Inside the transformer, residue tokens are progressively reduced while [CLS] and [EOS] tokens are preserved, until only N tokens remain, producing a fixed-length interface.

## D. Method: Progressive Token Downsampling

### D.1 Token Handling

- Input: [CLS] + residues + [EOS]
- Downsample residues only
- CLS/EOS always carried

### D.2 Schedule

- Every 4 transformer layers
- Residue length halves
- Stop when length ≤ N
- v0: non-overlap only

### D.3 Downsampling Operators

| Method | Trainable | Context | v0 Role |
| --- | --- | --- | --- |
| Mean Pooling | No | Local (pair) | Baseline |
| Gated Merge (GM) | Yes | Local (pair) | Learned merge |
| Local Attention Pooling (LAP) | Yes | Local (pair) | Learned pooling |

## E. Training: Distillation

- **Teacher:** vanilla ESM-C (no downsampling)
- **Student:** ESM-C + downsampling modules
- **Targets:**
  - CLS-to-CLS alignment
  - Residue token alignment after resolution matching
  - Intermediate checkpoints only immediately after downsampling layers
- **Loss:**
  - Cosine distance (primary)
  - Composite loss (no weights specified)

## F. Data (v0 ONLY)

- **Dataset:** Swiss-Prot
- **Length filter:** 64 ≤ L ≤ 2048
- **No sampling**
- Long sequences are weighted more heavily
- Length-bucket batching

## G. Experiments (PLAN, NOT RESULTS)

- Stability analysis
- Distillation alignment
- Length-wise breakdown
- **Comparison set:**
  - Mean vs GM vs LAP
  - Teacher is not a competitor.

## H. Roadmap

- [ ] v0: Swiss-Prot + ESM-C 300M (N = 64)
- [ ] v1: UniRef50 + ESM-C 600M (winner only)
- [ ] N = 256 interface
- [ ] Prot2Text integration

## I. Relationship to Prot2Text

ESM‑CDS provides the encoder for Prot2Text. Prot2Text is developed in a separate repository.

## J. Citation

TODO
