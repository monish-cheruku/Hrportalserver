from msilib.schema import TextStyle
from django.http import HttpResponse
from django.shortcuts import render
import io
# from django.http import FileResponse
from reportlab.pdfgen import canvas
import base64 
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from jobpost.models.jobpostmodel import JobPost
from rest_framework.decorators import api_view
from datetime import datetime

# Create your views here.

@api_view(['POST'])
def PDF(request):

    jobpostdata=JobPost.objects.filter(JobPostId=request.data["JobPostId"])[0]
    # print(jobpostdata.JobDesc)
    # print(jobpostdata.JobDesc.splitlines())

    buffer = io.BytesIO()
    # x = canvas.Canvas(buffer)
    doc = SimpleDocTemplate(buffer,pagesize=letter,
                            rightMargin=55,leftMargin=72,
                            topMargin=45,bottomMargin=18)
    Story=[]
    logo = 'Belcan_Logo.jpg'
    Job_Title = jobpostdata.JobTitle
    Objective = 'Belcan is looking for a %s to work in a dynamic & professional environment, promoting teamwork and using formal development processes.'%(Job_Title)
    Job_Desc =  jobpostdata.JobDesc.splitlines()
    Job_Location = jobpostdata.Location.LocationName
    NoOf_Openings = jobpostdata.NoOfPositions
    jobpostdata.OnBoardingDate=datetime.strptime(str(jobpostdata.OnBoardingDate), "%Y-%m-%d").strftime('%m/%d/%Y')
    OnBoarding_Date = jobpostdata.OnBoardingDate

    im = Image(logo, 6*inch, 0.75*inch, hAlign='LEFT')
    Story.append(im) 
    
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    style_center = ParagraphStyle(name='Job_Title', parent=styles['Normal'], alignment=TA_CENTER)
    TEXT_STYLE = ParagraphStyle(name='Skills', parent=styles['Normal'])
  
    Story.append(Spacer(1, 12))
    ptext = '%s' %  "<strong>" + Job_Title + "</strong>"
    Story.append(Paragraph(ptext, style_center))
    Story.append(Spacer(1, 12))

    ptext = '%s' % Objective 
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))    

    Story.append(Spacer(1, 12))
    ptext =  "<b>" + 'Job Description:' + "</b>" 
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 8))
    for part in Job_Desc:
        ptext = '%s' % part.strip()
        Story.append(Paragraph(ptext, TEXT_STYLE, bulletText='•'))
        Story.append(Spacer(1, 12))

    Story.append(Spacer(1, 12))
    ptext = "<b>" + 'Job Location:' + "</b>" '%s' % Job_Location
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = "<b>" + 'NoOf Openings:' + "</b>" '%s' % NoOf_Openings
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = "<b>" + 'Expected OnBoarding Date:' + "</b>" '%s' % str(OnBoarding_Date)
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12)) 
   
   
    doc.build(Story)

    # x.showPage()
    # x.save()
    buffer.seek(0)
    data = base64.b64encode(buffer.getvalue())
    print(data)
    return HttpResponse(data)



