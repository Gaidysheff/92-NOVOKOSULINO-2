from django.shortcuts import render, redirect
from .forms import UploadFilesMultipleForm
from .models import UploadFilesMultiple


def upload_and_display_files(request):
    files = UploadFilesMultiple.objects.all()

    if request.method == 'POST':
        form = UploadFilesMultipleForm(request.POST, request.FILES)
        if form.is_valid():
            for uploaded_file in request.FILES.getlist('files'):
                UploadFilesMultiple.objects.create(file=uploaded_file)
            return redirect('upload_and_display')
    else:
        form = UploadFilesMultipleForm()

    context = {
        'form': form,
        'files': files,
        'title': 'Загрузка файлов',
    }

    return render(request, 'app_load_multiple/upload_and_display.html', context)


def upload_for_village(request):
    files = UploadFilesMultiple.objects.all()

    if request.method == 'POST':
        form = UploadFilesMultipleForm(request.POST, request.FILES)
        if form.is_valid():
            for uploaded_file in request.FILES.getlist('files'):
                UploadFilesMultiple.objects.create(file=uploaded_file)
            return redirect('upload_for_village')
    else:
        form = UploadFilesMultipleForm()

    context = {
        'form': form,
        'files': files,
        'title': 'Загрузка файлов',
    }

    return render(request, 'app_load_multiple/upload_for_village.html', context)
