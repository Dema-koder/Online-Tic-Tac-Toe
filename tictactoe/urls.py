from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from game import views as game_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
    path('register/', user_views.register, name='register'), 
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(http_method_names=["post", "get", "options"], template_name='users/logout.html'), name='logout'),
    path('create/', game_views.create_game, name='create_game'),
    path('connect/', game_views.connect, name='connect'),
    path('connect_to_game/<int:game_id>/', game_views.connect_to_game, name='connect_to_game'),
    path('game/<int:game_id>/make_move/', game_views.make_move, name='make_move'),
    path('', include('django_prometheus.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
