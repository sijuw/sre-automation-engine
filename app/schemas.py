from pydantic import BaseModel
from typing import Optional


class GrafanaAlert(BaseModel):
    title: str
    status: str
    message: Optional[str] = None
    dashboardURL: Optional[str] = None