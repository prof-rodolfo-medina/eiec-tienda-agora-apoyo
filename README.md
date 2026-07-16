# Tienda Ágora API · Repositorio de apoyo

Laboratorio didáctico para **Entornos de Integración y Entrega Continua**.

## Propósito

El repositorio permite demostrar:

- pruebas unitarias y de API;
- cobertura y lint;
- GitHub Actions y GitLab CI;
- construcción de una imagen Docker;
- health checks y smoke tests;
- trazabilidad entre commit, artefacto y despliegue;
- escenarios de pipeline verde y rojo.

## Ejecución local

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
python -m pytest
flake8 app tests
uvicorn app.main:app --reload
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

## Docker

```bash
docker compose up --build
```

Abrir:

- API: `http://localhost:8000`
- Swagger: `http://localhost:8000/docs`
- Health: `http://localhost:8000/health`

## Escenarios

La carpeta `scenarios/` contiene instrucciones para provocar fallos
controlados durante la simulación.

## Estrategia didáctica

1. Mostrar `main` en verde.
2. Aplicar un escenario rojo.
3. Leer el log con el grupo.
4. Corregir el fallo.
5. Construir el artefacto.
6. Ejecutar el smoke test.
7. Relacionar el artefacto con el commit.
