from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework_roles.roles import is_user, is_anon, is_admin
from django.core.exceptions import MultipleObjectsReturned

CUSTOMER_ROLE = "customer"
VENDOR_ROLE = "vendor"

ADDITIONAL_ROLES = [
        CUSTOMER_ROLE,
        VENDOR_ROLE,
        ]

def any_handler(request, view):
    return True

def IsOwnerWrapper(ownership = VENDOR_ROLE):
        class IsOwnerOrReadOnly(BasePermission):
               """
               Permission class to allow access to owners or read-only requests.
                """
               def has_object_permission(self, request, view):
                        try:
                               obj = view.get_object()
                        except (AttributeError, MultipleObjectsReturned):
                               return False

                        return object.get(ownership) == request.user

               def has_permission(self, request, view):
                        return request.method in SAFE_METHODS or (
                                request.user.is_authenticated and
                                self.has_object_permission(request, view)
                                )


        return IsOwnerOrReadOnly

def is_admin_or_vendor_owner(request, view):
      """
    Function to check for admin or owner role.
    """
      # Leverage the built-in is_admin function
      return True \
        if is_admin(request=request, view=view) \
                else IsOwnerWrapper(ownership=VENDOR_ROLE)().has_permission(request, view)


def is_admin_or_customer_owner(request, view):
      """
    Function to check for admin or owner role.
    """
      # Leverage the built-in is_admin function
      return True \
        if is_admin(request=request, view=view) \
                else IsOwnerWrapper(ownership = CUSTOMER_ROLE)().has_permission(request, view)


def admin_or_vendor(request, view):
    return request.user.is_authenticated and (request.user.is_superuser or request.user.groups.filter(name = VENDOR_ROLE).exists())

# function to generate handler for each and every additional roles
def role_factory(role_name):
        return lambda request, view: is_user(request, view) and request.user.groups.filter(name = role_name).exists()

ROLES = {
                # Django out-of-the-box
                'admin': is_admin,
                'anon': is_anon,
                'user': is_user,

                # Some custom role examples
                "is_admin_or_customer_owner": is_admin_or_customer_owner,
                "is_admin_or_vendor_owner": is_admin_or_vendor_owner,
                "admin_or_vendor":admin_or_vendor,
                "any": any_handler,
                **{
                        key: role_factory(role_name = key)
                                for key in ADDITIONAL_ROLES
                }
}