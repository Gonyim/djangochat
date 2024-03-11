"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

# settings.py 경로에 맞춰 DJANGO_SETTINGS_MODULE 환경변수의 디폴트 값을 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# asgi.py 편집을 통해, 클라이언트로부터의 요청을 채널스에서 먼저 받고
django_asgi_app = get_asgi_application()

# http 요청은 장고를 통해서 처리토록 하게 함
# 프로토콜 타입 별로 서로 다른 ASGGI application을 통해 처리토록 라우팅합니다.
application = ProtocolTypeRouter({
    # 지금은 http 타입에 대한 라우팅만 명시
    "http": django_asgi_app,
    # 서비스 규모에 따라 http와 websocket을 분리하여 (웹서버와 채팅서버) 운영
    # websocket": ... ,
})