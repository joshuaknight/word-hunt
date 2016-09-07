from django.conf.urls import url,include
from django.contrib import admin
from my_quiz.views import * 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_page,name	= 'home'),
    #url(r'^add$',list_my_view.as_view(),name = 'add'),
    url(r'^add/(?P<pk>\d+)',list_my_view,name = 'next'),
    url(r'^form$',my_question.as_view(),name = 'question'),
    url(r'^score$',score,name = 'score'),
    url(r'^score/round3$',score_round,name = 'score_round3'),
    url(r'^round3/(?P<pk>\d+)',round3,name = 'round3'),
    url(r'^add/round3$',AddRound3.as_view(),name = 'add_round3'),
]
