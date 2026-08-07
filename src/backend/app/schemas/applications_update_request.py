from pydantic import BaseModel
from typing import Optional
from datetime import date
from ..domain.application_status import ApplicationStatus

class ApplicationUpdateRequest(BaseModel):
    position: Optional[str] = None
    company_name: Optional[str] = None
    status: Optional[ApplicationStatus] = None
    source: Optional[str] = None
    applied_date: Optional[date] = None