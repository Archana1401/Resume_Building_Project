from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from .forms import ResumeForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


#  LIST PAGE
def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'list.html', {'resumes': resumes})


#  CREATE
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save()
            return redirect('download', id=resume.id)
    else:
        form = ResumeForm()

    return render(request, 'form.html', {'form': form})

def view_resume(request, id):
    resume = Resume.objects.get(id=id)
    return render(request, 'display.html', {'resume': resume})


#  EDIT
def edit_resume(request, id):
    resume = get_object_or_404(Resume, id=id)

    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ResumeForm(instance=resume)

    return render(request, 'form.html', {'form': form})


#  DELETE
def delete_resume(request, id):
    resume = get_object_or_404(Resume, id=id)
    resume.delete()
    return redirect('list')


#  DOWNLOAD
def download_pdf(request, id):
    resume = Resume.objects.get(id=id)

    template = get_template('pdf.html')
    html = template.render({'resume': resume})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    pisa.CreatePDF(html, dest=response)
    return response