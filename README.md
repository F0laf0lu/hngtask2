# API Documentation for Person Resource


## Base URL
The base URL for this API is http://example.com/api/


## Authentication
This API does not require authentication for the endpoints mentioned below.

## Endpoints

### Create a New Person
Endpoint POST /api/

Description: Create a new person and add their details to the database.

Request Body: JSON object containing the following fields:

name (string): The name of the person.

track (string): The track of the person.

Sample Request:

```{
    "name": "John",
    "track": "backend",
}```


