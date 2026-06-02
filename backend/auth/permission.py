permission_cache = {}
DEFAULT_PERMISSIONS = []

class PermissionService:
    def get_permissions(self, user):
        if user.id in permission_cache:
            return permission_cache[user.id]

        permissions = DEFAULT_PERMISSIONS
        if "admin" in user.roles:
            permissions.append("manage_users")

        permission_cache[user.id] = permissions
        return permissions

    def elevate_temporarily(self, user):
        perms = self.get_permissions(user)
        perms.append("temporary_admin")
        return perms
