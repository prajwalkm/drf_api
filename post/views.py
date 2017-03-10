from django.shortcuts import render

from rest_framework import mixins
from .models import User
from rest_framework import generics
from .serializers import UserSerializer,UserCreateSerializer
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import redirect

from .models import User
from .mixins import LoginRequiredMixin
from django.views import View

# Create your views here.



#registers User using API
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class=UserCreateSerializer
    queryset=User.objects.all()



def welcome(request):
    queryset=User.objects.get(email=request.user)
    template_name = 'welcome.html'
    context={
    'user':queryset
    }

    # def get(self, request):
    #     queryset = get_object_or_404(User, pk=self.request.user.id)
    #     return Response({'users': queryset})
    return render(request,template_name,context)


# class welcome(View,LoginRequiredMixin):
#     model=User
#     queryset=User.objects.all()
#     def get_context_data(self,request,*args,**kwargs):
#         context=super(CategoryDetailView,self).get_context_data(*args,**kwargs)
#         qs=User.objects.get(email=request.user)
#         context["user"]=qs
#         return context

#API used to fetch user detail and Update(Edit)
class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'edit.html'

    def get(self, request, pk):
        profile = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('welcome')




class UserCreateView(generics.CreateAPIView):
    serializer_class=UserSerializer

class UserListView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDeleteView(generics.RetrieveDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

def home(request):
    template='index.html'
    return render(request,template,{})
