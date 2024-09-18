from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def admin_level_0_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_admin_level_0():
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def expert_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_expert():
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap