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
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from fpdf import FPDF,HTMLMixin

# Create your views here.
class PDFGeneration(ModelViewSet):
    @action(detail=True, methods=['post'])
    def jdpdf(self, request, format=None):   

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

        # Min_Experience_Range = jobpostdata.MinimumExperiance

        # Max_Experience_Range = jobpostdata.MaximumExperiance

        Experience_Range = str(jobpostdata.MinimumExperiance) + '-' + str(jobpostdata.MaximumExperiance)



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

            Story.append(Paragraph(ptext, TEXT_STYLE))

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

    

        ptext = "<b>" + 'Experience Range:' + "</b>" '%s' % str(Experience_Range) +' Years'

        Story.append(Paragraph(ptext, styles["Normal"]))

        Story.append(Spacer(1, 12))

    

        doc.build(Story)



        # x.showPage()

        # x.save()

        buffer.seek(0)

        data = base64.b64encode(buffer.getvalue())

        print(data)

        return HttpResponse(data)

    @action(detail=True, methods=['post'])
    def offerletterpdf(self, request, format=None):
        data = (
            ("First name", "Last name", "Age", "City"),
            ("Jules", "Smith", "34", "San Juan"),
            ("Mary", "Ramos", "45", "Orlando"),
            ("Carlson", "Banks", "19", "Los Angeles"),
            ("Lucas", "Cimon", "31", "Saint-Mahturin-sur-Loire"),
        )
        pdf = PDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_margins(0, 0, 0)

        pdf.set_font('Times', '', 12)
        pdf.cell(210, 10, 'Powered by FPDF.', 0, 0, 'C')
        pdf.write_html(
   """
<H1 align="center">html2fpdf</H1>
<h2>Basic usage</h2>
<p>You can now easily print text mixing different
styles : <B>bold</B>, <I>italic</I>, <U>underlined</U>, or
<B><I><U>all at once</U></I></B>!<BR>You can also insert links
on text, such as <A HREF="http://www.fpdf.org">www.fpdf.org</A>,
or on an image: click on the logo.<br>
<center>
<A HREF="http://www.fpdf.org"><img src="tutorial/logo.png" width="104" height="71"></A>
</center>
<h3>Sample List</h3>
<ul><li>option 1</li>
<ol><li>option 2</li></ol>
<li>option 3</li></ul>

<table border="0" align="center" width="50%">
<thead><tr><th width="30%">Header 1</th><th width="70%">header 2</th></tr></thead>
<tbody>
<tr><td>cell 1</td><td>cell 2</td></tr>
<tr><td>cell 2</td><td>cell 3</td></tr>
</tbody>
</table>
"""

            )
        pdf.output('sample.pdf', 'F')  
        return HttpResponse("asasas")

class PDF(FPDF, HTMLMixin):
    def header(self):
        # Select Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Framed title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Print centered page number
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')