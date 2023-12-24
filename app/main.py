from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# title str, content str
my_posts = [{"title":"title of post 1", "content":"content of post 1", "id": 1},{"title": "post2",
                                                                                 "content": "I like pizza",
                                                                                 "id": 2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
async def root():
    return {"message":"Welcome to my API 2!!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(payLoad: dict = Body(...)):
def create_posts(post: Post):
    print(post)
    print(post.dict())
    post_dict = post.dict()
    post_dict['id'] =randrange(0, 1000000)
    # return {"post": f"title {payLoad['title']} content: {payLoad['content']}"} 
    my_posts.append(post_dict)
    return {"data" : post_dict} 


@app.get("/posts/{id}")   # {id} is a path parameter
def get_post(id: int, response: Response):  # will convert to a int 
    
    post = find_post(id)
    if not post: 
        # response.status_code = 404
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")

    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting post
    # find the index in the array that has required ID
    # my_post.pop(id)
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id {id} does not exist')
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id {id} does not exist')
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {'data': post_dict}
