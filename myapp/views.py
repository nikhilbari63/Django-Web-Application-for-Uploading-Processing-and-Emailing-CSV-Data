
import pandas as pd
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import UploadFileForm

def handle_uploaded_file(file):
    if file.name.endswith('.csv'):
        data = pd.read_csv(file)
    elif file.name.endswith(('.xls', '.xlsx')):
        data = pd.read_excel(file)
    else:
        raise ValueError('Unsupported file format')

    summary = data.groupby(['Cust State', 'DPD']).size().reset_index(name='Count')
    return summary

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            summary = handle_uploaded_file(request.FILES['file'])
            # Email the summary
            send_mail(
                'Summary Report',
                summary.to_string(),
                'your-email@example.com',
                ['tech@themedius.ai', 'hr@themedius.ai'],
                fail_silently=False,
            )
            return render(request, 'myapp/success.html', {'summary': summary.to_html()})
    else:
        form = UploadFileForm()
    return render(request, 'myapp/upload.html', {'form': form})
