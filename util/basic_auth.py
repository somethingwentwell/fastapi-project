from fastapi import Depends, HTTPException  
from fastapi.security import HTTPBasic, HTTPBasicCredentials  
  
security = HTTPBasic()  
  
def basic_auth(credentials: HTTPBasicCredentials = Depends(security)):  
    if credentials.username == "user" and credentials.password == "pass":  
        return  
    raise HTTPException(status_code=401, detail="Invalid credentials")  
