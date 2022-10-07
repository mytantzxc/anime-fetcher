from dataclasses import dataclass
from typing import List


@dataclass
class Anime:
    title: str
    score: float
    genres: List[str]
    description: str
    url: str
    episodes: int
    status: str
