from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'ingredientMaster', views.IngredientMasterViewSet, "ingredient")
router.register(r'classification', views.ClassificationViewSet, "classification")

app_name = 'qumi'
#url = serializers.HyperlinkedIdentityField(view_name="qumi:ingredientmaster-detail")

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'api/', include(router.urls)),
    #url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    #    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #    url(r'^(?P<pk>[0-9]+)/results/$',
    #        views.ResultsView.as_view(), name='results'),
    #    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
