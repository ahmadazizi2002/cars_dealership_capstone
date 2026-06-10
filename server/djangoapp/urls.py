from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login', views.login_user),
    path('logout', views.logout_user),
    path('register', views.register_user),
    path('get_dealers', views.get_dealers),
    path('get_dealers/<str:state>', views.get_dealers_by_state),
    path('get_dealer/<int:dealer_id>', views.get_dealer_by_id),
    path('get_dealer_reviews/<int:dealer_id>', views.get_dealer_reviews),
    path('get_cars', views.get_cars),
    path('post_review', views.post_review),
]
