from pydantic import BaseModel, ConfigDict

from dte_colombia.client.enums import ProfileExcecutionId


class UUID(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: ProfileExcecutionId
    name: str
    content: str
