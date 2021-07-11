from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

def accept(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        github = request.POST.get('github','')
        summary = request.POST.get('summary','')
        experience = request.POST.get('experience','')
        phone = request.POST.get('phone','')
        degree = request.POST.get('degree','')
        SSC = request.POST.get('SSC','')
        HSC = request.POST.get('HSC','')
        university = request.POST.get('university','')
        skills = request.POST.get('skills','')
        codingprofile = request.POST.get('codingprofile','')

        profile = Profile(name=name,email=email,summary=summary,experience=experience,phone= phone,degree=degree,SSC=SSC,HSC=HSC,github=github,codingprofile=codingprofile,university=university,skills=skills)
        profile.save()
    return render(request,'pdf/about.html')


def resume(request,id):
    #same as before
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'enable-local-file-access': None,    # add this new option
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    #SET TO UR PATH

    config = pdfkit.configuration(wkhtmltopdf='C:\\wkhtmltox\\bin\\wkhtmltopdf.exe')  
    filename = user_profile.name + " resume.pdf"
    pdf = pdfkit.from_string(html,False,options,configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')    
    response['Content-Disposition'] = 'attachment ; filename =' + filename 
    return response 

def list(request):
    profiles = Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})    
