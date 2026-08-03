import enum
import uuid
from datetime import datetime, date
from sqlalchemy import Uuid, DateTime, Enum, Date, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class ApplicationStatus(enum.Enum):
    APPLICATION = "Inscrição"
    SCREENING = "Triagem"
    RH_INTERVIEW = "Entrevista RH"
    TECHNICAL_INTERVIEW = "Entrevista Técnica"
    OFFER = "Proposta"
    HIRED = "Contratada"
    REJECTED = "Rejeitada"
    CANCELLED = "Cancelada"

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key= True, default=uuid.uuid4)
    registration_date: Mapped[datetime] = mapped_column(
        DateTime(timezone= True),
        server_default= func.now(),
        nullable= False
        )
    position: Mapped[str] = mapped_column(nullable= False)
    company_name: Mapped[str] = mapped_column(nullable= False)
    status: Mapped[ApplicationStatus] = mapped_column(
        Enum(ApplicationStatus), 
        nullable= False
        )
    source: Mapped[str | None]
    applied_date: Mapped[date] = mapped_column(
        Date,
        nullable= False
        )