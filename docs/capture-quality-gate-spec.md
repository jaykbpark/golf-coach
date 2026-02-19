# Capture Quality Gate Spec (V0)

## Purpose

Define a strict, explainable gate that determines whether a swing video is reliable enough for downstream swing analysis.

If gate fails, no swing coaching feedback is shown.

## Scope

- Input video type: fixed-angle smartphone capture.
- Supported views:
  - `face_on`
  - `down_the_line`
- This is a pre-analysis quality decision, not biomechanical scoring.

## Inputs

- `video_id` (required)
- `view_mode` (required): `face_on | down_the_line`
- `club_class` (optional): `driver | iron | wedge`
- `handedness` (optional): `right | left`
- `device_metadata` (optional): model, OS, camera lens, capture fps

## Output Contract

```json
{
  "passed": true,
  "overall_score": 0.89,
  "checks": [
    {
      "name": "fps_min",
      "type": "hard",
      "value": 120,
      "threshold": ">=60",
      "pass": true
    }
  ],
  "reasons": [],
  "recapture_tips": [],
  "version": "gate_v0.1.0"
}
```

## Decision Rules

- `hard` checks: any failure results in gate failure.
- `soft` checks: do not fail gate by themselves, but reduce confidence and trigger warnings.

## Hard Checks (V0 Defaults)

1. `fps_min`
   - Rule: `fps >= 60`
2. `resolution_min`
   - Rule: `width >= 1280` and `height >= 720`
3. `duration_window`
   - Rule: `1.2s <= duration <= 6.0s`
4. `body_visible_ratio`
   - Rule: body landmarks visible in `>= 0.90` of sampled frames
5. `club_region_visible_ratio`
   - Rule: club proxy visibility in `>= 0.80` of sampled frames
6. `camera_tilt_max`
   - Rule: absolute horizon tilt `<= 6` degrees
7. `view_mode_confidence`
   - Rule: classifier confidence `>= 0.80` for selected `view_mode`

## Soft Checks (V0 Defaults)

1. `low_light_warning`
2. `motion_blur_warning`
3. `background_clutter_warning`

Soft check failures should appear in `reasons` and `recapture_tips`.

## Error and Warning Taxonomy

Use stable codes for UI and analytics.

- `ERR_FPS_TOO_LOW`
- `ERR_RESOLUTION_TOO_LOW`
- `ERR_DURATION_OUT_OF_RANGE`
- `ERR_BODY_OUT_OF_FRAME`
- `ERR_CLUB_NOT_VISIBLE`
- `ERR_CAMERA_TILTED`
- `ERR_VIEW_MODE_MISMATCH`
- `WARN_LOW_LIGHT`
- `WARN_MOTION_BLUR`
- `WARN_BACKGROUND_CLUTTER`

## Recapture Guidance Mapping

Each error must map to a specific instruction:

- `ERR_BODY_OUT_OF_FRAME` -> "Move camera back until full body and club are visible through finish."
- `ERR_CAMERA_TILTED` -> "Level the phone horizon before recording."
- `ERR_FPS_TOO_LOW` -> "Use 60fps or 120fps capture mode."

## Suggested Measurement Pipeline

1. Read media metadata (fps, resolution, duration).
2. Sample frames at fixed interval.
3. Run body landmark detection on sampled frames.
4. Estimate horizon/camera tilt from scene or body reference.
5. Estimate club proxy visibility.
6. Run view-mode classifier and compare with requested mode.
7. Compute pass/fail and emit structured result.

## Threshold Tuning Strategy

- Start strict to minimize false-pass.
- Build a labeled set of at least 150 videos.
- Weekly review:
  - false-pass rate
  - false-fail rate
  - top failing checks
- Tune thresholds only with validation data and version bump.

## Versioning and Auditability

- Include gate version in every result (`version`).
- Store raw check values and thresholds used at evaluation time.
- Never overwrite historical gate outputs; append new records for re-runs.

## Non-Goals (V0)

- Estimating true 3D camera pose.
- Estimating clubface orientation at impact.
- Real-time on-device high-fidelity gate scoring.
