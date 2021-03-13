from dataclasses import dataclass
from typing import List


@dataclass(frozen=True, eq=False)
class CarPath:
    streets_sequence: List[Street]
