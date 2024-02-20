# FastAPI Project  
  
This FastAPI project contains a main app, an API folder with sample APIs, and a util folder with utility functions.  
  
## Project Structure  
  
- main.py: Main FastAPI app, includes APIs from the api folder.  
- api: Contains APIs created by the developer.  
    - hello_world.py: A sample "Hello, World!" API that uses basic authentication as a dependency.  
- util: Contains utility functions, such as authentication.  
    - basic_auth.py: A sample basic authentication function used as a dependency in the APIs.  
  
## Running the Project  
  
1. Activate the virtual environment.  
2. Run the following command:  
  
```bash  
uvicorn main:app --reload  
```

## Running the Project with Docker Compose  
  
1. Ensure that Docker and Docker Compose are installed on your system.  
  
2. Build and run the project using Docker Compose by running the following command in the project directory:  
  
```bash  
docker-compose up --build  
```

3. To stop the containers and remove the resources created by Docker Compose, run the following command:

```bash
docker-compose down  
```

## API docs
Visit http://127.0.0.1:8000/docs to view the API documentation.

## Testing the APIs  
  
You can test the APIs using tools like `curl`, Postman, or directly in your web browser.  
  
### Testing the Hello World API  
  
The Hello World API is a simple GET request that returns a "Hello, World!" message. It requires basic authentication. The default username is "user" and the password is "pass".  
  
#### Using curl  
  
To test the Hello World API using `curl`, run the following command in your terminal:  
  
```bash  
curl -u user:pass http://127.0.0.1:8000/hello  
