from django.http import HttpResponseForbidden
from functools import wraps

def active_user_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_active:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not allowed to access this page.")
    return _wrapped_view

def staff_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden("You are not allowed to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
