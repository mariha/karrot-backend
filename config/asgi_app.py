from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.security import websocket
from django.conf import settings
from django.core.asgi import get_asgi_application

from starlette.staticfiles import StaticFiles

from karrot.subscriptions.consumers import WebsocketConsumer, TokenAuthMiddleware


class OriginValidatorThatAllowsFileUrls(websocket.OriginValidator):
    # We need to allow file urls in the origin header for our cordova app
    def valid_origin(self, parsed_origin):
        if parsed_origin is not None and parsed_origin.scheme == 'file':
            return True
        return super().valid_origin(parsed_origin)


def AllowedHostsAndFileOriginValidator(application):
    # copied from channels.security.websocket
    allowed_hosts = settings.ALLOWED_HOSTS
    if settings.DEBUG and not allowed_hosts:
        allowed_hosts = ["localhost", "127.0.0.1", "[::1]"]
    return OriginValidatorThatAllowsFileUrls(application, allowed_hosts)


api_app = get_asgi_application()
media_app = StaticFiles(directory=settings.MEDIA_ROOT)

if settings.FRONTEND_DIR:
    frontend_app = StaticFiles(directory=settings.FRONTEND_DIR, html=True)
else:
    frontend_app = None


async def http_app(scope, receive, send):
    app = None
    if 'path' in scope:
        path = scope['path']
        # TODO: need to check some more paths here... maybe a regex?
        # TODO: maybe a seperate static_app needed if that is set.. for prod?

        if any(path.startswith(prefix) for prefix in ('/api/', '/docs/', '/api-auth/', '/static/')):
            app = api_app
        elif path.startswith('/media'):
            scope['path'] = path[len('/media'):]
            app = media_app
        else:
            app = frontend_app

    if not app:
        raise Exception('invalid')

    return await app(scope, receive, send)


application = ProtocolTypeRouter({
    'http':
    http_app,
    'websocket':
    AllowedHostsAndFileOriginValidator(
        AuthMiddlewareStack(
            TokenAuthMiddleware(
                WebsocketConsumer.as_asgi(),
            ),
        ),
    ),
})