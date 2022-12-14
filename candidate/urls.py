from django.urls import path
from candidate.views.candidateactions import CandidateAction

from candidate.views.candidateinsert import CandidateApi
from candidate.views.candidatedetails import CandidateDetails

urlpatterns=[
     path('/addcandidate', CandidateApi.as_view()),
     path('/gridcandidates', CandidateDetails.as_view({'post': 'candidatedetails'})),
     path('/downloadresume', CandidateDetails.as_view({'post': 'download'})),
     path('/candidateactionsdetails', CandidateAction.as_view({'post': 'candidateactiondetails'}))
]