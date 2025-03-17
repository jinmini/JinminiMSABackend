from enum import Enum

class StrategyType(Enum):
    DEFAULT_CREATE = "default_create"
    VALIDATED_CREATE = "validated_create"
    GET_DETAIL = "get_detail"
    GET_ALL = "get_all"
    FULL_UPDATE = "full_update"
    PARTIAL_UPDATE = "partial_update"
    SOFT_DELETE = "soft_delete"
    HARD_DELETE = "hard_delete"
