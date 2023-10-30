from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms

from website import settings
from .models import FeedBack

class CreateFeedBackForm(forms.ModelForm):

    class Meta:
        model = FeedBack
        fields = ('subject', 'email', 'content')

    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, public_key=settings.RECAPTCHA_PUBLIC_KEY, private_key=settings.RECAPTCHA_PRIVATE_KEY, label='Капча')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

class SearchForm(forms.Form):

    query = forms.CharField(label='Поиск по сайту', max_length=100)