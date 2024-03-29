from rest_framework import serializers
from datetime import datetime
from HRproj.settings import MEDIA_ROOT, MEDIA_URL
from candidate.models.Candidate_Feedback_Model import Candidate_Feedback
from candidate.models.Feedback_Category_Model import Feedback_Category
from candidate.models.candidateapprovalmodel import CandidateApprovalModel
from candidate.models.candidatemodel import Candidate
from jobpost.models.jobpostmodel import JobPost
from managestages.models import Stage
from candidate.models.candidateactionmodel import CandidateActionModel
import os
from HRproj.util.Constants.HR_WorkFlow_Constants import Constants1
from candidate.models.selected_Candidates_Model import Selected_Candidates
from jobpost.serializers import JobPostDetailsGridSerializer
from selectedcandidate.Serializers import candidatepersonalinfogetSerializer
from selectedcandidate.Serializers import candidatebankdetailgetSerializer

class  CandidatePostSerializer(serializers.ModelSerializer):    

    Job_Post_ID = serializers.IntegerField()
    # file       = serializers.FileField()

    def validate(self, data):
        # missing_fields = [f for f in self.Meta.required_fields if f not in data]

        # if missing_fields:
        #     mf = ", ".join(missing_fields)
        #     raise serializers.ValidationError(f"candidate missing the following fields: {mf}")

        return data

    def create(self, validated_data):
        print("sasas-"+str(validated_data))
        stage_name = Constants1.STAGE_CR
        jobp = JobPost.objects.filter(JobPostId=validated_data["Job_Post_ID"]).first()
        print("2323-"+str(jobp.JobCode))
        stage = Stage.objects.filter(StageName=stage_name).first()        
        count = Candidate.objects.filter(Jobpost = jobp).count()
        maxvaluepad = str(count+1).zfill(2)
        # if jobp.ServiceLine and jobp.Customer :
            # Cancode =  jobp.ServiceLine.Acronym+"-"+jobp.Customer.Acronym+"-"+jobp.JobPostId+"-"+maxvaluepad
        Cancode = jobp.JobCode+"-"+maxvaluepad
        CreatedOn = datetime.now()
        ModifiedOn = None
        print("Cancode-"+str(Cancode))
                        
        candidate = Candidate.objects.create(
            CandidateCode = Cancode,
            Stage = stage,
            Jobpost = jobp,
            HRUserName =  validated_data["HRUserName"],
            CanFirstName = validated_data["CanFirstName"],
            CanLastName = validated_data["CanLastName"],        
            
            Qualification = validated_data["Qualification"],
            OverallExpYear = validated_data["OverallExpYear"],
            OverallExpMonth = validated_data["OverallExpMonth"],
            ReleventExpYear = validated_data["ReleventExpYear"],
            ReleventExpMonth = validated_data["ReleventExpMonth"],
            EmploymentType = validated_data["EmploymentType"],
            Duration = validated_data["Duration"],
            Location = validated_data["Location"],
            CurrentCTC = validated_data["CurrentCTC"],
            ExpectedCTC = validated_data["ExpectedCTC"],
            NegotiatedCTC = validated_data["NegotiatedCTC"],
            ExpectedDOJ = validated_data["ExpectedDOJ"],
            CurrentOrganization = validated_data["CurrentOrganization"],
            CurrentJobLocation = validated_data["CurrentJobLocation"],
            Skills = validated_data["Skills"],
            Email = validated_data["Email"],
            ContactNo = validated_data["ContactNo"],
            Resume = validated_data["Resume"],
            AvgApprovedCTC = validated_data["AvgApprovedCTC"],
            AvgBillRate = validated_data["AvgBillRate"],
            CreatedBy = validated_data["CreatedBy"],
            CreatedOn = CreatedOn,
            ModifiedBy = validated_data["ModifiedBy"],
            ModifiedOn = ModifiedOn,
            Comments = validated_data["Comments"],
        )
        return candidate
    #dead code
    def update(self, instance, validated_data):
        # stage_name = "BH Approval"
        # cancode=Candidate.objects.filter(CandidateId=validated_data["CandidateId"]).first()
        jobp=JobPost.objects.filter(JobPostId=validated_data["Job_Post_ID"]).first()

        # instance.CandidateCode = cancode
        # instance.Stage = stage
        instance.Jobpost = jobp
        # instance.JobTitle=validated_data.get('JobTitle', instance.JobTitle) 
        instance.HRUserName = validated_data.get('HRUserName', instance.HRUserName) 
        instance.CanFirstName = validated_data.get('CanFirstName', instance.CanFirstName) 
        instance.CanLastName =validated_data.get('CanLastName', instance.CanLastName)        

        instance.Qualification = validated_data.get('Qualification', instance.Qualification) 
        instance.OverallExpYear =validated_data.get('OverallExpYear', instance.OverallExpYear) 
        instance.OverallExpMonth = validated_data.get('OverallExpMonth', instance.OverallExpMonth) 
        instance.ReleventExpYear = validated_data.get('ReleventExpYear', instance.ReleventExpYear) 
        instance.ReleventExpMonth = validated_data.get('ReleventExpMonth', instance.ReleventExpMonth) 

        instance.EmploymentType = validated_data.get('EmploymentType', instance.EmploymentType) 
        instance.Location = validated_data.get('Location', instance.Location) 
        instance.CurrentCTC = validated_data.get('CurrentCTC', instance.CurrentCTC) 
        instance.ExpectedCTC = validated_data.get('ExpectedCTC', instance.ExpectedCTC) 
        instance.NegotiatedCTC = validated_data.get('NegotiatedCTC', instance.NegotiatedCTC) 
        instance.ExpectedDOJ =validated_data.get('ExpectedDOJ', instance.ExpectedDOJ) 
        instance.CurrentOrganization = validated_data.get('CurrentOrganization', instance.CurrentOrganization) 
        instance.CurrentJobLocation =validated_data.get('CurrentJobLocation', instance.CurrentJobLocation) 
        instance.Skills = validated_data.get('Skills', instance.Skills) 
        instance.Email = validated_data.get('Email', instance.Email) 
        instance.ContactNo = validated_data.get('ContactNo', instance.ContactNo) 
        instance.Comments = validated_data.get('Comments', instance.Comments) 
        # if(type(validated_data.get("Resume")) is str):
        #     print("old file name")
        # else:
        #     print("new file ")
        if(instance.Resume.name is not None):
            print("removing file ...")
            try:
                os.remove(os.path.join(MEDIA_ROOT, str(instance.Resume.name)))
            except:
                print("")
            finally:
                print("")
            instance.Resume =validated_data.get('Resume', instance.Resume) 
        else:
            instance.Resume =validated_data.get('Resume', instance.Resume) 
        instance.AvgApprovedCTC =validated_data.get('AvgApprovedCTC', instance.AvgApprovedCTC) 
        instance.AvgBillRate = validated_data.get('AvgBillRate', instance.AvgBillRate) 
        instance.CreatedBy =validated_data.get('CreatedBy', instance.CreatedBy) 
        instance.CreatedOn = validated_data.get('CreatedOn', instance.CreatedOn) 
        instance.ModifiedOn = datetime.now() 
      
       
        instance.save()
        return instance
    class Meta:
        model = Candidate
        fields = [
            "HRUserName",
            "CanFirstName",
            "CanLastName",
            "Qualification",
            "OverallExpYear",
            "OverallExpMonth",
            "ReleventExpYear",
            "ReleventExpMonth",
             "EmploymentType",
             "Duration",
            "Location",
            "CurrentCTC",
            "ExpectedCTC",
            "NegotiatedCTC",
            "ExpectedDOJ",
            "CurrentOrganization",
            "CurrentJobLocation",
            "Skills",
            "Email",
            "ContactNo",
            "Resume",
            "AvgApprovedCTC",
            "AvgBillRate",            
            "Job_Post_ID",   
            "CreatedBy",
            "ModifiedBy",
            "Comments"
        ]
        required_fields = fields

