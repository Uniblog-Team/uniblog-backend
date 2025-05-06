# Dockerfile
# Usa una imagen base de Python oficial
FROM python:3.13-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias primero para aprovechar el caché de Docker
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto en el que correrá FastAPI (Uvicorn)
EXPOSE 8000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
# Adapta 'app.main:app' a la ubicación de tu instancia de FastAPI
# '--host 0.0.0.0' es necesario para que sea accesible desde fuera del contenedor
# '--reload' es útil para desarrollo, considera quitarlo para producción
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]