# Roadmap

## Phase 0: Foundations (2-4 weeks)

- Finalize capture standards and quality gate requirements.
- Define metric dictionary and context taxonomy.
- Build docs-backed API contracts and data schemas.

## Phase 1: MVP Analyzer (6-10 weeks)

- iOS capture/upload and playback UI.
- Manual drawing tools (line, circle, label).
- Video quality gate with recapture messaging.
- Basic keypoint tracking and event detection.
- Deterministic scoring for 5-8 high-confidence findings.
- Session history and before/after comparison.

## Phase 2: Coach-Grade Iteration (8-12 weeks)

- Coach review console for annotation correction.
- Expanded metric coverage by view mode and club class.
- Confidence calibration and finding prioritization improvements.
- Better overlays with frame-anchored event markers.

## Phase 3: Personalization and Scale

- Personalized benchmark ranges per user trend.
- ML ranking for recommendation ordering.
- Team/coach accounts, sharing, and lesson workflows.

## Release Gates

- Minimum coach agreement target reached.
- Quality gate false-pass rate below threshold.
- No critical regressions in event detection timing.

## Known Risks

- Clubhead occlusion in poor lighting.
- Device fps inconsistency across phone models.
- Overfitting to narrow swing populations.

## Risk Mitigations

- Strict capture gate and explainable failure states.
- Device-aware calibration and fallback confidence.
- Diverse data collection and periodic benchmark refresh.
