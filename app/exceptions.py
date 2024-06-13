from django.core.exceptions import (
    ValidationError as DjangoValidationError,
    PermissionDenied,
)
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import exceptions
from rest_framework.serializers import as_serializer_error
from typing import Any


def custom_exception_handler(
    exception: type[BaseException], context: dict[str, Any]
) -> Response:
    if isinstance(exception, DjangoValidationError):
        exception = exceptions.ValidationError(as_serializer_error(exception))

    if isinstance(exception, Http404):
        exception = exceptions.NotFound()

    if isinstance(exception, PermissionDenied):
        exception = exceptions.PermissionDenied()

    response = exception_handler(exception, context)

    if response is None:
        return response

    if isinstance(exception.detail, (list, dict)):
        response.data = {"message": response.data}

    return response
