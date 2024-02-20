import pkgutil  
from fastapi import FastAPI  
from importlib import import_module  
  
app = FastAPI()  
  
# Automatically import all routers from the 'api' folder  
package_name = "api"  
package = import_module(package_name)  
  
for _, module_name, _ in pkgutil.iter_modules(package.__path__):  
    module = import_module(f"{package_name}.{module_name}")  
    if hasattr(module, "router"):  
        app.include_router(module.router)  
  
if __name__ == "__main__":  
    import uvicorn  
  
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")  
