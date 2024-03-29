# API Documentation 


## Base URL
The base URL for this API is https://folafolu.pythonanywhere.com/


## Authentication
This API does not require authentication for the endpoints mentioned below.

## Endpoints

### Create a New Person
Endpoint : `POST /api/`

Creates a new person and add their details to the database.

Request body : JSON object containing the following fields:

- name (string) - The name of the person.

- track (string) - The track of the person.

##### Sample Request:

```json
{
    "name": "John",
    "track": "backend",
}
```
##### Response (HTTP 201 Created)
```json
{   
    "id": 1,
    "name": "John",
    "track": "backend",
}
```

## Retrieve Person Details

Endpoint : `GET /api/<user_id>/`

Retrieves details of a person with the specified `user_id`

Parameters :

- `user_id` (integer): The unique ID of the person you want to retrieve.

#### Sample Request :

`GET /api/1/`

#### Response (HTTP 200 OK) :
```json
{   
    "id": 1,
    "name": "John",
    "track": "backend",
}
```

## Update Person Details

Endpoint : `PUT /api/<user_id>/`

Update details of an existing person with the specified `user_id`

Parameters :

- `user_id` (integer): The unique ID of the person you want to retrieve.

Request Body : JSON object containing the following fields (you can update one or more fields):

- name (string) - The name of the person.

- track (string) - The track of the person.

#### Sample Request `PUT /api/1/` :

Request body :

```json
{
    "name": "John",
    "track": "Frontend",
}
```

#### Response (HTTP 200 OK) :
```json
{   
    "id": 1,
    "name": "John",
    "track": "Frontend",
}
```

## Delete a Person

Endpoint : `DELETE /api/<user_id>/`

Remove a person with the specified `user_id` from the database.

Parameters :

- `user_id` (integer) - The unique ID of the person you want to delete.

#### Sample Request:

`DELETE /api/1/`

#### Response (HTTP 204 No Content)

(No response content; the person has been deleted)

## Limitations

- It is not possible to create or update multiple persons at the same time using the api

## Conclusion
This API allows you to perform CRUD operations on a "person" resource.
