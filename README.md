# fsc-python

Curso de Python — fundamentos, Django e tópicos avançados, organizado em módulos progressivos.

---

## Módulos

| Módulo | Status | Descrição | Repositório |
|---|---|---|---|
| `modulo-01` | ✅ Completo | Fundamentos da linguagem Python + introdução ao Django | [fsc-python-01-basic](https://github.com/angelorpt/fsc-python-01-basic) |
| `module-02` | 📦 Placeholder | A definir | — |

---

## Clonar o projeto

O repositório usa **submodules** do Git para gerenciar cada módulo.

### Clonar com submódulos (recomendado)

```bash
git clone --recurse-submodules git@github.com:angelorpt/django-python-projects.git
```

### Se já clonou sem os submódulos

```bash
git submodule update --init --recursive
```

### Atualizar submódulos (puxar changes mais recentes)

```bash
git submodule update --remote --merge
```

---

## Como usar

Cada módulo é independente e contém seu próprio `README.md` com instruções específicas. Navegue até o módulo desejado e siga as orientações locais.

### Django (modulo-01)

```bash
source modulo-01/mini-project/venv/bin/activate
python manage.py runserver   # servidor de desenvolvimento
```

> Todos os comandos do Django devem ser executados de dentro de `modulo-01/mini-project/`.

---

## Convenções

- `modulo-01` = nomenclatura em pt-BR (primeiro módulo)
- `module-02` = nomenclatura em inglês (segundo módulo, a definir)
