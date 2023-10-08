from django.contrib import admin
from django.urls import path
from projects import views as project_views
from users import views as users_views
from forum import views as forum_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', project_views.main, name='main'),
    path('blog/', project_views.blog, name='blog'),
    path('projects/', project_views.projects, name='projects'),
    path('account/<int:pk>/', users_views.user_profile, name='account'),
    path('registration/', users_views.user_register, name='registration'),
    path('login/', users_views.user_login, name='login'),
    path('logout/', users_views.user_logout, name='logout'),
    path('account/update/', users_views.user_profile_settings, name='account_settings'),
    path('blog/create-post/', project_views.create_post, name='create_post'),
    path('blog/<str:link>/', project_views.blog_post, name='post'),
    path('projects/<str:link>/', project_views.project, name='project'),
    path('forum/', forum_views.forum, name='forum'),
    path('forum/discussion/<int:pk>/', forum_views.discussion, name='discussion'),
    path('forum/create_discussion/', forum_views.create_theme, name='create_discussion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
