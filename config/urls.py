
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('instagram.urls')),
    path('', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
    path('post/', include('post.urls')),
    path('chat/', include('chat.urls')),
    path('comment/', include('comment.urls')),
    path('story/', include('story.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
