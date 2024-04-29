from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework_roles.roles import is_user, is_anon, is_admin

CUSTOMER_ROLE = "customer"
VENDOR_ROLE = "vendor"

ADDITIONAL_ROLES = [
        CUSTOMER_ROLE,
        VENDOR_ROLE,
        ]

def any_handler(request, view):
    return True

class IsOwnerOrReadOnly(BasePermission):
    """
    Permission class to allow access to owners or read-only requests.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(view, 'get_object') and  # Check if a view method has 'get_object'
            (view.get_object().owner == request.user or request.method in SAFE_METHODS)
        )

def is_admin_or_owner(request, view):
      """
    Function to check for admin or owner role.
    """
      permission = IsOwnerOrReadOnly()
      if is_admin(request=request, view=view):  # Leverage the built-in is_admin function
        return True

      return permission.has_permission(request, view)


# function to generate handler for each and every additional roles
def role_factory(role_name):
        return lambda request, view: is_user(request, view) and request.user.groups.filter(name = role_name).exists()

ROLES = {
                # Django out-of-the-box
                'admin': is_admin,
                'anon': is_anon,
                'user': is_user,

                # Some custom role examples
                "admin_or_owner": is_admin_or_owner,
                "any": any_handler,
                **{
                        key: role_factory(role_name = key)
                                for key in ADDITIONAL_ROLES
                }
}