from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from app.schemas.analysis import (
    AnalysisCreateRequest,
    AnalysisCreateResponse,
    AnalysisDetailResponse,
)

router = APIRouter(prefix="/analyses", tags=["analyses"])

# Temporary in-memory store until DB persistence is wired.
ANALYSIS_STORE: dict[str, AnalysisDetailResponse] = {}


@router.post("", response_model=AnalysisCreateResponse, status_code=status.HTTP_202_ACCEPTED)
def create_analysis(payload: AnalysisCreateRequest) -> AnalysisCreateResponse:
    analysis = AnalysisDetailResponse.queued_from_request(payload)
    ANALYSIS_STORE[analysis.analysis_id] = analysis
    return AnalysisCreateResponse(
        analysis_id=analysis.analysis_id,
        status=analysis.status,
        created_at=analysis.created_at,
    )


@router.get("/{analysis_id}", response_model=AnalysisDetailResponse)
def get_analysis(analysis_id: str) -> AnalysisDetailResponse:
    analysis = ANALYSIS_STORE.get(analysis_id)
    if analysis is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": "ANALYSIS_NOT_FOUND", "message": "Analysis id was not found"},
        )
    return analysis
