from datetime import datetime
from rest_framework import serializers
from ManageCustomer.models import Customer
from ManageExperienceLevel.models import Experience
from ManageIndustry.models import Industry
from ManageLocation.models import Location
from jobpost.models.jobpostactionmodel import JobPostActionModel
from jobpost.models.jobpostapprovalmodel import JobPostApproval

from jobpost.models.jobpostmodel import JobPost
from jobpost.models.jobpostuserrolesmodel import JobPostUserRolesModel
from managebusinessunit.models import BusinessUnit
from managecompany.models import Company
from manageserviceline.models import ServiceLine
from managestages.models import Stage
from django.db.models import Max
from django.contrib.auth.models import User


class  JobPostDetailsGridSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField(read_only=True, source="Stage.StageDesc")
    industry_name = serializers.CharField(read_only=True, source="Industry.IndustryName")
    company_name = serializers.CharField(read_only=True, source="Company.CompanyName")
    businessunit_name = serializers.CharField(read_only=True, source="BusinessUnit.BusinessUnitName")
    serviceline_name = serializers.CharField(read_only=True, source="ServiceLine.ServiceLineName")
    customer_name = serializers.CharField(read_only=True, source="Customer.CustomerName")
    location_name = serializers.CharField(read_only=True, source="Location.LocationName")  
    experience_Level = serializers.CharField(read_only=True, source="ExperianceLevel.ExperienceLevel")
    approversDetails = serializers.SerializerMethodField()     


    def get_approversDetails(self, jobpost1):
        qs = JobPostApproval.objects.filter(jobpost=jobpost1)
        serializer = JobPostApprovalSerializer(instance=qs, many=True)
        return serializer.data    

    class Meta:
        model = JobPost
        fields = "__all__"


class  JobPostActionGridSerializer(serializers.ModelSerializer):
    jobpost = JobPostDetailsGridSerializer(read_only=True) 

    class Meta:
        model = JobPostApproval
        fields = "__all__"
        

class  JobPostDetailsPostSerializer(serializers.ModelSerializer):    
    # stage_name = serializers.CharField(read_only=True, source="Stage.StageDesc")
    # Stage_id = serializers.IntegerField()
    

    Company_id = serializers.IntegerField()
    BusinessUnit_id = serializers.IntegerField()
    Serviceline_id = serializers.IntegerField()
    Customer_id = serializers.IntegerField()
    Location_id = serializers.IntegerField()
    ExperianceLevel_id = serializers.IntegerField()
    Industry_id = serializers.IntegerField()
    BH_User_Name = serializers.CharField()
    HR_User_Name = serializers.CharField()

    def validate(self, data):
        missing_fields = [f for f in self.Meta.required_fields if f not in data]

        if missing_fields:
            mf = ", ".join(missing_fields)
            raise serializers.ValidationError(f"job post missing the following fields: {mf}")

        return data

    def create(self, validated_data):
        stage_name = "BH Approval"
        serviceline = ServiceLine.objects.filter(ServiceLineId=validated_data["Serviceline_id"]).first()
        customer = Customer.objects.filter(CustomerId=validated_data["Customer_id"]).first()
        stage = Stage.objects.filter(StageName=stage_name).first()
        industry = Industry.objects.filter(IndustryId=validated_data["Industry_id"]).first()
        company = Company.objects.filter(CompanyId=validated_data["Company_id"]).first()
        businessUnit = BusinessUnit.objects.filter(BusinessUnitId=validated_data["BusinessUnit_id"]).first()
        location = Location.objects.filter(LocationId=validated_data["Location_id"]).first()
        experience = Experience.objects.filter(ExperienceLevelId=validated_data["ExperianceLevel_id"]).first()
        user = User.objects.get(username=validated_data["UserName"])
        max =  JobPost.objects.all().aggregate(Max('JobPostId'))
        count = JobPost.objects.count()
        # print(max11)
        # aggregate(Max('JobPostId'))
        # if max['JobPostId__max'] is None:
        #     maxvalue = 1
        # else:    
        #     maxvalue =  max['JobPostId__max']+1 
        maxvaluepad = str(count+1).zfill(5)
        if serviceline and customer :
            jobcode =  serviceline.Acronym+"-"+customer.Acronym+"-"+maxvaluepad

        CreatedOn = datetime.now()
        # ModifiedBy = None
        ModifiedOn = None
        # validated_data["serviceline"] = serviceline
        # validated_data["customer"] = customer
        # validated_data["Stage"] = stage
        # validated_data["Company"] = company
        # validated_data["BusinessUnit"] = businessUnit
        # validated_data["Location"] = location
        # validated_data["ExperianceLevel"] = experience
                        
        jobpost = JobPost.objects.create(
            JobCode = jobcode,
            UserName =  validated_data["UserName"],
            FirstName = user.first_name,
            LastName = user.last_name,
            Email = user.email,
            Stage = stage,
            Industry = industry,
            Company = company,
            BusinessUnit = businessUnit,
            ServiceLine = serviceline,
            Customer = customer,
            Location = location,
            EmploymentType = validated_data["EmploymentType"],
            Duration = validated_data["Duration"],
            JobTitle =validated_data["JobTitle"],
            JobDesc =validated_data["JobDesc"],
            NoOfPositions = validated_data["NoOfPositions"],
            ExperianceLevel = experience,
            Qualification = validated_data["Qualification"],
            OnBoardingDate = validated_data["OnBoardingDate"],
            POReference = validated_data["POReference"],
            CreatedBy = validated_data["CreatedBy"],
            CreatedOn = CreatedOn,
            ModifiedBy = validated_data["ModifiedBy"],
            ModifiedOn = ModifiedOn
        )
        return jobpost

    class Meta:
        model = JobPost
        fields = [
            "UserName",
            # "FirstName",
            # "LastName",
            # "Email",
            "EmploymentType",
            "Duration",
            "JobTitle",
            "JobDesc",
            "NoOfPositions",
            "Qualification",
            "OnBoardingDate",
            "POReference",
            # "Stage",
            # "Company",
            # "BusinessUnit",
            # "ServiceLine",
            # "Customer",
            # "Location",
            # "ExperianceLevel",
            #"Stage_id",
            "Industry_id",
            "Company_id",
            "BusinessUnit_id", 
            "Serviceline_id" ,
            "Customer_id" ,
            "Location_id" ,
            "ExperianceLevel_id" ,     
            "CreatedBy",
            "ModifiedBy",
            "BH_User_Name",
            "HR_User_Name"
        ]
        required_fields = fields


class  JobPostApprovalSerializer(serializers.ModelSerializer):


    class Meta:
        model = JobPostApproval
        fields = "__all__"

class  JobPostActionModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPostActionModel
        fields = "__all__"

class  JobPostUserRolesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobPostUserRolesModel
        fields = ["RoleName","UserName", "FullName"]
        