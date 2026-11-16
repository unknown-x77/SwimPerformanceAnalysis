from dataclasses import dataclass
import datetime

@dataclass
class Swimmer:
    name: str
    id: int


@dataclass
class Event:
    stroke: str
    distance: int
    course: str


@dataclass
class Result:
    swimmer: Swimmer
    event: Event
    time: float
    date: int
    suited: bool | None = None
