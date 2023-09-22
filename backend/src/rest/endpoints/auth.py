from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse

# from rest.authentication.auth import auth_handler, users
from ..schemas.auth_details import AuthDetails
# from rest.authentication.auth import include_in_schema_override, auth_dependencies
# from rest.authentication.auth import user_id_provider


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
    # dependencies=auth_dependencies,
    # include_in_schema=include_in_schema_override,
)


@router.post('/register', status_code=201)
def register(auth_details: AuthDetails):
    pass
    # if any(x['username'] == auth_details.username for x in users):
    #     raise HTTPException(status_code=400, detail='Username is taken')
    # hashed_password = auth_handler.get_password_hash(auth_details.password)
    # users.append({'username': auth_details.username, 'password': hashed_password})
    # return {'message': 'User has been registered successfully.'}


@router.post('/login')
def login(auth_details: AuthDetails):
    if auth_details.username == "admin" and auth_details.password == "admin":
        return_data = {'message': 'User has been login successfully.'}
        return JSONResponse(content=return_data, status_code=200, media_type="application/json")
    raise HTTPException(status_code=401, detail='Invalid username and/or password')
    # for x in users:
    #     if x['username'] == auth_details.username:
    #         user = x
    #         break
    #
    # if (user is None) or (
    #     not auth_handler.verify_password(auth_details.password, user['password'])
    # ):
    #     raise HTTPException(status_code=401, detail='Invalid username and/or password')
    # token = auth_handler.encode_token(user['username'])
    # return {'token': token}

