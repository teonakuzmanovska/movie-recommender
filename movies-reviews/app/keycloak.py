# from keycloak import KeycloakOpenID
# from app.settings import *
# from keycloak.exceptions import KeycloakInvalidTokenError
# from fastapi import HTTPException
# from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm


# # Initialize the KeycloakOpenID instance (use your actual Keycloak configuration)
# # keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_SERVER_URL,
# #                                  client_id=KEYCLOAK_CLIENT_ID,
# #                                  realm_name=KEYCLOAK_REALM)

# # Define OAuth2PasswordBearer for token retrieval
# # oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{KEYCLOAK_SERVER_URL}/protocol/openid-connect/token")

# # def authenticate_keycloak(token: str):
# #     try:
# #         # Validate the token and retrieve user information
# #         userinfo = keycloak_openid.userinfo(token)
        
# #         # If validation is successful, return the user information
# #         return userinfo

# #     except KeycloakInvalidTokenError:
# #         raise HTTPException(
# #             status_code=401,
# #             detail="Invalid or expired Keycloak token",
# #             headers={"WWW-Authenticate": "Bearer realm='Keycloak'"},
# #         )
        