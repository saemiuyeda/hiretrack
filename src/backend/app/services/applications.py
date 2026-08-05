from datetime import date
from sqlalchemy.sql import exists
from sqlalchemy.orm import Session
from ..schemas.applications_request import Item
from ..models.application import Application
from ..domain.exceptions import InvalidApplicationDate, ApplicationAlreadyExists, DatabaseError

class ApplicationService():
    def __init__(self, db: Session):
         self.db = db

    def create_application(self, application_data: Item):
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