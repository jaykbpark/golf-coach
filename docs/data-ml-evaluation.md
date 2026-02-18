# Data, Modeling, and Evaluation

## Data Strategy

Start with a coach-reviewed dataset, then scale through assisted labeling.

## Dataset Layers

1. Raw swing videos with consent and metadata.
2. Frame-level annotations:
   - Body keypoints
   - Club shaft and clubhead points
   - Event timestamps
3. Session-level labels:
   - Swing tendencies
   - Priority faults
   - Coach agreement notes

## Annotation Tooling Requirements

- Frame scrubbing with onion-skin overlays.
- Keypoint correction UI.
- Event marker editing.
- Side-by-side model output vs coach label.

## Model Stack (V1 to V2)

- V1:
  - Pose/keypoint model + deterministic feature/rule engine.
  - Limited ML used for view classification and event detection.
- V2:
  - Learned ranking/personalization layer on top of deterministic metrics.
  - Confidence calibration model using historical agreement data.

## Evaluation Framework

### Technical metrics

- Keypoint localization error.
- Event timing error (ms/frame offset).
- Metric stability across repeated uploads.
- Quality gate precision (block bad videos, pass usable ones).

### Coaching metrics

- Coach-model agreement by finding type.
- Precision and recall of high-priority fault detection.
- Recommendation usefulness rating.

### Product metrics

- Re-upload rate after failed gate.
- Improvement trend for tracked metrics over sessions.

## Offline and Online Validation

- Offline: labeled benchmark set per view mode and club class.
- Online: shadow evaluation and limited beta with coach audits.

## Drift and Re-Training

- Monitor distributions of keypoint confidence and derived metrics.
- Trigger retraining when drift exceeds threshold.
- Use versioned model registry and reproducible eval reports.
