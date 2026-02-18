# Capture and Calibration Spec

## Objective

Define input standards that protect measurement accuracy for fixed-angle swing analysis.

## Supported Capture Modes

- `face_on` (camera facing golfer chest-on).
- `down_the_line` (camera behind hands target-line view).

User must select mode before recording or upload.

## Recommended Capture Requirements

- Frame rate: 120 fps preferred, 60 fps minimum.
- Resolution: 1080p preferred, 720p minimum.
- Entire body and club visible from address to finish.
- Stable tripod or fixed support.
- Neutral lighting with minimal motion blur.

## Positioning Guide (In-App Overlay)

- Show silhouette template and live framing hints.
- Enforce horizon level within tolerance.
- Enforce camera height range by mode.
- Enforce estimated distance range so keypoints are not too small.

## Quality Gate Checks

Analysis runs only when all hard checks pass.

### Hard checks

- View classification confidence above threshold.
- Full body visibility for required swing segment frames.
- Club visibility ratio above threshold.
- FPS and duration minimums met.
- Camera tilt below max degree threshold.

### Soft checks

- Background clutter score.
- Lighting score.
- Potential occlusion warnings.

Soft checks reduce confidence but do not always block analysis.

## Calibration

Two-level approach:

- Level 1 (default): auto-scale from body landmarks and club length priors.
- Level 2 (optional): user places known-length reference object (alignment stick/club) in first frame.

Calibration metadata is stored with analysis for reproducibility.

## Failure UX

If gate fails, return specific reasons and recapture guidance.

Examples:

- "Camera is too low for down-the-line analysis."
- "Clubhead is out of frame during transition."
- "Frame rate appears below 60 fps."

## Why this matters

Capture standards are the strongest lever for trustworthy feedback. A strict gate prevents confident-sounding but incorrect coaching.
