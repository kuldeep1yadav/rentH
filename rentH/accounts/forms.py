from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from . models import User


# # class LoginForm(forms.Form):
# #     username = forms.CharField(
# #         widget= forms.TextInput(
# #             attrs={
# #                 "class": "form-control"
# #             }
# #         )
# #     )
# #     password = forms.CharField(
# #         widget=forms.PasswordInput(
# #             attrs={
# #                 "class": "form-control"
# #             }
# #         )
# #     )


# # class SignUpForm(UserCreationForm):
# #     username = forms.CharField(
# #         widget=forms.TextInput(
# #             attrs={
# #                 "class": "form-control"
# #             }
# #         )
# #     )
# #     password1 = forms.CharField(
# #         widget=forms.PasswordInput(
# #             attrs={
# #                 "class": "form-control"
# #             }
# #         )
# #     )
# #     password2 = forms.CharField(
# #         widget=forms.PasswordInput(
# #             attrs={
# #                 "class": "form-control"
# #             }
# #         )
# #     )
# #     email = forms.CharField(
# #         widget=forms.TextInput(
# #             attrs={
# #                 "class": "form-control"
# #             }
# #         )
# #     )

# #     class Meta:
# #         model = User
# #         fields = ('username', 'email', 'password1', 'password2', 'is_employee', 'is_customer')

# class ClientRegisterForm(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("This email is already registered.")
#         return email

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords do not match.")
#         return password2

#     def save(self, commit=True):
#         user = super(ClientRegisterForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user   
     
# class OwnerRegisterForm(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User