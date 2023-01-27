from django.urls import path
from candidate.views.candidateactions import CandidateAction

from candidate.views.candidateinsert import CandidateApi
from candidate.views.candidatedetails import CandidateDetails
from candidate.views.FeedbackFeilds import FeedbackFields
from candidate.views.CandidateFeedbacks import CandidateFeedBacks
from candidate.views.selectedcandidatesgridview import selectedcandidatesgridview
from candidate.views.updateselectedcandidate import updateselectedcandidate
# from candidate.views.updateselectedcandidate import previewannexure
urlpatterns=[
     path('/addcandidate', CandidateApi.as_view()),
     path('/gridcandidates', CandidateDetails.as_view({'post': 'candidatedetails'})),
     path('/downloadresume', CandidateDetails.as_view({'post': 'download'})),
     path('/candidateactionsdetails', CandidateAction.as_view({'post': 'candidateactiondetails'})),
     path('/candidateworkflowsubmit', CandidateAction.as_view({'post': 'candidateworkflowsubmit'})),
     path('/getfeedbackfields', FeedbackFields.as_view()),
     path('/getcandidatefeedbacks',CandidateFeedBacks.as_view()),
     path('/getselectedcandidates',selectedcandidatesgridview.as_view()),
     path('/updateselectedcandidate',updateselectedcandidate.as_view({'post':"updateselcandidate"})),
     path('/getAnnexureDetails',updateselectedcandidate.as_view({'post':"getAnnexureDetails"})),


]