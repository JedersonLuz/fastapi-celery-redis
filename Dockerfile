# Use a imagem base do Python 3.10
FROM python:3.10-slim

# Expõe a porta 8000
EXPOSE 8000

# Define o diretório de trabalho
WORKDIR /code

# Copia o pyproject.toml e o poetry.lock para o diretório de trabalho
COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock

# Instala as dependências do projeto
RUN pip install --no-cache-dir --upgrade poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

# Copia o restante dos arquivos para o diretório de trabalho
COPY . /code

# Define o comando de inicialização do container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]