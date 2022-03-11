from fastapi import FastAPI
import controller

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/promo")
def get_promos():
    return controller.get_promos()


@app.get("/promo/{id}")
def get_promo(promo_id):
    results = controller.get_promo(promo_id)
    return results


@app.post("/promo")
def post_promo(name, description = None):
    results = controller.post_promo(name, description)
    return results
