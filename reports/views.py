import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from students.models import Student
from teachers.models import Teacher
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def generate_report(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    # Header
    p.setFont("Helvetica-Bold", 24)
    p.setFillColorRGB(0.3, 0.27, 0.9)  # Primary color approx #4F46E5
    p.drawString(150, 750, "EduCore Academic System Report")
    
    # Subheader
    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)
    p.drawString(220, 730, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    p.line(50, 710, 550, 710)
    
    # Fetch Data securely
    try:
        students_count = Student.objects.count()
        teachers_count = Teacher.objects.count()
    except Exception:
        students_count = 0
        teachers_count = 0
        
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, 660, "System Overview Statistics")
    
    p.setFont("Helvetica", 14)
    p.drawString(70, 630, f"• Total Active Students: {students_count}")
    p.drawString(70, 600, f"• Total Faculty Members: {teachers_count}")
    
    p.setFont("Helvetica-Oblique", 12)
    p.setFillColor(colors.gray)
    p.drawString(50, 100, "This is an automatically generated system report by EduCore Platform.")
    
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='EduCore_Report.pdf')
