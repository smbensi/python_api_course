
## main.py

To run it:
> uvicorn main:app

made of 2 portions:
- a function root() (async is optional) that return a special data
- a decorator when we can reference our fastAPI instance, HTTP request and the root path/root Url ("/")

To automatically reload when changing the code
> uvicorn main:app --reload


- FastAPI returns the first match with the path if you have multiple functions wih the same path **(order matters)**

## test your API

### Postman

nice tool to test your API

## HTTP requests

### GET

want data from the API server

### POST

we can send data to the API server, when we want to create something
extract the data with Body from fastapi.params

## Schema validation

we want to define how the data should look like explicitely
Use `pydantic` to define Schema

CRUD API: 4 main options of an application. Create (POST), Read (GET), Update (PUT/PATCH), Delete (DELETE)


- The {id} is always a str

- there is a lot of HTTP status code:
    - 400 bad request
    - 404 not found
    - 500 internal server error
    - 201  when we create something


- auto documentation go to the adress and add /docs for example http://127.0.0.1:8000/docs
or adding `redoc` at the end

# Database

- collection of organized data that can be easily accessed and managed
- we don't work or interact wiht DBs directly
- Instead we make use of a software referred to as a Database Management System (DBMS)
- 2 major branches of DBMS (Relational (MYSQL,ORACLE,POSTGRESQL) or NoSQL(MongoDB, DynamoDB, ORACLE))
- SQL - Language used to communicate with DBMS

## Postgres

- Each instance of postgres can be carved into multiple separate dbs.
- By default every Postgres installation comes with one db already created called "postgres"
- serial is a regular integrer bbut automatically create a number (incrementing)

## Tables 

- a table represents a subject or event in an app (Users, Products, Purchases and they are relational)
- a column represents a different attribute
- each row represents a different entry in the table
- databases have datatypes just like any programing language

### Primary key

- it's a column or group of columns that uniquely identifies each row in a table , Table can have only
one primary key
- a UNIQUE constraint can be applied to any column to make sure every record hass a unique value for that column
- Null Constraints: When adding a new entry, any column can be left black. When a column is left blank, it has a nulll value


### SQL

```SQL

products is the table name
* means everthingg

SELECT * from products;
SELECT name,price,id from products (particular columns)
```