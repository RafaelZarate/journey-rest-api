
from django.contrib import admin
from django.conf.urls import url
from django.urls import  path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token

# Swagger view
schema_view = get_swagger_view(title="Journey API")

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^api-token-auth/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'))
]
