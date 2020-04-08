import functools
from django.shortcuts import redirect

def admins_only(func):
    @functools.wraps(func)
    def wrapper_logged_in(*args, **kwargs):
        request = args[0]
        if not request.user.is_authenticated:
            return redirect("account:login")
        if not request.user.is_superuser:
            return redirect("account:login")
        return func(*args, **kwargs)
    return wrapper_logged_in