from django.urls import path

from selectedcandidate.views.selectedcandidateactions import SelectedCandidateAction

urlpatterns=[

     path('/selectedcandidatedetailsbyemail', SelectedCandidateAction.as_view({'post': 'selectedcandidatedetailsbyemail'})),



]