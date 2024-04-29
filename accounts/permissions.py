from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsVendor(BasePermission):
    """
    Custom permission to check if the user is a vendor.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a vendor
        return request.user.is_authenticated and hasattr(request.user, 'vendorinformation')


class IsAdminOrVendor(BasePermission):
    """
    Custom permission to check if the user is a vendor.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a vendor
        return request.user.is_authenticated and (request.user.is_superuser or hasattr(request.user, 'vendor'))


class IsAdminOrVendorOrReadOnly(BasePermission):
    """
    Custom permission to check if the user is a vendor.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a vendor
        return request.method in SAFE_METHODS or request.user.is_authenticated and (request.user.is_superuser or hasattr(request.user, 'vendorinformation'))


class IsAdminOrUnAthenticatedUser(BasePermission):
    """
    Custom permission to check if the user is a vendor.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a vendor
        return not request.user.is_authenticated or request.user.is_superuser

class IsAdminOrUserSelf(BasePermission):
    """
    Custom permission to check if the user is a vendor.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a vendor
        # return request.user.is_authenticated and (request.user.is_superuser or request.user == view.get_object())
        return request.user.is_authenticated and (request.user.is_superuser or hasattr(request.user, 'vendor'))


class IsCustomer(BasePermission):
  """
  Permission to check if user belongs to the 'Customer' role.
  """
  def has_permission(self, request, view):
    # Access user object from request
    user = request.user
    # Check if user is authenticated and has the specific role
    return user.is_authenticated and user.role == 'customer'

  # Optionally define a message to be displayed if permission is denied
  message = "User must be a customer to access this resource."
