from django import forms

class AddArticle(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.HiddenInput)
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)