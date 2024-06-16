from django.http import HttpResponseRedirect
from functools import wraps
from typing import Callable


def roles_required(
    required_roles: list[str], redirect: str = "/auth/login/"
) -> Callable:
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            role = request.session.get("role")
            if not role:
                return HttpResponseRedirect(redirect)
            if request.session.get("role").upper() not in [
                role.upper() for role in required_roles
            ]:
                return HttpResponseRedirect(redirect)
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
