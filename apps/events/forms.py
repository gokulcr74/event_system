
from django import forms 
from apps.events.models  import UserPost
class UploadForm(forms.ModelForm): 
    description=forms.CharField( widget=forms.Textarea(attrs={'width':"50%", 'cols' : "80", 'rows': "3","placeholder":"Whats in your mind today?" }),required=True )
    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].label = "description"
        self.fields['description'].label = False
        self.fields['image'].widget.attrs.update({"id":"upload","class":"form-control","class":"imageUploadBtn" })
        self.fields['image'].required = True
        self.fields['image'].label = "Upload Image"
    class Meta: 
        model =UserPost
        fields = ['description','image'] 
        