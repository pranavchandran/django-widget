from django import forms

class contactForm(forms.Form):
    name = forms.CharField(error_messages={'required':'Please enter your name'},
                            initial='very sensitive',widget=forms.TextInput(attrs={}))
    email = forms.EmailField(help_text='valid email address required')
    message = forms.CharField(widget=forms.Textarea(
                                attrs={
                                    'placeholder':'Message minm 150',
                                    'class':'new-class',
                                    'rows' : 6,
                                    'cols' : 25,

                                }

                            ))
    cc_myself = forms.BooleanField(required=False)
