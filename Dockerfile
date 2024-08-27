# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente al contenedor
COPY . .

# Expone el puerto en el que tu app Flask corre
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
