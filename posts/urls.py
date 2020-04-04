from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     # path('specifics/<int:question_id>/', views.detail, name='detail'),
#     # # ex: /polls/5/results/
#     # path('<int:question_id>/results/', views.results, name='results'),
#     # # ex: /polls/5/vote/
#     # path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
