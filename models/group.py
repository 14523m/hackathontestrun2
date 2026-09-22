from dataclasses import dataclass, field
from models.member import Member


@dataclass
class Group:
    id: str
    name: str
    members: list[Member] = field(default_factory=list)