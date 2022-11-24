from rest_framework import serializers
from datetime import datetime
from candidate.models.candidateapprovalmodel import CandidateApprovalModel
from candidate.models.candidatemodel import Candidate
from jobpost.models.jobpostmodel import JobPost
from managestages.models import Stage


class  CandidatePostSerializer(serializers.ModelSerializer):    

    Job_Post_ID = serializers.IntegerField()
    # file       = serializers.FileField()

    def validate(self, data):
        missing_fields = [f for f in self.Meta.required_fields if f not in data]

        if missing_fields:
            mf = ", ".join(missing_fields)
            raise serializers.ValidationError(f"candidate missing the following fields: {mf}")

        return data

    def create(self, validated_data):
        print("sasas-"+str(validated_data))
        stage_name = "Candidate Review"
        jobp = JobPost.objects.filter(JobPostId=validated_data["Job_Post_ID"]).first()
        print("2323-"+str(jobp.JobCode))
        stage = Stage.objects.filter(StageName=stage_name).first()        
        count = Candidate.objects.filter(Jobpost = jobp).count()
        maxvaluepad = str(count+1).zfill(2)
        if jobp.ServiceLine and jobp.Customer :
            Cancode =  jobp.ServiceLine.Acronym+"-"+jobp.Customer.Acronym+"-CAND-"+maxvaluepad
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
            CurrentCTC = validated_data["CurrentCTC"],
            ExpectedCTC = validated_data["ExpectedCTC"],
            NegotiatedCTC = validated_data["NegotiatedCTC"],
            ExpectedDOJ = validated_data["ExpectedDOJ"],
            CurrentOrganization = validated_data["CurrentOrganization"],
            CurrentJobLocation = validated_data["CurrentJobLocation"],
            Skills = validated_data["Skills"],
            Email = validated_data["Email"],
            ConatctNo = validated_data["ConatctNo"],
            Resume = validated_data["Resume"],
            AvgApprovedCTC = validated_data["AvgApprovedCTC"],
            AvgBillRate = validated_data["AvgBillRate"],
            CreatedBy = validated_data["CreatedBy"],
            CreatedOn = CreatedOn,
            ModifiedBy = validated_data["ModifiedBy"],
            ModifiedOn = ModifiedOn
        )
        return candidate

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
            "CurrentCTC",
            "ExpectedCTC",
            "NegotiatedCTC",
            "ExpectedDOJ",
            "CurrentOrganization",
            "CurrentJobLocation",
            "Skills",
            "Email",
            "ConatctNo",
            "Resume",
            "AvgApprovedCTC",
            "AvgBillRate",            
            "Job_Post_ID",   
            "CreatedBy",
            "ModifiedBy"
        ]
        required_fields = fields

class  CandidateDetailsGridSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField(read_only=True, source="Stage.StageDesc")
    Job_Code = serializers.CharField(read_only=True, source="Jobpost.JobCode")
    approversDetails = serializers.SerializerMethodField()     


    def get_approversDetails(self, Candidate1):
        qs = CandidateApprovalModel.objects.filter(Candidate=Candidate1)
        serializer = CandidateApprovalSerializer(instance=qs, many=True)
        return serializer.data    

    class Meta:
        model = Candidate
        fields = "__all__"        


class  CandidateApprovalSerializer(serializers.ModelSerializer):


    class Meta:
        model = CandidateApprovalModel
        fields = "__all__"