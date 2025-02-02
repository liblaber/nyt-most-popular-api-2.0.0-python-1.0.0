"""
An enum class containing all the possible environments for the SDK
"""

from enum import Enum


class Environment(Enum):
    """The environments available for the SDK"""

    DEFAULT = "https://api.nytimes.com/svc/mostpopular/v2"
