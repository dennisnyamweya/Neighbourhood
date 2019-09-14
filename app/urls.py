from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.HomePageView.as_view(),name="home"),
    # path('detail/<int:id>',views.detail,name="detail"),
    path('detail/<int:pk>',views.HoodDetailView.as_view(),name="detail"),
    path('business_detail/<int:pk>',views.BusinessDetailView.as_view(),name="business_detail"),
    path('search/',views.search,name="search"),
    path('business/',views.business,name="business"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
]