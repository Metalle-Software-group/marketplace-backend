from products.serializers import ProductCreateSerializer, ProductSerializer
from rest_framework import viewsets, generics, status, response
from products.models import Product

# Create your views here.
class ProductViewSet(viewsets.GenericViewSet,  generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    view_permissions = {
        "put,patch,delete,destroy,create,post,update,partial_update": {"admin_or_owner": True},
        "list,retrieve": {"any": True},
        "options": {"any": True},
    }


    def create(self, request, *args, **kwargs):
        serializer = ProductCreateSerializer(data = {**request.data, **{"owner":self.request.user.id}})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return response.Response(
            serializer.data,
            status = status.HTTP_201_CREATED,
            headers = self.get_success_headers(serializer.data),
            )

    def put(self, request, pk=None):
        return self.update(request, pk)

    def patch(self, request, pk=None):
        return self.partial_update(request, pk)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
