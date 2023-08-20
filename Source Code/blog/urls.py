from django.urls import path
from . import views
urlpatterns = [
    path('MovieDetails/', views.MovieDetails,name='blog-MovieDetails'),
    path('login/', views.login,name='blog-login'),
    path('signup/', views.signup,name='blog-signup'),
    path('output/',views.output,name='blog-output'),
    path('screens/',views.screens,name='blog-screens' ),
    path('screens_reset/',views.screens_reset,name='blog-screens' ),
    path('profile/',views.profile,name='blog-profile')
]