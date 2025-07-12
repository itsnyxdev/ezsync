from dataclasses import Field
from typing import Annotated

from pydantic import PlainValidator

from app.utils import is_password_safe

PasswordStr = Annotated[str, Field(min_length=8, max_length=128, description="Password must be between 8 and 128 characters long"),
    PlainValidator(is_password_safe)

]
UsernameStr = Annotated[str, Field(min_length=4, max_length=10, description="Username must be between 4 and 10 characters long")]