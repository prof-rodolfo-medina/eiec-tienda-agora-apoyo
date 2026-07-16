# Arquitectura didáctica

```text
Estudiante
   |
   v
FastAPI
   |
   +--> Catálogo en memoria
   |
   +--> Pruebas unitarias
   |
   +--> Pruebas de API
   |
   +--> Pipeline CI
   |
   +--> Imagen Docker
   |
   +--> Smoke test
```

Este diseño es intencionalmente pequeño para que la complejidad técnica no
opaque los conceptos de CI/CD.
