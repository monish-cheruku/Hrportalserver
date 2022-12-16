from django import urls
from django.urls import path
from CandidateFeedback.views.FeedbackFeilds import FeedbackFields
from CandidateFeedback.views.AddFeedBack import AddFeedBack
from CandidateFeedback.views.CandidateFeedbacks import CandidateFeedBacks


urlpatterns=[
    path('/getfeedbackfields',FeedbackFields.as_view()),
    path('/addfeedback',AddFeedBack.as_view()),
    path('/getcandidatefeedbacks',CandidateFeedBacks.as_view()),
]