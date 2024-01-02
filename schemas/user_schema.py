def user_schema(user) -> dict:
    return {
        "id": user["_id"],
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
    }
