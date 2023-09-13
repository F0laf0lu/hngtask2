<<<<<<< HEAD
=======
# API Documentation for Person Resource


## Base URL
The base URL for this API is http://example.com/api/


## Authentication
This API does not require authentication for the endpoints mentioned below.

## Endpoints

### Create a New Person
Endpoint `POST /api/`

Create a new person and add their details to the database.

JSON object containing the following fields:

name (string) - The name of the person.

track (string) - The track of the person.

Sample Request

```json
{
    "name": "John",
    "track": "backend",
}
```
Response (HTTP 201 Created)
```json
{   
    "id": 1,
    "name": "John",
    "track": "backend",
}
```

## Retrieve Person Details

Endpoint GET /api/<user_id>/

Retrieve details of a person with the specified `id`

Parameters
    `user_id` (integer): The unique ID of the person you want to retrieve.

Sample Request 
    ` GET /api/1/ `

Response (HTTP 200 OK):
```json
{   
    "id": 1,
    "name": "John",
    "track": "backend",
}
```

## Update Person Details

Endpoint `PUT /api/<user_id>/`

Update details of an existing person with the specified id

Parameters
    `user_id` (integer): The unique ID of the person you want to retrieve.

Sample Request 
    ` GET /api/1/ `

Request Body
    JSON object containing the following fields (you can update one or more fields):
    name (string) - The name of the person.

    track (string) - The track of the person.

Sample Request

```json
{
    "name": "John",
    "track": "Frontend",
}
```

Response (HTTP 200 OK):
```json
{   
    "id": 1,
    "name": "John",
    "track": "Frontend",
}
```

## Delete a Person

Endpoint: `DELETE /api/<user_id>/`

Remove a person with the specified ID from the database.

Parameters:
    `user_id` (integer) - The unique ID of the person you want to delete.

Sample Request
    `DELETE /api/1/`

Response (HTTP 204 No Content)

(No response content, the person has been deleted)


## Conclusion
This API allows you to perform CRUD operations on a "person" resource. Make sure to replace http://example.com/api/ with your actual API URL when making requests.
>>>>>>> 0b4a40ebd229bcc0fed076fb6f65395662dec837
