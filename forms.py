from django import forms

from .models import Poll, Announcement  



class PollForm(forms.ModelForm):
    # this we will access in the template view, the text in the header and in the submit button
    template_name = "Create Poll"

    class Meta:
        model = Poll   
        # we only want to get the title here
        fields = ['title']   



class AnnouncementForm(forms.ModelForm):
    # same goes here 
    template_name = "Create Announcement"

    class Meta:
        model = Announcement      
        # we only want to get the title field
        fields = ['title']   