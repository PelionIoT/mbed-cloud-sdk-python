class UserStatusEnum:
    """Represents the `UserStatusEnum` options as used by Mbed Cloud account_admin functionality"""

    ACTIVE = "ACTIVE"
    ENROLLING = "ENROLLING"
    INACTIVE = "INACTIVE"
    INVITED = "INVITED"
    RESET = "RESET"

    values = frozenset(("ACTIVE", "ENROLLING", "INACTIVE", "INVITED", "RESET"))

    def __setattr__(self, name, value):
        raise Exception("enum container values cannot be modified")


class UserOrderEnum:
    """Represents the `UserOrderEnum` options as used by Mbed Cloud account_admin functionality"""

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))

    def __setattr__(self, name, value):
        raise Exception("enum container values cannot be modified")


class ApiKeyStatusEnum:
    """Represents the `ApiKeyStatusEnum` options as used by Mbed Cloud accounts functionality"""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    values = frozenset(("ACTIVE", "INACTIVE"))

    def __setattr__(self, name, value):
        raise Exception("enum container values cannot be modified")


class ListOrder:
    """Represents the `ListOrder` options as used by Mbed Cloud common functionality"""

    ASC = "ASC"
    DESC = "DESC"

    values = frozenset(("ASC", "DESC"))

    def __setattr__(self, name, value):
        raise Exception("enum container values cannot be modified")
