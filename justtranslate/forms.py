from django import forms

class AddArticleForm(forms.Form):
    article = forms.CharField(widget=forms.Textarea)