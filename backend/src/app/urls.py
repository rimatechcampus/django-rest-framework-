from django.urls import path, include

# from .views import article_list, article_detail , ArticleAPIView,
from .views import article_detail, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path('', article_list, name='article_list'),
    # path('detail/<int:pk>/', article_detail, name='article_detail'),

    # ! cbv
    # path('', ArticleAPIView.as_view(), name='article_list'),

    # ! genetic class view
    # path('<int:id>/', GenericAPIView.as_view(), name='article_list'),

    # ! viewsets
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

]
