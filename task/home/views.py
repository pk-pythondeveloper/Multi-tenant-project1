from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()  
    serializer_class = ProductSerializer

    def get_queryset(self):
        # i done the Dynamically filter the queryset based on the tenant
        if self.request.tenant:
            return Product.objects.filter(tenant=self.request.tenant)
        return Product.objects.none()

    def perform_create(self, serializer):
        # here atomatacilly called tanant during creation
        serializer.save(tenant=self.request.tenant)
