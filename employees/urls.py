from django.urls import path, include
from employees.views import employee_view
from rest_framework.routers import DefaultRouter

# Create a router and register EmployeeViewSet with it.
router = DefaultRouter()
router.register(r'employees', employee_view.EmployeeViewSet, basename='Employee')

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
