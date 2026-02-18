# Design Decisions

This file captures key decisions, why they were made, and what tradeoffs they introduce.

## 1. Build for two explicit camera modes

- Decision: Support `face_on` and `down_the_line` as separate analysis modes.
- Why: Checkpoints and geometry assumptions differ by viewpoint.
- Tradeoff: More implementation complexity, but significantly higher accuracy and fewer false positives.

## 2. Reject low-quality captures instead of guessing

- Decision: Introduce a quality gate before analysis.
- Why: Bad framing, camera tilt, low fps, and occlusion produce misleading feedback.
- Tradeoff: Short-term user friction, long-term trust and retention gains.

## 3. Measure first, coach second

- Decision: Separate measurement pipeline from language feedback generation.
- Why: Explainable, testable outputs are required for credibility.
- Tradeoff: Slower initial UX polish, stronger correctness foundation.

## 4. Use checkpoint ranges, not universal perfect angles

- Decision: Evaluate against ranges by context (club, skill level, shot intent).
- Why: Swing variations can all be functional; hard thresholds over-penalize valid patterns.
- Tradeoff: Requires more metadata and calibration of ranges.

## 5. Return confidence with each finding

- Decision: Every finding includes confidence and evidence summary.
- Why: Users and coaches need to know what is reliable.
- Tradeoff: Additional model calibration and QA effort.

## 6. Keep overlay rendering as structured commands

- Decision: Feedback output includes machine-readable draw primitives.
- Why: Enables consistent UI rendering and future LLM integration.
- Tradeoff: Requires strict schema versioning.

## 7. Start with rule-based scoring, layer ML ranking later

- Decision: V1 scoring is deterministic from measured features; ML personalizes severity and prioritization later.
- Why: Faster path to auditable behavior.
- Tradeoff: Early feedback can feel rigid until personalization matures.

## 8. Human-in-the-loop data strategy

- Decision: Coaches review and correct model outputs for training data.
- Why: Biomechanics labels need expert signal.
- Tradeoff: Labeling cost and tooling work.

## 9. Version everything

- Decision: Persist model version, rule pack version, and overlay schema version with every analysis.
- Why: Required for reproducibility and regression debugging.
- Tradeoff: More metadata and migration handling.

## 10. Optimize for reliability before real-time

- Decision: Batch analysis first, near-real-time later.
- Why: Accuracy and explainability are priority over latency in early stages.
- Tradeoff: Less immediate feedback in V1, better technical foundation.
