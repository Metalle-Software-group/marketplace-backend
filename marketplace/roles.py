from rest_framework_roles.roles import is_user, is_anon, is_admin

ADDITIONAL_ROLES = [
        "customer",
        "vendor"
        ]

def any_handler(request, view):
    return True
# function to generate handler for each and every additional roles
def role_factory(role_name):
        return lambda request, view: is_user(request, view) and request.user.groups.filter(name = role_name)

ROLES = {
                # Django out-of-the-box
                "any": any_handler,
                'admin': is_admin,
                'anon': is_anon,
                'user': is_user,
                # Some custom role examples
                **{
                        key: role_factory(role_name = key)
                                for key in ADDITIONAL_ROLES
                }
}