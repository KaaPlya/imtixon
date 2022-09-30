from django.urls import path
from .views import NewsViews, SingleNews


urlpatterns = [
    path('list/', NewsViews.as_view()),
    path('list/<int:id>/', SingleNews.as_view()),
]
