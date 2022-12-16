from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from CandidateFeedback.serializers.AddFeedBackSerializer import AddFeedBackSerializer

# class AddFeedBack(APIView):
#     def post(self,request,format=None):
#         try:
#             print("working")
#             print(request.data)
#             res={"data":"working"}
#             return Response(res.data)
#         except:
#             return Response("failed",status=status.HTTP_400_BAD_REQUEST)

class AddFeedBack(generics.ListCreateAPIView):  
    serializer_class = AddFeedBackSerializer 

    def get_serializer(self, *args, **kwargs):  
        if isinstance(kwargs.get("data", {}), list):  
            kwargs["many"] = True  

        return super(AddFeedBack, self).get_serializer(*args, **kwargs) 
