# System Architecture

## High-Level Components

1. Client App (iOS first)
2. Media Ingest Service
3. Quality Gate Service
4. Pose and Club Tracking Service
5. Swing Event Detection Service
6. Feature Extraction and Scoring Service
7. Feedback Generation Service
8. Overlay Rendering Engine (client)
9. Data Store and Analytics

## End-to-End Flow

1. User uploads or records video.
2. Ingest service normalizes media and extracts metadata.
3. Quality gate validates if analysis is reliable.
4. Tracking models produce time-series keypoints.
5. Event detector marks address, takeaway, top, transition, impact, finish.
6. Feature extractor computes biomechanical metrics at checkpoints.
7. Scoring engine maps metrics to findings and confidence.
8. Feedback generator creates prioritized guidance and draw commands.
9. Client renders overlays on video playback timeline.

## Suggested V1 Deployment Shape

- Mobile client: SwiftUI.
- Backend: Python or Node services behind REST API.
- Async jobs: queue-based analysis worker.
- Storage:
  - Object storage for videos.
  - Relational DB for metadata and results.
  - Optional vector/feature store for model experimentation.

## Service Boundaries

- Keep measurement logic deterministic and isolated.
- Keep natural-language explanation layer replaceable.
- Version all model and rule outputs.

## Reliability and Observability

- Per-step latency and failure metrics.
- Analysis trace IDs across services.
- Model confidence histograms.
- Drift monitoring for keypoint detection distributions.

## Security and Privacy

- Signed upload URLs.
- Encrypted storage at rest.
- Explicit retention policy and delete endpoint.
- Access control for coach/student sharing flows.
