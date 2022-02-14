from channels.auth import AuthMiddlewareStack
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http.cookie import parse_cookie


@database_sync_to_async
def get_user(token_key):
    try:
        return get_user_model().objects.get(auth_token__key=token_key)
    except get_user_model().DoesNotExist:
        return AnonymousUser()


class TokenInHeaderOrCookieAuthMiddlewareInstance:

    HEADER: bytes = b'authorization'
    HEADER_TOKEN_KEY: str = 'Token'
    COOKIE_TOKEN_KEY: str = 'x-auth-token'

    def __init__(self, scope, middleware):
        self.middleware = middleware
        self.scope = dict(scope)
        self.inner = self.middleware.inner

    async def __call__(self, receive, send):
        headers = dict(self.scope['headers'])

        if self.HEADER in headers:
            token_name, _token_key = headers[self.HEADER].decode().split(':')
            token_key = _token_key.lstrip()
            if token_name == self.HEADER_TOKEN_KEY:
                self.scope['user'] = await get_user(token_key)

        elif b'cookie' in headers:
            cookies = parse_cookie(headers[b'cookie'].decode())
            cookies_lower = {k.lower(): v for k, v in cookies.items()}
            token_key = cookies_lower.get(self.COOKIE_TOKEN_KEY)
            if token_key:
                self.scope['user'] = await get_user(token_key)

        inner = self.inner(self.scope)
        return await inner(receive, send)


class TokenInHeaderOrCookieAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        return TokenInHeaderOrCookieAuthMiddlewareInstance(scope, self)


def TokenInHeaderOrCookieAuthMiddlewareStack(inner):
    return TokenInHeaderOrCookieAuthMiddleware(AuthMiddlewareStack(inner))
