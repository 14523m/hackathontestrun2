from dataclasses import dataclass
from typing import Optional


@dataclass
class Member:
    id: str
    name: str
    origin: str
    max_travel_time: int
    budget: int
    activities: list[str]
    preferred_time: str