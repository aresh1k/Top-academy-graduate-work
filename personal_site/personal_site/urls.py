"""
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('logout/', users_views.user_login, name='logout'),
    path('login/', users_views.user_logout, name='login'),
]
