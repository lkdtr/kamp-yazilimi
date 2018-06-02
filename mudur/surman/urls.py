
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from surman.views import AnswerListView

urlpatterns = [
                       url(r'^answers', login_required(AnswerListView.as_view()), name="survey_answers"),
]