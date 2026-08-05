from ..domain.application_status import ApplicationStatus
from datetime import date
from pydantic import BaseModel

class Item(BaseModel):
    position: str
    company_name: str
    status: ApplicationStatus
    source: str | None = None
    applied_date: date