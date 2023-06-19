
# Toy Store

This flask application demonstrates a simple application of an online toy store. 
## Run Locally

Clone the project

```bash
  git clone https://github.com/chrstsrs/Toy.git
```

Go to the project directory

```bash
  cd Toy
```

Build Docker images

```bash
  docker-compose build
```

Start the server

```bash
  docker-compose up
```

Stop the server

```bash
  ^C
```

Remove the containers

```bash
  docker-compose down -v
```

## Swagger Reference
There is a swagger reference in the 
http://127.0.0.1:5000//swagger-ui
## API Reference

#### Get all toys

```http
  GET /catalog
```
Returns all the available toys.


#### Post a new toy

```http
  POST /catalog
```
Creates a new toy.

The arguments in the body of the request are:
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string(60)` | **Required**. The toy's name |
| `description` | `string(255)` | The description of the toy |
| `price` | `float` | **Required**. The price of the toy |
| `quantity` | `integer` | **Required**. The quantity of the toy |


#### Update a toy

```http
  PUT /catalog/{id}
```
Updates an existing toy.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `ineger` | **Required**. The toy's id |

The arguments can be passed in the body of the request are:

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string(60)` | The toy's name |
| `description` | `string(255)` | The description of the toy |
| `price` | `float` | The price of the toy |
| `quantity` | `integer` | The quantity of the toy |

#### Get Toy

```http
  GET /catalog/{name}
```
Returns information for a particular toy.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. The toy's name |

#### Delete a toy

```http
  DELETE /catalog/{id}
```
Deletes a toy.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `ineger` | **Required**. The toy's id |



## Assumption

The name is set as unique and not null. As I understand, the user will request a particular toy, with a user-friendly name. The users can not deal with numbers easily, as product codes. To avoid confusion I set the name as unique and not null. 


## Author

- Charisios Tsiairis[@chrstsrs](https://www.github.com/chrstsrs)