class  CandidatePutSerializer(serializers.ModelSerializer):    

    Job_Post_ID = serializers.IntegerField()
    # file       = serializers.FileField()

    def validate(self, data):
        # missing_fields = [f for f in self.Meta.required_fields if f not in data]

        # if missing_fields:
        #     mf = ", ".join(missing_fields)
        #     raise serializers.ValidationError(f"candidate missing the following fields: {mf}")

        return data

    def update(self, instance, validated_data):
        # stage_name = "BH Approval"
        # cancode=Candidate.objects.filter(CandidateId=validated_data["CandidateId"]).first()
        jobp=JobPost.objects.filter(JobPostId=validated_data["Job_Post_ID"]).first()

        # instance.CandidateCode = cancode
        # instance.Stage = stage
        instance.Jobpost = jobp
        # instance.JobTitle=validated_data.get('JobTitle', instance.JobTitle) 
        instance.HRUserName = validated_data.get('HRUserName', instance.HRUserName) 
        instance.CanFirstName = validated_data.get('CanFirstName', instance.CanFirstName) 
        instance.CanLastName =validated_data.get('CanLastName', instance.CanLastName)        

        instance.Qualification = validated_data.get('Qualification', instance.Qualification) 
        instance.OverallExpYear =validated_data.get('OverallExpYear', instance.OverallExpYear) 
        instance.OverallExpMonth = validated_data.get('OverallExpMonth', instance.OverallExpMonth) 
        instance.ReleventExpYear = validated_data.get('ReleventExpYear', instance.ReleventExpYear) 
        instance.ReleventExpMonth = validated_data.get('ReleventExpMonth', instance.ReleventExpMonth) 
        instance.EmploymentType = validated_data.get('EmploymentType', instance.EmploymentType) 
        instance.Duration = validated_data.get('Duration', instance.Duration) 
        instance.Location = validated_data.get('Location', instance.Location) 
        instance.CurrentCTC = validated_data.get('CurrentCTC', instance.CurrentCTC) 
        instance.ExpectedCTC = validated_data.get('ExpectedCTC', instance.ExpectedCTC) 
        instance.NegotiatedCTC = validated_data.get('NegotiatedCTC', instance.NegotiatedCTC) 
        instance.ExpectedDOJ =validated_data.get('ExpectedDOJ', instance.ExpectedDOJ) 
        instance.CurrentOrganization = validated_data.get('CurrentOrganization', instance.CurrentOrganization) 
        instance.CurrentJobLocation =validated_data.get('CurrentJobLocation', instance.CurrentJobLocation) 
        instance.Skills = validated_data.get('Skills', instance.Skills) 
        instance.Email = validated_data.get('Email', instance.Email) 
        instance.ContactNo = validated_data.get('ContactNo', instance.ContactNo) 
        instance.Resume =validated_data.get('Resume', instance.Resume) 
        instance.AvgApprovedCTC =validated_data.get('AvgApprovedCTC', instance.AvgApprovedCTC) 
        instance.AvgBillRate = validated_data.get('AvgBillRate', instance.AvgBillRate) 
        instance.CreatedBy =validated_data.get('CreatedBy', instance.CreatedBy) 
        instance.CreatedOn = validated_data.get('CreatedOn', instance.CreatedOn) 
        instance.ModifiedOn = datetime.now() 
        instance.Comments=validated_data.get('Comments',instance.Comments)
       
        instance.save()
        return instance
    class Meta:
        model = Candidate
        fields = [
            "HRUserName",
            "CanFirstName",
            "CanLastName",
            "Qualification",
            "OverallExpYear",
            "OverallExpMonth",
            "ReleventExpYear",
            "ReleventExpMonth",
            "EmploymentType",
            "Duration",
            "Location",
            "CurrentCTC",
            "ExpectedCTC",
            "NegotiatedCTC",
            "ExpectedDOJ",
            "CurrentOrganization",
            "CurrentJobLocation",
            "Skills",
            "Email",
            "ContactNo",
            "AvgApprovedCTC",
            "AvgBillRate",            
            "Job_Post_ID",   
            "CreatedBy",
            "ModifiedBy",
            "Comments"
        ]
        required_fields = fields

