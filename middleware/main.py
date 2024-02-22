from typing import Any
from django.http import HttpResponse


class ExampleMiddleware:
    def __init__(self,get_response) -> None:
        self.get_response=get_response
    def __call__(self, request,*args: Any, **kwds: Any) -> Any:
        print("Middleware called")
        response= self.get_response(request)
        user_agent=request.META.get("HTTP_USER_AGENT")
        print(user_agent)
        return HttpResponse(response)