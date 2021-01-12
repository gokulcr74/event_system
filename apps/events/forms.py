
from django import forms 
from apps.events.models  import UserPost


class DateInput(forms.DateInput):
    input_type = 'date'


class UploadForm(forms.ModelForm): 
    description=forms.CharField( widget=forms.Textarea(attrs={'width':"50%", 'cols' : "80", 'rows': "3","placeholder":"description of your event?" }),required=True )
    event_place=forms.CharField()
    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
       # self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].label = "description"
        self.fields['description'].label = False
        #self.fields['event_place'].widget.attrs.update({'class': 'form-control'})
        self.fields['event_place'].label = "place"
        self.fields['event_start_date'].label = "event_start_date"
        #self.fields['event_start_date'].widget.attrs.update({'class': 'form-control'})
        #self.fields['event_end_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['event_end_date'].label = "event end date"
        #self.fields['image'].widget.attrs.update({"id":"upload","class":"form-control","class":"imageUploadBtn" })
        self.fields['image'].required = True
        self.fields['image'].label = "Upload Image"
    class Meta: 
        model =UserPost
        fields = ['description','event_place','event_start_date','event_end_date','image'] 
        widgets = {
            'event_start_date':  DateInput(),
            'event_end_date':  DateInput(),
        }
