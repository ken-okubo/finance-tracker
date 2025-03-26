# 💰 Finance Tracker API

Uma API simples para controle de despesas pessoais ou de pequenos negócios.

A simple API to track expenses for personal or small business use.

---

## 📦 Stack

- Python 3.10
- Django + Django REST Framework
- PostgreSQL
- Docker + Docker Compose

---

## Como rodar localmente | How to run locally

### ✅ Pré-requisitos | Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

### 🔄 Passo a passo (em português)

```bash
# 1. Apagar qualquer instância anterior (containers, banco, rede)
docker compose down -v

# 2. Dar permissão ao script de inicialização
chmod +x entrypoint.sh

# 3. Construir a imagem e subir os containers
docker compose build
docker compose up
```

Abra outro terminal para:

```bash
# 4. Aplicar as migrações
docker compose exec web python manage.py migrate

# 5. Popular com dados mock (opcional)
docker compose exec -T web python manage.py shell < finance/mock_data.py
```

Acesse em: [http://localhost:8000/api/expenses/](http://localhost:8000/api/expenses/)

---

### 🔄 Step-by-step (English)

```bash
# 1. Stop and remove any previous containers, volumes or networks
docker compose down -v

# 2. Make sure the entrypoint script is executable
chmod +x entrypoint.sh

# 3. Build and start the containers
docker compose build
docker compose up
```

In another terminal:

```bash
# 4. Run migrations
docker compose exec web python manage.py migrate

# 5. Load mock data (optional)
docker compose exec -T web python manage.py shell < finance/mock_data.py
```

Open: [http://localhost:8000/api/expenses/](http://localhost:8000/api/expenses/)

---

## 🔍 Endpoints

- `GET /api/expenses/` — list all expenses
- `POST /api/expenses/` — create a new expense
- `GET /api/categories/` — list all categories
- `GET /api/expenses/summary/?month=2025-03` — monthly summary

---

## 📚 API Documentation / Documentação da API

The interactive API documentation is available at the following routes:

A documentação interativa da API está disponível nos seguintes endereços:

- [Swagger UI](http://localhost:8000/swagger/)
- [ReDoc](http://localhost:8000/redoc/)

These docs are auto-generated from the codebase using `drf-yasg`.

Essas documentações são geradas automaticamente a partir do código usando `drf-yasg`.

---

## 📁 Estrutura do projeto | Project structure

```
finance-tracker/
├── finance/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── mock_data.py
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
└── requirements.txt
```

---

## ✍️ Autor | Author

**Ken Okubo**  
Backend Developer
[LinkedIn](https://www.linkedin.com/in/ken-okubo-8b484978/) | [GitHub](https://github.com/ken-okubo)