from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from ..database.connection import get_db
from ..schemas.applications_request import ApplicationRequest
from ..schemas.applications_response import ApplicationResponse
from ..schemas.applications_update_request import ApplicationUpdateRequest
from ..services.applications import ApplicationService
from ..domain.exceptions import InvalidApplicationDate, ApplicationAlreadyExists, DatabaseError, ApplicationDoesNotExist

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

@router.patch("/{application_id}", status_code=status.HTTP_200_OK)
def edit_application(application_id: UUID, updated_data: ApplicationUpdateRequest, db: Session = Depends(get_db)):
    try:
        service = ApplicationService(db=db)
        service.edit_applications(updated_data, application_id)
        return {
            "message": "Candidatura atualizada com sucesso."
            }
    except ApplicationDoesNotExist as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
            )

    except InvalidApplicationDate as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=str(error)
            )

    except DatabaseError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
        )

@router.delete("/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_application(application_id: UUID, db: Session = Depends(get_db)):
    try:
        service = ApplicationService(db=db)
        service.delete_application(application_id)
    except ApplicationDoesNotExist as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
            )
    except DatabaseError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error)
            )