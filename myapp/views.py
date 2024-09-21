from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login
from mytest.serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from mytest.serializers import ProductsSerializer,UserSerializer,CartSerializer,CartItemSerializer
from myapp.models import Products,User,Cart,CartItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
# Signup API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "token": Token.objects.create(user=user).key
        })

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key,
            
        })


@csrf_exempt   
# class dipesh(APIView): 
def dipesh(request):
    if request.method=='GET':
        student = Products.objects.all()
        student_serializer=ProductsSerializer(student,many=True)
        return JsonResponse(student_serializer.data,safe=False)
        
@csrf_exempt
# class StudentApi(APIView):
def StudentApi(request):
    if request.method=='GET':
        student = User.objects.all()
        student_serializer=UserSerializer(student,many=True)
        return JsonResponse(student_serializer.data,safe=False)
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        print(student_data)
        student_serializer=UserSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=User.objects.get(id=id)
        student_serializer=UserSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        student=User.objects.get(id=id)
        student.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
@csrf_exempt    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    user = request.user
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)
    
    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=user)
        product = Products.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity = quantity
        cart_item.save()

        return Response({'message': 'Product added to cart!'}, status=status.HTTP_200_OK)
    return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart_items(request):
    user = request.user
    if user.is_authenticated:
        cart = Cart.objects.get(user=user)
        serializer = CartSerializer(cart)
        print(serializer.data)
        return Response(serializer.data)
    return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_cart_item(request, item_id):
    try:
        cart = Cart.objects.get(user=request.user)
        print(f"User's cart: {cart}")
        cart_item = CartItem.objects.get(id=item_id, cart=cart)
        print(f"Item to delete: {cart_item}")
        cart_item.delete()
        return Response({"message": "Item removed"}, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
