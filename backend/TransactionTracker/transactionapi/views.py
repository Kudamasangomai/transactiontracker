
from rest_framework import status
from .models import Transactions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TransactionsSerializer


@api_view(['GET'])
def getroutes(request):
	routes =[
	'api/transactions/',
	'api/login/',
	]
	return Response(routes)

@api_view(['POST'])
def login(request):
    """ Simple login endpoint checking against hardcoded credentials. """
    username = "username"
    password = "password"

    if username == "username" and password == "password":
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST'])
def transactions(request):
       
        if request.method == 'GET':
            transaction_list = Transactions.objects.all()
            serializer = TransactionsSerializer(transaction_list, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = TransactionsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

