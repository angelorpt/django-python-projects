# fsc-python

Educational Django 5.2 project — Python fundamentals tutorial.

## Structure

- `modulo-01/fundamento.py` — standalone Python tutorial script (no `main()` guard)
- `modulo-01/mini-project/` — Django 5.2 project (`hello_django` app)
- `module-02/` — empty placeholder (not a typo; naming is intentionally mixed pt/en)

## Django commands

Venv is at `modulo-01/mini-project/venv/` — activate before running anything:

```bash
source modulo-01/mini-project/venv/bin/activate
python manage.py runserver   # dev server
```

All Django commands must run from `modulo-01/mini-project/`.

## Type checking

Pyright is configured via `pyrightconfig.json` in the mini-project dir, but no local install. Use either:
- Global `pyright`, or
- `pip install pyright` in the venv

Run from the mini-project root:
```bash
pyright
```

The source has a known typo: `# pyrefly: ignore [missing-import]` in `urls.py` — replace `pyrefly` with `pyright` if type-checking that file.

## Tests / Lint

None configured. No test framework, no linter, no formatter. Focus is educational content.

## Git

No remote configured. All branches (`main`, `develop`, `feature/module-02`) point at the same single commit.
