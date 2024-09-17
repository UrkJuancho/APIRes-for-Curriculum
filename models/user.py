from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class basicData(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Full name of the user")
    typeDoc: str = Field(..., description="Type of document (e.g., C.C., Passport)")
    numberDoc: int = Field(..., description="Document number")
    dateBirthday: str = Field(..., description="Birthdate in string format")
    numberPhone: str = Field(..., description="Phone number")
    email: EmailStr = Field(..., description="Valid email address")

class xpData(BaseModel):
    company: str = Field(..., description="Company name")
    datetime: str = Field(..., description="Time worked in the company")
    position: str = Field(..., description="Role or position held in the company")

class schoolarData(BaseModel):
    institute: str = Field(..., description="Name of the institute or university")
    datetime: str = Field(..., description="Time spent studying there")
    schoolarTitle: str = Field(..., description="Degree or title obtained")
