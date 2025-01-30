# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *





class TrainingProgram(Base):
    """description: Model representing training programs associated with skills."""
    __tablename__ = 'training_programs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    duration_weeks = Column(Integer)





# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    role_dentist = Role(name='Dentist', description='Dental professional responsible for oral health.')
    role_receptionist = Role(name='Receptionist', description='Front office staff handling scheduling and patient interaction.')
    role_hygienist = Role(name='Hygienist', description='Dental hygienist assisting lateral duties.')
    role_assistant = Role(name='Dental Assistant', description='Support dentist with various procedures.')
    skill_cleaning = Skill(name='Teeth Cleaning', description='Regular cleaning and maintenance of oral hygiene.')
    skill_xray = Skill(name='X-Ray Imaging', description='Taking and analyzing dental x-rays.')
    skill_scheduling = Skill(name='Appointment Scheduling', description='Efficient scheduling and patient management.')
    skill_anesthesia = Skill(name='Administer Anesthesia', description='Administer and handle local anesthesia.')
    employee_dr_smith = Employee(name='Dr. John Smith', hire_date=date(2015, 3, 18))
    employee_mrs_jones = Employee(name='Mrs. Emily Jones', hire_date=date(2018, 11, 2))
    employee_mr_wilson = Employee(name='Mr. Kevin Wilson', hire_date=date(2020, 5, 20))
    employee_miss_clark = Employee(name='Miss. Rachel Clark', hire_date=date(2021, 7, 8))
    
    
    
    session.add_all([role_dentist, role_receptionist, role_hygienist, role_assistant, skill_cleaning, skill_xray, skill_scheduling, skill_anesthesia, employee_dr_smith, employee_mrs_jones, employee_mr_wilson, employee_miss_clark])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
