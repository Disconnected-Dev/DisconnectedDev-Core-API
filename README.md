# DisconnectedDev-Core-API

A fastAPI api to serve as the basis of the backend for the Disconnected Dev site.

API documentation is built in and can be reached from a running api at the following endpoints:

> OpenAPI interactive Documentation (previously Swagger UI)

```http
http://127.0.0.1:8000/docs
```

> Alternative ReDoc Documentation

```http
http://127.0.0.1:8000/redoc
```

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
"/blogs/pub_post/{blog_id}"

# return a list of all published blog entries from a specific user
"/blogs/users_posts/{user_id}"

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
