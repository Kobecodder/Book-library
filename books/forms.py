
from django import forms
from django.forms import ModelForm
from models import Books, Subscriber
from django.utils.safestring import mark_safe


class BooksForm(ModelForm):
    class Meta:
        model = Books
        # fields = ['book_catagory', 'book_title', 'book_author_name', 'book_author_profession', 'book_cover_image', 'book_upload', 'book_overview']


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscriber


class UploadForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    attach = forms.FileField(widget = forms.FileInput)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)












