from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import UploadFileForm
import pandas as pd

def handle_uploaded_file(f):
    df = pd.read_excel(f)
    summary = df.groupby(['Cust State', 'DPD']).size().reset_index(name='Count')
    return summary

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            summary = handle_uploaded_file(request.FILES['file'])
            send_mail(
                'Summary Report',
                summary.to_string(),
                'your_email@example.com',
                ['tech@themedius.ai', 'hr@themedius.ai'],
            )
            return render(request, 'myapp/success.html', {'summary': summary})
    else:
        form = UploadFileForm()
    return render(request, 'myapp/upload.html', {'form': form})
