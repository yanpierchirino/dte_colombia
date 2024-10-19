from enum import Enum


class ProfileExcecutionId(int, Enum):
    """Profile excecution ID for organizations."""

    PRODUCTION = 1
    HABILITATION = 2
