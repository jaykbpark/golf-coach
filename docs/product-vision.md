# Product Vision

## Problem

Most golfers can record swings, but cannot reliably self-diagnose what caused a miss. Existing apps often provide generic advice or inconsistent measurements.

## Vision

Build a swing analysis platform that gives feedback users can trust because each insight is tied to measurable checkpoints, confidence scores, and clear visual overlays.

## Product Goals

- High-confidence feedback from fixed-angle smartphone video.
- Fast user loop: capture, analyze, understand, retry.
- Human-readable and machine-readable feedback.
- Clear distinction between high-confidence findings and speculative suggestions.

## Non-Goals (V1)

- 3D reconstruction from a single camera.
- Full clubface orientation at impact from low-fps video.
- Real-time coaching during the swing.

## Core Personas

- Self-improving amateur golfer.
- Golf coach reviewing student uploads.
- Content creator sharing before/after swing analysis.

## Core User Flows

1. User records or uploads swing video.
2. System validates capture quality.
3. System detects swing events and computes measurements.
4. System returns prioritized feedback with overlay drawings.
5. User compares attempts over time.

## Success Metrics

- Analysis completion rate after upload.
- Percent of videos passing quality gate.
- Coach agreement rate with feedback labels.
- User-reported usefulness of feedback.
- Repeat session rate within 7 days.
