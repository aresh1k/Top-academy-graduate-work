from django.contrib import admin
from django.urls import path
from projects import views as project_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', project_views.main, name='main'),
    path('blog/', project_views.blog, name='blog'),
    path('projects/', project_views.projects, name='projects'),
    path('account/', users_views.user_account, name='account'),
    path('registration/', users_views.user_register, name='registration'),
    path('login/', users_views.user_logout, name='login'),
    path('logout/', users_views.user_login, name='logout'),
]
