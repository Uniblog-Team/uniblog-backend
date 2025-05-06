# uniblog-backend
Backend de la plataforma Uniblog, pasos se instalación:

1. Crear y activar el entorno virtual de Python  

   - **En Linux/macOS:**  

      ```bash
      python3 -m venv scp-env  
      source scp-env/bin/activate  
      ```  

   - **En Windows:**  

      ```powershell
      python -m venv scp-env  
      scp-env\Scripts\activate  
      ```  

2. Instalar los requerimientos del proyecto  

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecute la aplicación

   ```bash
   uvicorn app.main:app --reload
   ```

---

## Entorno de desarrollo

Para desarrollar correctamente, es necesario contar con una base de datos disponible para pruebas. Este repositorio ya incluye una instancia de PostgreSQL contenida junto con la aplicación mediante Docker. El flujo de desarrollo recomendado es el siguiente:

1. **Clonar el repositorio**.

2. **Crear un archivo `.env` local** (si se desea utilizar esta opción), con el siguiente contenido:

   ```
   DATABASE_URL=postgresql://uniblog_user:uniblog_password@db:5432/uniblog_db
   POSTGRES_DB=uniblog_db
   POSTGRES_USER=uniblog_user
   POSTGRES_PASSWORD=uniblog_password
   # SOLO PARA PRUEBAS
   ```

3. **Levantar el entorno de desarrollo**:

   ```bash
   docker-compose up -d
   ```

4. **Si se realizan cambios en los modelos (como creación o modificación de tablas)**:

   * Editar el archivo `app/models.py`.

   * Generar una nueva migración:

     ```bash
     docker-compose exec backend alembic revision --autogenerate -m "Descripción del cambio"
     ```

   * Aplicar la migración localmente:

     ```bash
     docker-compose exec backend alembic upgrade head
     ```

   * Hacer *commit* tanto de los cambios en los modelos como del nuevo script de migración ubicado en `alembic/versions/`.

5. **Desarrollar la lógica de la aplicación**.

6. **Para detener el entorno**:

   ```bash
   docker-compose down
   ```

   Si se desea eliminar también los volúmenes de la base de datos (reiniciar desde cero):

   ```bash
   docker-compose down -v
   ```

---

> ⚠️ **Nota sobre errores en migraciones:**
> Si al ejecutar una migración aparece un error relacionado con tipos de datos no reconocidos, agregue manualmente el siguiente import al script de migración generado:
>
> ```python
> import sqlmodel
> ```
>
> Esto asegura que los tipos definidos por **SQLModel** estén disponibles durante la ejecución.
> Puede que necesite aplicar el comando con `sudo`, dependiendo de su configuración.

---
