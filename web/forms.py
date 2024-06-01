from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "required form-group",
                       "placeholder": "Your name:",
                    }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "required email form-group",
                    "placeholder": "Your Mail:",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "required form-group",
                    "placeholder": "Enter Your number:",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "required form-group",
                    "placeholder": "Your message:",
                }
            ),
        }