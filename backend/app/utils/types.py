from dataclasses import Field
from enum import StrEnum
from typing import Annotated

from annotated_types import Len
from pydantic import PlainValidator

from .helpers import is_password_safe

PasswordStr = Annotated[str, PlainValidator(is_password_safe)]
UsernameStr = Annotated[str, Len(4, 10)]

class LevelType(StrEnum):
    entry = "entry"
    mid = "mid"
    senior = "senior"