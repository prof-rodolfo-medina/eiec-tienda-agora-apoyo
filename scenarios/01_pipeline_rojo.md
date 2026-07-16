# Escenario 1 · Pipeline rojo

Cambiar temporalmente `/health`:

```python
return {"status": "fail"}
```

Resultado esperado:

- falla `test_health_endpoint_returns_ok`;
- el pipeline se detiene;
- no debe fusionarse el Pull Request.

Pregunta al grupo:

> ¿Qué evidencia del log permite localizar el problema?
