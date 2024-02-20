from fastapi import APIRouter, Depends  
from util.basic_auth import basic_auth  
  
router = APIRouter()  
  
@router.get("/hello", dependencies=[Depends(basic_auth)])  
async def hello_world():  
    return {"message": "Hello, World!"}  