class  CandidateDetailsGridSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField(read_only=True, source="Stage.StageDesc")
    Job_Code = serializers.CharField(read_only=True, source="Jobpost.JobCode")
    CanJobLocation = serializers.CharField(read_only=True, source="Location.LocationName")
    CanEmploymentType = serializers.CharField(read_only=True, source="EmploymentType")
    CanDuration = serializers.CharField(read_only=True, source="Duration")
    
    approversDetails = serializers.SerializerMethodField()     
    candidatefullname=serializers.SerializerMethodField()

    def get_candidatefullname(self,Candidate1):
        return Candidate1.CanLastName+", "+Candidate1.CanFirstName
    def get_approversDetails(self, Candidate1):
        qs = CandidateApprovalModel.objects.filter(Candidate=Candidate1)
        serializer = CandidateApprovalSerializer(instance=qs, many=True)
        return serializer.data    

    class Meta:
        model = Candidate
        fields = "__all__"        


class  CandidateApprovalSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(read_only=True, source="role.name")
    stage_name = serializers.CharField(read_only=True, source="Stage.StageName")

    class Meta:
        model = CandidateApprovalModel
        fields = "__all__"
        

class  CandidateActionModelSerializer(serializers.ModelSerializer):
    Comments = serializers.SerializerMethodField()     


    def get_Comments(self, Candidate1):
        can=Candidate.objects.filter(CandidateId=Candidate1.CandidateId).first()
        qs = CandidateApprovalModel.objects.filter(Candidate=can).exclude(approvalStatus="N")
        # qs1=qs.filter(approvalStatus="N")
        serializer = CandidateApprovalCommentsSerializer(instance=qs, many=True)
        return serializer.data    

    class Meta:
        model = CandidateActionModel
        fields = "__all__"
class CandidateApprovalCommentsSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(read_only=True, source="role.name")
    stage_name = serializers.CharField(read_only=True, source="Stage.StageName")
    class Meta:
        model=CandidateApprovalModel
        fields=["approvalComments","role_name","stage_name"]

class FeedbackBulkCreateSerializer(serializers.ListSerializer):  
    def create(self, validated_data):  
        product_data = [Candidate_Feedback(**item) for item in validated_data]  
        return Candidate_Feedback.objects.bulk_create(product_data)  
  
  
class AddFeedBackSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Candidate_Feedback  
        fields ="__all__"
        # read_only_fields = ['id',]  
        list_serializer_class = FeedbackBulkCreateSerializer

class CandidateFeedBacksSerializer(serializers.ModelSerializer):
    interviewtype=serializers.CharField(read_only=True, source="FeedbackCategory.InterviewType")
    feedbackcategory=serializers.CharField(read_only=True, source="FeedbackCategory.FeedbackCategory")
    class Meta:
        model=Candidate_Feedback
        fields="__all__"  
              
class FeedbackFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback_Category
        fields="__all__"        
class selectedcandidatesgridviewSerializer(serializers.ModelSerializer):
    designation_name = serializers.CharField(read_only=True, source="designation.DesignationName")
    band_name = serializers.CharField(read_only=True, source="band.BandName")
    subband_name = serializers.CharField(read_only=True, source="subband.SubBandName")
    jobpost=JobPostDetailsGridSerializer(source="candidate.Jobpost")
    candidate=CandidateDetailsGridSerializer()
    personalinfo = candidatepersonalinfogetSerializer(source='candidatepersonalinfo_set', many=True)
    bankdetails = candidatebankdetailgetSerializer(source = 'candidatebankdetails_set', many=True)
    
        
    class Meta:
        model=Selected_Candidates
        fields="__all__"
        
class AddSelectedCandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Selected_Candidates
        fields=["candidate"]
