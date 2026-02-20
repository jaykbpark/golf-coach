from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List, Literal, Optional
from uuid import uuid4

from pydantic import BaseModel, Field

AnalysisStatus = Literal["queued", "processing", "complete", "failed"]
ViewMode = Literal["face_on", "down_the_line"]
ClubClass = Literal["driver", "iron", "wedge"]
Handedness = Literal["right", "left"]
SkillBand = Literal["beginner", "mid", "advanced"]
ShotIntent = Literal["stock", "draw", "fade"]
GateCheckType = Literal["hard", "soft"]


class AnalysisCreateRequest(BaseModel):
    video_id: str = Field(min_length=1)
    view_mode: ViewMode
    club_class: Optional[ClubClass] = None
    handedness: Optional[Handedness] = None
    skill_band: Optional[SkillBand] = None
    shot_intent: Optional[ShotIntent] = None


class AnalysisRequestSnapshot(BaseModel):
    video_id: str
    view_mode: ViewMode
    club_class: Optional[ClubClass] = None
    handedness: Optional[Handedness] = None
    skill_band: Optional[SkillBand] = None
    shot_intent: Optional[ShotIntent] = None

    @classmethod
    def from_request(cls, request: AnalysisCreateRequest) -> "AnalysisRequestSnapshot":
        return cls(**request.model_dump())


class GateCheck(BaseModel):
    name: str
    type: GateCheckType
    value: Any
    threshold: str
    passed: bool
    code: Optional[str] = None


class QualityGateResult(BaseModel):
    passed: bool
    overall_score: float = Field(ge=0.0, le=1.0)
    checks: List[GateCheck] = Field(default_factory=list)
    reasons: List[str] = Field(default_factory=list)
    recapture_tips: List[str] = Field(default_factory=list)
    gate_version: str = "gate_v0.1.0"


class ErrorResult(BaseModel):
    code: str
    message: str


class AnalysisCreateResponse(BaseModel):
    api_version: Literal["v1"] = "v1"
    schema_version: str = "analysis_create_response.v1"
    analysis_id: str
    status: AnalysisStatus
    created_at: datetime


class AnalysisDetailResponse(BaseModel):
    api_version: Literal["v1"] = "v1"
    schema_version: str = "analysis_detail_response.v1"
    analysis_id: str
    status: AnalysisStatus
    created_at: datetime
    updated_at: datetime
    request: AnalysisRequestSnapshot
    quality_gate: Optional[QualityGateResult] = None
    model_versions: Dict[str, str] = Field(default_factory=dict)
    error: Optional[ErrorResult] = None

    @classmethod
    def queued_from_request(cls, request: AnalysisCreateRequest) -> "AnalysisDetailResponse":
        now = datetime.now(tz=timezone.utc)
        return cls(
            analysis_id=f"an_{uuid4().hex[:12]}",
            status="queued",
            created_at=now,
            updated_at=now,
            request=AnalysisRequestSnapshot.from_request(request),
        )
