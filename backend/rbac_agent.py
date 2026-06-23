def get_permissions(role):

    permissions = {

        "ADMIN": [
            "VIEW_CASES",
            "APPROVE_CASES",
            "MANAGE_USERS",
            "VIEW_LOGS"
        ],

        "AUDITOR": [
            "VIEW_CASES",
            "ADD_NOTES",
            "VIEW_LOGS"
        ],

        "ACCOUNTANT": [
            "VIEW_CASES",
            "ADD_NOTES"
        ]
    }

    return permissions.get(role, [])

def has_permission(role, permission):

    permissions = get_permissions(role)

    return permission in permissions