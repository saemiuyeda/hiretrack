from datetime import date
from uuid import UUID
from sqlalchemy.sql import exists, select
from sqlalchemy.orm import Session
from ..schemas.applications_request import ApplicationRequest
from ..schemas.applications_update_request import ApplicationUpdateRequest
from ..models.application import Application
from ..domain.exceptions import InvalidApplicationDate, ApplicationAlreadyExists, DatabaseError, ApplicationDoesNotExist

class ApplicationService():
    def __init__(self, db: Session):
         self.db = db

    def create_application(self, application_data: ApplicationRequest):
        if application_data.applied_date > date.today():
            raise InvalidApplicationDate("The application date cannot be in the future.")

        application_exists = self.db.query(
            exists().where((Application.position == application_data.position) & (Application.company_name == application_data.company_name))
            ).scalar()
        
        if application_exists:
            raise ApplicationAlreadyExists("This application already exists")

        new_application = Application(**application_data.model_dump())

        try:
            self.db.add(new_application)
            self.db.commit()
            self.db.refresh(new_application)
            return new_application
        except Exception as exception:
            self.db.rollback()
            raise DatabaseError(f"Error saving to the database: {str(exception)}")

    def list_applications(self) -> list[Application]:
        applications_query = select(Application)

        applications_list = self.db.scalars(applications_query).all()
        return applications_list

    def edit_applications(self, application_uptade_data: ApplicationUpdateRequest, application_id: UUID):
        application_query = self.db.query(Application).filter(Application.id == application_id).first()
        update_data = application_uptade_data.model_dump(exclude_unset= True)

        if not application_query:
            raise ApplicationDoesNotExist("This application does not exist")

        if "applied_date" in update_data:
            if application_uptade_data.applied_date > date.today():
                raise InvalidApplicationDate("The application date cannot be in the future.")

        for key, value in update_data.items():
            setattr(application_query, key, value)

        try:
            self.db.commit()
            return True
        except Exception as exception:
            self.db.rollback()
            raise DatabaseError(f"Error saving to the database: {str(exception)}")

    def delete_application(self, application_id: UUID):
        application_query = self.db.query(Application).filter(Application.id == application_id).first()

        if not application_query:
            raise ApplicationDoesNotExist("This application does not exist")

        try:
            self.db.delete(application_query)
            self.db.commit()
            return True
        except Exception as exception:
            self.db.rollback()
            raise DatabaseError(f"Error saving to the database: {str(exception)}")