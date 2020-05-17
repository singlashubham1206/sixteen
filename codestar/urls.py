from django.conf.urls import url
from codestar import views

urlpatterns = [
	url(r'^home/$',views.greetings),
    url(r'^home/run$',views.runcode),
]
