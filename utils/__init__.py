from rest_framework.views import exception_handler


def custom_exception_handler(exec, context) -> None:
    response = exception_handler(exec, context)

    if response:
        pass

    return response
