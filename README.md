# USER = user-api

### Description

### Test Cases

```USER API

```

| Method    | Endpoint      | Description                  |
| :-------- | :------------ | :--------------------------- |  
| `POST`    | `{user/{id}}` | **Get a User by Id**.        |
| :-------- | :-----------  | :-----------------------     |
| `PUT`     | `{user/{id}}` | **Edit a User**.             |
| :-------- | :-------      | :-----------------------     |
| `DELETE`  | `{user/{id}}` | **Delete a User**.           |
| :-------- | :-----------  | :-----------------------     |
| `POST`    | `/users`      | **Create a User**.           |
| :-------- | :-----------  | :-----------------------     |
| `GET`     | `/users`      | **Query users with params**. |     |

# Installation and Setup Locally

**To be able to get this project to your local machine**

```sh
    git clone git@github.com:BethMwangi/user-api.git
    pip install virtualenv venv
   . venv/bin/activate
    cd user-api/
```

## To execute the demo run the commands

```sh
$ cd user-app/
$ docker-compose build
```

```sh
$ docker-compose up
$ Go to http://localhost/swagger-ui to test the api endpoints
```

## ApiLink Testing

[Link to the API Project -Heroku](https://userapilist.herokuapp.com/swagger-ui)

![User API](https://jmp.sh/XAFg7sLx)
