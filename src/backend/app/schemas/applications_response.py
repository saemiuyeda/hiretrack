from datetime import date
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from ..domain.application_status import ApplicationStatus

class ApplicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    position: str
    company_name: str
    status: ApplicationStatus
    source: str | None = None
    applied_date: date