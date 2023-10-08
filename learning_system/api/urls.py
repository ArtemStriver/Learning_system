from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('products/', views.GetProductInfoView.as_view()),
    path('lessons/', views.GetLessonInfoView.as_view()),
    path('userdata/', views.GetUserDataInfoView.as_view()),
    # path('probe/', views.Probe.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
