from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


from routers.auditorium.router import router as auditorium_router
from routers.equipment.router import router as equipment_router
from routers.auth.router import router as auth_router


app = FastAPI()

app.include_router(auditorium_router, prefix='/api')
app.include_router(equipment_router, prefix='/api')
app.include_router(auth_router, prefix='/api')

origins = []

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_methods=['POST', 'GET', 'PUT', 'DELETE'],
                   allow_headers=['*'])
