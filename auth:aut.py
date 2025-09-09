def authenticate_user(username):
    print(f"Authenticating {username} with Azure AD...")
    # TODO: integrate Azure AD
    return True

if __name__ == "__main__":
    user = "test_user"
    authenticated = authenticate_user(user)
    print("Authentication success!" if authenticated else "Failed")
