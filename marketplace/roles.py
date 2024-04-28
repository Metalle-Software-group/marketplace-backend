from rest_framework_roles.roles import is_user, is_anon, is_admin

ADDITIONAL_ROLES = [
        "customer",
        "vendor"
        ]

# def is_customer(request, view):
#         return is_user(request, view) and request.user.usertype == 'customer'

# def is_vendor(request, view):
#         return is_user(request, view) and request.user.usertype == 'vendor'

def role_factory(role_name = "customer",):
        return lambda request, view: is_user(request, view) and request.user.usertype == role_name

ROLES = {
        **{
                # Django out-of-the-box
                'admin': is_admin,
                'anon': is_anon,
                'user': is_user,

                # Some custom role examples
                # 'customer': role_factory(role_name="customer"),
                # 'vendor': role_factory(role_name="vendor"),
                },
                **{
                        key: role_factory(role_name = key)
                                for key in ADDITIONAL_ROLES
                                }
}