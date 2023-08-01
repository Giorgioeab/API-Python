from fastapi import FastAPI

app = FastAPI()

@app.get('/{name}')
def boas_vindas(name:str):
    return {"mensagem": f"{name}"}

@app.get('/items/{item_id}')
def id_product(item_id: int):
    return {'ID item':f'{item_id}'}