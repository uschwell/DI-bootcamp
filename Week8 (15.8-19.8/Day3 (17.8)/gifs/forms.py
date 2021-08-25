from django import forms
 
# creating a form
class GifForm(forms.Form):
 
    uploader_name = forms.CharField(max_length = 200)
    title = forms.CharField(max_length = 200)
    url = forms.URLField(default='https://giphy.com/gifs/Friends-friends-episode-2-tv-H7IA7tNxNnCMdhhZPy')
    categories = forms.ModelMultipleChoiceField(queryset=None)

    class CategoryForm(forms.Form):
        name = forms.CharField(max_length = 200)