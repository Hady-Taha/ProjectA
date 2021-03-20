
from student.models import StudentProfile , StudentAttendence
from webservices.DataAccessLayer.serializers import StudentProfileSerializer  ,StudentAttendenceSerilalizer
from rest_framework.response import Response
from rest_framework import generics     
from rest_framework.decorators import api_view





# Function Based Views

@api_view(['GET'])              #get all Profiles 
def profileListApi(request):
    all_profiles= StudentProfile.objects.all()
    data =  StudentProfileSerializer(all_profiles, many=True).data
    return Response({'data':data})

@api_view(['GET'])              #get Specific Profile
def profile_details_api(request,id):
    profile_details=StudentProfile.objects.get(id=id)
    data =  StudentProfileSerializer(profile_details, many=True).data
    return Response({'data':data})






class profileListApi2(generics.RetrieveUpdateDestroyAPIView):
    model = StudentProfile
    queryset=StudentProfile.objects.all()
    serializer_class=StudentProfileSerializer



class profileDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=StudentProfileSerializer
    queryset=StudentProfile.objects.all()
    lookup_field='id'


#----------------------------------------------------------------------


@api_view(['GET'])
def attendenceListApi(request):
    all_attendence= StudentAttendence.objects.all()
    data =  StudentAttendenceSerilalizer(all_attendence, many=True).data
    return Response({'data':data})




class attendenceListApi2(generics.ListCreateAPIView):
    model = StudentAttendence
    queryset=StudentAttendence.objects.all()
    serializer_class=StudentAttendenceSerilalizer

