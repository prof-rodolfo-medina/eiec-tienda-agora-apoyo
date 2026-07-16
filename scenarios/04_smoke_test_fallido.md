# Escenario 4 · Smoke test fallido

Cambiar la ruta `/health` por `/healthz` sin actualizar el health check.

Resultado esperado:

- la imagen se construye;
- el contenedor arranca;
- el smoke test falla;
- el despliegue debe detenerse.
