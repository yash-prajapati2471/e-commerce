from django import forms
from account.models import account

class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formcontrol'}))
    con_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formcontrol'}))

    class Meta:
        model = account
        fields = ['firstname','lastname','email','phone','password','con_password']

    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        password = cleaned_data.get(password)
        con_password = cleaned_data.get(con_password)

        if password != con_password:
            raise forms.ValidationError("Password and Confirmpassword not match.")
        
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['firstname'].widget.attrs['placeholder'] = "Firstname"
        self.fields['lastname'].widget.attrs['placeholder'] = "Lastname"
        self.fields['email'].widget.attrs['placeholder'] = "Email"

        for i in self.fields:
            self.fields[i].widget.attrs['class'] = "form-control"
        
        
        
