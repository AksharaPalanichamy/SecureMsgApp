from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    plaintext_message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Message
        fields = ['receiver', 'plaintext_message']  # Use plaintext_message instead
