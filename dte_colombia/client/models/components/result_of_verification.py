from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, field_serializer


class ResultOfVerification(BaseModel):
    validation_result_code: Optional[str] = None
    validation_datetime: Optional[datetime] = None

    @field_serializer("validation_datetime")
    def serialize_dt(self, dt: datetime) -> str:
        return dt.isoformat()