from .models import User
from rest_framework import serializers
import random





class UserCreateSerializer(serializers.ModelSerializer):

    password=serializers.HiddenField(default='123')
    OTP=serializers.HiddenField(default='123')
    # email=serializers.EmailField()

    class Meta:
        model=User
        fields=['email','password','OTP']
        extra_kwargs={"password":{"write_only":True} }


    # def validate_email(self,value):
    #     value=self.get_initial()
    #     email=value.get('email')
    #     num=random.randrange(100,10000,3)
    #     User_obj,created=User.objects.get_or_create(email=email)
    #     if created:
    #         User_obj.OTP=num
    #         User_obj.set_password(email)
    #         User_obj.save()
    #     else:
    #         User_obj.OTP=num
    #         User_obj.save()
    #     return value

    # def Update(self,validated_data):
    #     num=random.randrange(100,10000,3)
    #     print(num)
    #     email=validated_data['email']
    #     password=validated_data['email']
    #     User_obj,created=User.objects.get_or_create(email=email)
    #     if created:
    #         User_obj.OTP=num
    #         User_obj.set_password(password)
    #         User_obj.save()
    #     else:
    #         User_obj.OTP=num
    #         User_obj.save()
    #     return validated_data

    def create(self,validated_data):
        num=random.randrange(100,10000,3)
        email=validated_data['email']
        password=validated_data['email']
        User_obj=User(email=email,OTP=num)
        User_obj.set_password(password)
        User_obj.save()
        return validated_data

    # def Update(self,instance,validated_data):
    #     num=random.randrange(100,10000,3)
    #     instance.OTP=str(num)
    #     instance.save()
    #     return instance
    #







class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields=('first_name','last_name','father_name','gender','phone','email','spouse_name',)
