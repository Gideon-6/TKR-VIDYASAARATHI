from django import forms
from .models import upload_units
from ckeditor.widgets import CKEditorWidget

class UploadUnitsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(), required=True)

    class Meta:
        model = upload_units
        fields = ['content', 'pdf']

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        pdf = cleaned_data.get('pdf')

        if not content:
            raise forms.ValidationError("Unit content is required.")
        if not pdf:
            raise forms.ValidationError("PDF upload is required.")
