from django import forms

class AddArticleForm(forms.Form):
    article_name = forms.CharField(label='Article Name')
    article = forms.CharField(widget=forms.Textarea)