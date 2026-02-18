# API and Storage Design

## API Style

- REST for V1 simplicity.
- Async analysis jobs with polling or webhook completion.

## Core Endpoints (V1)

- `POST /v1/videos/upload-url`
- `POST /v1/analyses`
- `GET /v1/analyses/{analysis_id}`
- `GET /v1/analyses/{analysis_id}/overlays`
- `GET /v1/sessions/{session_id}/history`
- `DELETE /v1/videos/{video_id}`

## Analysis Request Example

```json
{
  "video_id": "vid_123",
  "view_mode": "down_the_line",
  "club_class": "iron",
  "handedness": "right",
  "skill_band": "mid",
  "shot_intent": "stock"
}
```

## Analysis Result Shape (Concept)

```json
{
  "analysis_id": "an_123",
  "status": "complete",
  "quality_gate": {
    "passed": true,
    "score": 0.89,
    "warnings": ["minor_motion_blur"]
  },
  "model_versions": {
    "view_classifier": "1.2.0",
    "keypoint_model": "2.0.3",
    "event_model": "0.9.1",
    "rule_pack": "2026.02.0"
  },
  "findings": [],
  "summary": {
    "overall_confidence": "high",
    "top_priorities": ["shaft_plane_p6", "head_sway_impact"]
  }
}
```

## Storage Model

- `videos`
  - id, user_id, object_url, fps, resolution, duration, created_at
- `analyses`
  - id, video_id, status, view_mode, club_class, quality_score, created_at
- `analysis_findings`
  - id, analysis_id, finding_id, severity, confidence, payload_json
- `analysis_metrics`
  - analysis_id, metric_name, event_name, value, unit, confidence
- `analysis_overlays`
  - analysis_id, schema_version, overlay_json

## Versioning

- Include `schema_version` in all JSON payloads.
- Keep backward-compatible readers in client.

## Retention and Privacy

- User-controlled deletion.
- Configurable TTL for raw video retention.
- Separate derived metric retention from media retention.
