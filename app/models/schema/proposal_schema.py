from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class ProposalBase(BaseModel):
    title: str
    body: str
    creator_id: UUID

class ProposalCreate(ProposalBase):
    date_created: datetime = datetime.today()
    pass

class ProposalSchema(ProposalBase):
    id: UUID
    date_created: str
    class Config:
        orm_mode = True

class ProposalPublic(ProposalBase):
    pass