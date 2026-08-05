from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.connection import get_db
from ..schemas.applications import Item
from ..services.applications import ApplicationService
from ..domain.exceptions import InvalidApplicationDate, ApplicationAlreadyExists, DatabaseError

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_application(item: Item, db: Session = Depends(get_db)):
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