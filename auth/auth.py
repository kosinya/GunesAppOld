from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend

SECRET = "SECRET"
ACCESS_TOKEN_LIFETIME = 86400

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=ACCESS_TOKEN_LIFETIME)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
