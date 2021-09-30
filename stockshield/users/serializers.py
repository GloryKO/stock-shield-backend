from allauth.account.adapter import get_adapter
from .models import User,BusinessId
from rest_framework import serializers
from rest_auth.registration.serializers import  RegisterSerializer
from rest_auth.serializers import LoginSerializer, PasswordChangeSerializer
from dj_rest_auth.serializers import PasswordChangeSerializer,PasswordResetSerializer
from allauth.account.utils import setup_user_email


class UserRegisterSerializer(RegisterSerializer):
    business_name = serializers.CharField()
    is_administrator = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = ('id','email','username','business_name','is_administrator')



    def get_cleaned_data(self):
        super(UserRegisterSerializer,self).get_cleaned_data
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'business_name': self.validated_data.get('business_name', ''),
            'is_administrator': self.validated_data.get('is_administrator', ''),
            
        }

    def save(self, request):
       
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        print(self.cleaned_data)
        adapter.save_user(request,user,self)
        setup_user_email(request, user, [])

        business = BusinessId()
        business.business_name = self.cleaned_data.get('business_name')
        business.save()
        user.is_administrator = self.cleaned_data.get('is_administrator')
        user.business = business
        user.save()
       
        return user

class UserLoginSerializer(LoginSerializer):
    class Meta:
        ref_name = "login"


class UserPasswordChangeSerializer(PasswordChangeSerializer):
    class Meta:
        ref_name = "admin user"

class UserPasswordResetSerializer(PasswordResetSerializer):
    class Meta:
        ref_name = "admin user"



