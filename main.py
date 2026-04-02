from fastapi import FastAPI
from models import Product

app = FastAPI()


@app.get("/")
def greet():
  return "Hello this my first work in fast api"

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=34, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),

]
@app.get("/products")
def get_all_products():
  return products

@app.get("/products/{id}")
def get_products_id(id:int):
  for product in products:
    if product.id == id:
      return product
    
  return "product not found"

@app.post("/product")
def add_product(product:Product):
  products.append(product)
  return product

@app.put('/product')
def update_product(id:int,product:Product):
  for i in range(len(products)):
    if products[i].id == id:
      products[i] = product

      return "sucessfully added"
  return "not found"

@app.delete('/product')
def update_product(id:int,product:Product):
  for i in range(len(products)):
    if products[i].id == id:
      del products[i]
      return "sucessfully deleted"
  return "not found"

