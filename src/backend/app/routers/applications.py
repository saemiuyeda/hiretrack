from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.connection import get_db
from ..schemas.applications_request import ApplicationRequest
from ..schemas.applications_response import ApplicationResponse
from ..services.applications import ApplicationService
from ..domain.exceptions import InvalidApplicationDate, ApplicationAlreadyExists, DatabaseError

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_application(item: ApplicationRequest, db: Session = Depends(get_db)):
    try:
        service = ApplicationService(db=db)
        new_application = service.create_application(application_data=item)
        return new_application
    except InvalidApplicationDate as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail= str(error)
            )
    
    except ApplicationAlreadyExists as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail=str(error)
            )
    
    except DatabaseError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
        )

@router.get("/", status_code=status.HTTP_200_OK)
def list_applications(db: Session = Depends(get_db)) -> list[ApplicationResponse]:
    service = ApplicationService(db=db)
    application_list = service.list_applications()
    applications = []
    for application in application_list:
        application_response = ApplicationResponse.model_validate(application)
        applications.append(application_response)
    return applications