from django.urls import path
from selectedcandidate.views.educationdetailview import educationdetailsview
from selectedcandidate.views.employementdetailview import employementdetailsview
from selectedcandidate.views.familydetailsview import familydetailsview
from selectedcandidate.views.personaldetailsview import personaldetialsview

from selectedcandidate.views.selectedcandidateactions import SelectedCandidateAction

urlpatterns=[

     path('/selectedcandidatedetailsbyemail', SelectedCandidateAction.as_view({'post': 'selectedcandidatedetailsbyemail'})),
     path('/createpersonaldetails', personaldetialsview.as_view({'post': 'createpersonaldetails'})),
     path('/updatepersonaldetails', personaldetialsview.as_view({'post': 'updatepersonaldetails'})),
     path('/getpersonaldetailsdata', personaldetialsview.as_view({'post': 'getpersonaldetails'})),

     path('/createfamilydetail', familydetailsview.as_view({'post': 'createfamilydetail'})),
     path('/updatefamilydetails', familydetailsview.as_view({'post': 'updatefamilydetails'})),
     path('/getfamilydetails', familydetailsview.as_view({'post': 'getfamilydetails'})),
     path('/deletefamilydetail', familydetailsview.as_view({'post': 'deletefamilydetail'})),


     path('/createeducationdetail', educationdetailsview.as_view({'post': 'createeducationdetail'})),
     path('/updateeducationdetails', educationdetailsview.as_view({'post': 'updateeducationdetails'})),
     path('/geteducationdetails', educationdetailsview.as_view({'post': 'geteducationdetails'})),
     path('/deleteeducationdetail', educationdetailsview.as_view({'post': 'deleteeducationdetail'})),


     path('/createemployementdetail', employementdetailsview.as_view({'post': 'createemployementdetail'})),
     path('/updateemployementdetails', employementdetailsview.as_view({'post': 'updateemployementdetails'})),
     path('/getemployementdetails', employementdetailsview.as_view({'post': 'getemployementdetails'})),
     path('/deleteemployementdetail', employementdetailsview.as_view({'post': 'deleteemployementdetail'})),




]