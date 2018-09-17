from mbed_cloud.pagination import PaginatedResponse


def paginate(self, foreign_key, wraps, *args, **kwargs):
    def wrapper(api_data):
        return foreign_key().from_api(**api_data)

    return PaginatedResponse(func=wraps, lwrap_type=wrapper, *args, **kwargs)
