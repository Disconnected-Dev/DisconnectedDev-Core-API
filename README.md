# DisconnectedDev-Core-API

A fastAPI api to serve as the basis of the backend for the Disconnected Dev site.

### running the API locally

Once you have cloned the repo, create a virtual environment:

Linux Terminal

```bash
# make sure you are in your project directory
cd <path to project>/DisconnectedDev-Core-API

# create a virtual environment to run the project in
python3 -m venv fast_env

# now activate the venv environment
source fast_env/bin/activate
```

---

Windows

```powershell
# On Windows envoke with
c:\> c:\Python35\python -m venv c:\path\to\fast_env

# if python is in your PATH make an env in the current DIR like this
c:\> python -m venv fast_env

# now activate the venv environment
source 'fast_env\Scripts\activate'
```

---

Install the requirments for the project:

```bash
pip install -r requirements.txt
```

Navigate to the 'dd-core-api' directory within the project directory:

```bash
cd [local_filesystem]/DisconnectedDev-Core-API/dd-core-api/
```

Start the API (--reload option tells uivcorn to hot reload):

```bash
uvicorn core_api:dd_api --reload
```

---

### API Documentation

API documentation is built in and can be reached from a running api at the following endpoints:

> OpenAPI interactive Documentation (previously Swagger UI)

```http
http://127.0.0.1:8000/docs
```

> Alternative ReDoc Documentation

```http
http://127.0.0.1:8000/redoc
```

---

### API Endpoint Reference

> Blog endpoints:

```python
# return a list of all published blog entries
"/blogs/"

# create a new blog entry
"/blogs/new_post/"

# update a draft blog entry
"/blogs/update_post/{blog_id}"

# publish a draft blog entry to make public
"/blogs/publish/{blog_id}"

# return a list of all published blog entries from a specific user
"/blogs/users_blogs/{user_id}"

# return a specific blog entry
"/blogs/post/{blog_id}"

# remove a specific blog entry from the database
"/blogs/remove/{blog_id}"
```

> User endpoints:

```python
# add a user to the database
"/users/add/"

# update an existing user in the database
"/users/update/{user_id}"

# remove a user from the database
"/users/remove/{user_id}"
```
