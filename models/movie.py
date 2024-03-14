from dataclasses import dataclass


@dataclass
class Movie:
    id: int
    title: str
    release_date: str
    rating: float
