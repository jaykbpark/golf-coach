# API v1 Contract

This document is the canonical contract for the first backend API slice.

## Base

- Prefix: `/v1`
- Content type: `application/json`
- Time format: ISO-8601 UTC

## Endpoint: Create Analysis

- Method: `POST`
- Path: `/v1/analyses`
- Purpose: Create an analysis job and return queued status.

### Request Body

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

### Response (202 Accepted)

```json
{
  "api_version": "v1",
  "schema_version": "analysis_create_response.v1",
  "analysis_id": "an_a1b2c3d4e5f6",
  "status": "queued",
  "created_at": "2026-02-20T20:11:35.214000Z"
}
```

## Endpoint: Get Analysis

- Method: `GET`
- Path: `/v1/analyses/{analysis_id}`
- Purpose: Retrieve current analysis state and result payload.

### Response (200 OK, queued example)

```json
{
  "api_version": "v1",
  "schema_version": "analysis_detail_response.v1",
  "analysis_id": "an_a1b2c3d4e5f6",
  "status": "queued",
  "created_at": "2026-02-20T20:11:35.214000Z",
  "updated_at": "2026-02-20T20:11:35.214000Z",
  "request": {
    "video_id": "vid_123",
    "view_mode": "down_the_line",
    "club_class": "iron",
    "handedness": "right",
    "skill_band": "mid",
    "shot_intent": "stock"
  },
  "quality_gate": null,
  "model_versions": {},
  "error": null
}
```

### Response (404 Not Found)

```json
{
  "detail": {
    "code": "ANALYSIS_NOT_FOUND",
    "message": "Analysis id was not found"
  }
}
```

## Enums

- `status`: `queued | processing | complete | failed`
- `view_mode`: `face_on | down_the_line`
- `club_class`: `driver | iron | wedge`
- `handedness`: `right | left`
- `skill_band`: `beginner | mid | advanced`
- `shot_intent`: `stock | draw | fade`

## Versioning Rules

- URL version is explicit in path prefix (`/v1`).
- Response includes `api_version` and `schema_version`.
- Backward-incompatible changes require `/v2`.

## Current Implementation Scope

- Job creation and retrieval are implemented as stubs.
- Storage is currently in-memory.
- Queue, DB persistence, and real quality-gate computation are pending.
