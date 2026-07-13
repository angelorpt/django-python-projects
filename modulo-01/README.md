# Módulo 01 — Fundamentos de Python

Este módulo contém dois materiais complementares: um **script tutorial** de Python puro e um **projeto Django** introdutório.

---

## `fundamento.py` — Tutorial Python

Script executável (441 linhas) que percorre os fundamentos da linguagem Python. Cada seção é auto-contida com exemplos práticos.

**Conteúdo abordado:**

| Seção | Tópicos |
|---|---|
| Tipos primitivos | `int`, `float`, `str`, `bool`, `None` |
| Coleções | `list`, `tuple`, `dict`, `set` |
| Operadores | aritméticos, comparação, lógicos |
| Controle | `if`/`elif`/`else`, `match`/`case` (3.10+) |
| Loops | `for` (com `range`, `enumerate`), `while`, `break`, `continue` |
| Funções | `def`, `return`, `*args`, `**kwargs`, `lambda`, docstrings |
| Funções de ordem superior | `filter`, `map`, `reduce` |
| Closures | função que retorna função |

**Para executar:**

```bash
python fundamento.py
```

> **Nota:** O script não tem guard `if __name__ == '__main__'` — todo o código executa no escopo global.

---

## `mini-project/` — Projeto Django 5.2

Projeto gerado com `django-admin startproject hello_django`, configurado como introdução ao framework.

### Estrutura

```
mini-project/
├── manage.py              # CLI do Django (entrypoint)
├── db.sqlite3             # Banco de dados SQLite
├── pyrightconfig.json     # Configuração do type checker Pyright
├── requirements.txt       # Dependências (Django 5.2.7 + stubs)
├── venv/                  # Ambiente virtual (Python 3.12.3)
└── hello_django/          # Pacote do projeto Django
    ├── __init__.py
    ├── settings.py        # Configurações (DEBUG=True, SQLite)
    ├── urls.py            # Rotas: /admin/, /hello/
    ├── views.py           # View hello() -> JSON
    ├── asgi.py            # Entrypoint ASGI
    └── wsgi.py            # Entrypoint WSGI
```

### Rotas

| Rota | Função |
|---|---|
| `/admin/` | Site admin padrão do Django |
| `/hello/` | Retorna `{"message": "Hello from Django"}` |

### Para rodar

```bash
source venv/bin/activate     # ativar ambiente virtual
python manage.py runserver   # servidor de desenvolvimento
```

Todos os comandos do Django (`runserver`, `migrate`, etc.) devem ser executados de dentro de `mini-project/`.

### Type checking

O projeto inclui configuração Pyright com plugin `django-stubs`:

```bash
# com Pyright instalado globalmente ou no venv:
pyright
```

> **Atenção:** O arquivo `hello_django/urls.py` contém o comentário `# pyrefly: ignore [missing-import]` — troque `pyrefly` por `pyright` se for fazer type checking naquele arquivo.

---

## `requirements.txt` (raiz)

Dependências compartilhadas entre o script tutorial e o projeto Django:

| Pacote | Versão |
|---|---|
| `asgiref` | 3.10.0 |
| `Django` | 5.2.7 |
| `sqlparse` | 0.5.3 |
