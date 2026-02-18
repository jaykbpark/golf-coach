# Measurement and Feedback Framework

## Principle

Feedback must be grounded in measurable signals extracted from video, not generic tips.

## Swing Timeline Events

- `address`
- `takeaway_p2`
- `lead_arm_parallel_p3`
- `top_p4`
- `delivery_p6`
- `impact`
- `finish_p8`

Event uncertainty is tracked per timestamp.

## Metric Families

- Setup metrics: posture, spine tilt, ball position proxies.
- Plane metrics: shaft plane, hand path depth, club pitch.
- Rotation metrics: pelvis and thorax rotation progression.
- Translation metrics: head sway, pelvis shift.
- Timing metrics: sequence and tempo proxies.

## Context Inputs

- View mode (`face_on` or `down_the_line`)
- Club class (driver, iron, wedge)
- Handedness
- Skill band (optional)
- Shot intent (stock, draw, fade; optional)

Context selects metric ranges and feedback wording.

## Scoring Model

For each metric:

- Compute normalized deviation from context range.
- Weight by metric reliability and event confidence.
- Convert to severity class:
  - `ok`
  - `watch`
  - `priority_fix`

Overall session score is a weighted aggregate with uncertainty penalties.

## Confidence Model

Confidence is derived from:

- Capture quality score
- Landmark visibility stability
- Event detection confidence
- Known metric reliability for selected view mode

Output confidence bands:

- `high`
- `medium`
- `low`

Low confidence findings should be visually de-emphasized.

## Feedback Object Schema (Concept)

```json
{
  "finding_id": "shaft_plane_p6",
  "severity": "priority_fix",
  "confidence": "high",
  "explanation": "Shaft is above target delivery window at P6, often linked to steep attack pattern.",
  "impact": "Can increase pull/slice pattern risk.",
  "recommendation": "Feel trail elbow move in front of hip before delivery.",
  "draw_commands": [
    { "type": "line", "from": [0.34, 0.62], "to": [0.59, 0.41], "label": "Target delivery line" },
    { "type": "line", "from": [0.36, 0.66], "to": [0.60, 0.31], "label": "Current shaft" },
    { "type": "circle", "center": [0.37, 0.67], "radius": 0.03, "label": "Hands at P6" }
  ]
}
```

Coordinates are normalized in video frame space.

## Guardrails

- Never claim cause with certainty from a single metric.
- Avoid prescriptions when confidence is low.
- Prefer "associated with" phrasing unless evidence is high.
