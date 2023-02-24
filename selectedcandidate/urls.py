from django.urls import path
from selectedcandidate.views.documentuploadview import documentuploadview
from selectedcandidate.views.educationdetailview import educationdetailsview
from selectedcandidate.views.employementdetailview import employementdetailsview
from selectedcandidate.views.familydetailsview import familydetailsview
from selectedcandidate.views.personaldetailsview import personaldetialsview

from selectedcandidate.views.selectedcandidateactions import SelectedCandidateAction
from selectedcandidate.views.candidateinfoclearance import Candidateinfoclearance
from selectedcandidate.views.acceptofferletter import Acceptofferletter
from selectedcandidate.views.insurancedetailview import insurancedetailsview
from selectedcandidate.views.bankdetailsview import bankdetailsview
from selectedcandidate.views.pfdetailsview import PFdetailsview

from selectedcandidate.views.verifydocument import Verifydocument
from selectedcandidate.views.verifycandidate import Verifycandidate

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

     path('/uploaddetaildocument', documentuploadview.as_view({'post': 'createdocument'})),
     path('/deletedocument', documentuploadview.as_view({'post': 'deletedocument'})),
     path('/downloaddetaildocuments', documentuploadview.as_view({'post': 'downloaddetaildocuments'})),
     path('/getotherdocuments', documentuploadview.as_view({'post': 'getotherdocuments'})),


     path('/getcandidateinfoclearance', Candidateinfoclearance.as_view({'post': 'getallcandidateinfoclearance'})),
     path('/acceptofferletter', Acceptofferletter.as_view({'post': 'acceptofferletter'})),
     path('/verifydocument', Verifydocument.as_view({'post': 'Verifydocument'})),
     path('/verifycandidate', Verifycandidate.as_view({'post': 'Verifycandidate'})),


     path('/createinsurancedetail', insurancedetailsview.as_view({'post': 'createinsurancedetail'})),
     path('/updateinsurancedetail', insurancedetailsview.as_view({'post': 'updateinsurancedetail'})),
     path('/getinsurancedetails', insurancedetailsview.as_view({'post': 'getinsurancedetails'})),
     path('/deleteinsurancedetail', insurancedetailsview.as_view({'post': 'deleteinsurancedetail'})),

     path('/createbankdetail', bankdetailsview.as_view({'post': 'createbankdetail'})),
     path('/updatebankdetail', bankdetailsview.as_view({'post': 'updatebankdetail'})),
     path('/getbankdetails', bankdetailsview.as_view({'post': 'getbankdetails'})),
     path('/deletebankdetail', bankdetailsview.as_view({'post': 'deletebankdetail'})),

     path('/createPFdetail', PFdetailsview.as_view({'post': 'createPFdetail'})),
     path('/updatePFdetail', PFdetailsview.as_view({'post': 'updatePFdetail'})),
     path('/getPFdetails', PFdetailsview.as_view({'post': 'getPFdetails'})),
     path('/deletePFdetail', PFdetailsview.as_view({'post': 'deletePFdetail'})),

]