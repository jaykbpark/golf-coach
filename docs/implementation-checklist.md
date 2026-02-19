# Implementation Checklist

This checklist turns the current product and quality-gate spec into executable engineering work.

## Phase 1: Contracts and Foundations

- [ ] Finalize `view_mode` definitions and terminology.
- [ ] Freeze V0 hard/soft gate checks and default thresholds.
- [ ] Define stable error/warning codes and recapture messages.
- [ ] Finalize API payload schemas for analysis status and gate output.
- [ ] Add schema version fields to all gate and analysis responses.

## Phase 2: iOS Capture and Playback

- [ ] Build capture mode picker (`face_on`, `down_the_line`).
- [ ] Implement camera capture with 60/120fps target using `AVFoundation`.
- [ ] Add live framing overlay guides per view mode.
- [ ] Add pre-upload local precheck:
  - [ ] device fps capability
  - [ ] orientation/horizon approximation
  - [ ] body-in-frame approximation
- [ ] Build upload flow with resumable or retry-safe behavior.
- [ ] Build playback UI:
  - [ ] frame scrubbing
  - [ ] slow-motion controls
  - [ ] event marker timeline placeholders

## Phase 3: Backend Quality Gate Service

- [ ] Create `POST /v1/analyses` endpoint (queue job and return `analysis_id`).
- [ ] Create `GET /v1/analyses/{analysis_id}` endpoint (status + gate details).
- [ ] Implement media metadata extractor:
  - [ ] fps
  - [ ] resolution
  - [ ] duration
- [ ] Implement frame sampler for gate analysis.
- [ ] Implement body landmark visibility scoring.
- [ ] Implement camera tilt scoring.
- [ ] Implement view-mode classifier and confidence output.
- [ ] Implement club proxy visibility scoring.
- [ ] Implement decision engine:
  - [ ] evaluate hard checks
  - [ ] evaluate soft checks
  - [ ] map failures to error codes and recapture tips

## Phase 4: Data Model and Persistence

- [ ] Create tables:
  - [ ] `videos`
  - [ ] `analyses`
  - [ ] `analysis_checks`
  - [ ] `analysis_quality_gate_results`
- [ ] Persist raw check values and thresholds used.
- [ ] Persist gate version and model/rule versions.
- [ ] Add analysis trace ID to all logs and DB records.
- [ ] Add retention and deletion policy support for raw media.

## Phase 5: Internal Tooling and Evaluation

- [ ] Build internal review page for each analyzed video:
  - [ ] view video
  - [ ] view checks and raw values
  - [ ] assign human label (`usable` / `not_usable`)
- [ ] Label first 150-200 videos.
- [ ] Compute gate confusion matrix:
  - [ ] true pass
  - [ ] false pass
  - [ ] true fail
  - [ ] false fail
- [ ] Tune thresholds to minimize false-pass first.
- [ ] Publish weekly threshold tuning changelog.

## Phase 6: Overlay and Annotation Baseline

- [ ] Implement manual drawing tools on playback:
  - [ ] line
  - [ ] circle
  - [ ] label text
- [ ] Store overlays as normalized coordinates.
- [ ] Add import path for server-provided `draw_commands`.
- [ ] Ensure overlays can be anchored to timeline events.

## Phase 7: Release Gates for V1

- [ ] Gate false-pass rate below agreed target.
- [ ] Recapture guidance appears for 100% hard failures.
- [ ] No analysis feedback shown on failed gate.
- [ ] P95 gate processing latency meets target.
- [ ] Observability dashboards available for:
  - [ ] pass/fail trends
  - [ ] failure-code distribution
  - [ ] device model breakdown

## Recommended Ownership Split

- iOS:
  - capture UX, playback, manual overlays, upload client.
- Backend:
  - gate pipeline, job processing, APIs, storage.
- Data/ML:
  - landmark/view models, threshold tuning, drift monitoring.
- Product/Coaching:
  - recapture copy quality, fail-state UX, acceptance criteria.

## First Sprint (Suggested)

- [ ] Implement API skeleton for analysis create/status.
- [ ] Implement metadata-only hard checks (`fps`, `resolution`, `duration`).
- [ ] Ship basic iOS capture/upload/playback path.
- [ ] Return real fail reasons for metadata failures.
- [ ] Instrument logs and dashboard for gate outcomes.
