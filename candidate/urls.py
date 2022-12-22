from django.urls import path
from candidate.views.candidateactions import CandidateAction

from candidate.views.candidateinsert import CandidateApi
from candidate.views.candidatedetails import CandidateDetails
from candidate.views.FeedbackFeilds import FeedbackFields
from candidate.views.CandidateFeedbacks import CandidateFeedBacks
urlpatterns=[
     path('/addcandidate', CandidateApi.as_view()),
     path('/gridcandidates', CandidateDetails.as_view({'post': 'candidatedetails'})),
     path('/downloadresume', CandidateDetails.as_view({'post': 'download'})),
     path('/candidateactionsdetails', CandidateAction.as_view({'post': 'candidateactiondetails'})),
     path('/candidateworkflowsubmit', CandidateAction.as_view({'post': 'candidateworkflowsubmit'})),
     path('/getfeedbackfields', FeedbackFields.as_view()),
     path('/getcandidatefeedbacks',CandidateFeedBacks.as_view()),

]