"""HRproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

#swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="HRPROJECT API",
      default_version='v1',
      description="Hr worlflow",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/company', include('managecompany.urls')),
     path('api/businessunit', include('managebusinessunit.urls')),
     path('api/serviceline', include('manageserviceline.urls')),
     path('api/Customer', include('ManageCustomer.urls')),
     path('api/Location', include('ManageLocation.urls')),
     path('api/Experience', include('ManageExperienceLevel.urls')),
     path('api/Designation', include('ManageDesignation.urls')),
     path('api/Band', include('ManageBand.urls')),
     path('api/SubBand', include('ManageSubBand.urls')),
     path('api/AvgCTC', include('ManageAvgCTC.urls')),
     path('api/Insurance', include('ManageInsurance.urls')),
     path('api/Roles', include('manageroles.urls')),
     path('api/UserRoles', include('ManageUserRoles.urls')),
     path('api/Industry', include('ManageIndustry.urls')),
     path('api/AdUsers', include('ManageAdUsers.urls')),
        path('api/stage', include('managestages.urls')),
        path('api/login', include('login.urls')),

     path('api/jobpost', include('jobpost.urls')),
     path('api/candidate', include('candidate.urls')),
     path('api/pdf', include('pdf.urls')),
    #  path('api/candidateFeedback', include('CandidateFeedback.urls')),
     path('api/Employementtype', include('Employementtype.urls')),
     path('api/Qualification', include('Qualification.urls')),
     path('api/Outlook', include('Outlook.urls')),
     path('api/selectedcandidate', include('selectedcandidate.urls')),




#swagger urls
   path('swagger1(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),

   path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   
]


