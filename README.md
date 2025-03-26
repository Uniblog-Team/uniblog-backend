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