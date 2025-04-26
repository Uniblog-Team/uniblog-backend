from fastapi import FastAPI


app = FastAPI(
    title="UniBlog Backend",
    description="API Backend para UniBlog",
    version="0.1.0"
)

# Configuración básica de CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[ # Dominios ficticios
#         "https://tudominio.com",
#         "https://www.tudominio.com",
#         "http://localhost:3000"  # Para desarrollo local
#     ],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["Authorization", "Content-Type"]
# )


@app.get("/")
def read_root():
    return {"message": "API de UniBlog está funcionando"}
