# Usar uma imagem base do Python
FROM python:3.9-slim

# Configurar diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos necessários para dentro do contêiner
COPY requirements.txt /app/
COPY app.py /app/
COPY model /app/model/
COPY train_model.py /app/
COPY use_model.py /app/

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta usada pela API (ajuste se necessário)
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
