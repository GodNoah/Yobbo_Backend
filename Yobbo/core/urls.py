from django.urls import path
from .views import RegisterView, LoginView, YobboAdminView, LogoutView, PostView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('YobboAdmin',YobboAdminView.as_view()),
    path('logout',LogoutView.as_view()),
    path('posts/<int:post_id>',PostView.as_view()),
    path('posts',PostView.as_view())
]
