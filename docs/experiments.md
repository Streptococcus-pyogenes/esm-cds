# Experiments Plan and Results (v0)

This document describes the experimental plan for the v0 experiments of ESM CDS and provides placeholders for results. The objective of v0 is to compare different downsampling operators and assess training stability and alignment.

## Experimental Setup

- **Teacher model:** Vanilla ESM‑C without downsampling.
- **Student models:** ESM‑C with downsampling modules using mean pooling, gated merge (GM), or local attention pooling (LAP).
- **Dataset:** Swiss‑Prot with length filter \(64 ≤ L ≤ 2048\).
- **Batching:** Length‑bucket batching; long sequences are weighted more heavily.
- **Token interface:** N = 64 residue tokens (+ CLS/EOS) in v0.
- **Training:** Distillation from the teacher to each student with cosine distance loss. Two phases: early phase focusing on intermediate checkpoints; late phase focusing on final representation alignment.

## Metrics

- **Training stability:** Monitor loss curves and gradient norms.
- **Distillation alignment:** Cosine similarity between student and teacher representations at checkpoints and final layer.
- **Length‑wise breakdown:** Evaluate performance across sequence length buckets (64–128, 128–256, 256–512, 512‑1024, 1024‑2048).
- **Comparison:** Compare mean, GM, and LAP operators under the same training conditions.

## Results Placeholder

Provide tables and plots summarising the metrics for each operator. Include:

- A table of cosine similarity scores per length bucket.
- Plots of loss curves showing training stability.
- Observations on which operator performs best or exhibits better stability (leave as TODO until experiments complete).

**TODO:** Insert experimental results once available.
