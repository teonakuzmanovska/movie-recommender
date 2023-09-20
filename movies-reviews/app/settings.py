import os
import httpx

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
KEYCLOAK_REALM = "movies-reviews"
KEYCLOAK_CLIENT_ID = "movies-reviews-client"
KEYCLOAK_SERVER_URL = "http://keycloak:8080/auth/realms/movies-reviews"

# async def get_access_token():
#     token_url = f"{KEYCLOAK_SERVER_URL}/protocol/openid-connect/token"
#     data = {
#         "grant_type": "implicit",
#         "client_id": KEYCLOAK_CLIENT_ID,
#     }

#     async with httpx.AsyncClient() as client:
#         response = await client.post(token_url, data=data)

#         if response.status_code == 200:
#             token_data = response.json()
#             access_token = token_data.get("access_token")
#             return access_token
#         else:
#             # Handle error response here
#             return None