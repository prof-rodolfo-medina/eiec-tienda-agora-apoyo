# Escenario 3 · Artefacto no trazable

Construir la imagen únicamente con la etiqueta:

```bash
docker build -t tienda-agora-api:latest .
```

Problema:

- no existe vínculo evidente con un commit;
- el rollback y la auditoría se complican.

Alternativa:

```bash
docker build -t tienda-agora-api:2.0.0 .
docker build -t tienda-agora-api:<COMMIT_SHA> .
```
