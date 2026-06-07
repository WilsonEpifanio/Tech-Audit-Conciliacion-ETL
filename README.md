# Tech Audit: Motor de Conciliación Automatizada (ETL)

Este proyecto consiste en un modelo de automatización de datos diseñado para optimizar los procedimientos de auditoría externa y fortalecer el control de gestión corporativo.

## Contexto y Desafío
El cruce manual de registros operativos (ej. Subdiario de Ventas) contra el Mayor Contable requiere una inversión significativa de horas de trabajo y presenta un alto riesgo de error humano. Asimismo, este procedimiento se ve fuertemente limitado por la capacidad de procesamiento de las hojas de cálculo tradicionales (Microsoft Excel) al enfrentarse a bases de datos de clientes con gran volumen transaccional.

## Arquitectura de la Solución
Se desarrolló un pipeline ETL (Extract, Transform, Load) estructurado en Python. El modelo ejecuta la ingesta, limpieza, normalización de formatos (como identificadores fiscales) y homologación de bases financieras. Mediante la aplicación de un cruce relacional avanzado (Outer Join), el sistema aísla e identifica desvíos transaccionales con total precisión.

## Impacto y Resultados Clave
* **Eficiencia Operativa:** Automatización integral del proceso de conciliación. El modelo es capaz de procesar bases de datos masivas (superando el límite técnico de 1 millón de filas de Excel) en segundos.
* **Auditoría y Gestión de Riesgos:** Clasificación automática de las partidas conciliatorias y excepciones en tres niveles de alerta crítica:
  1. Diferencias materiales de monto por errores de registro.
  2. Omisión de registro contable (Riesgo fiscal).
  3. Asientos contables registrados sin el debido respaldo operativo (Indicador de control interno / Riesgo de fraude).
* **Trazabilidad:** Generación automática de papeles de trabajo estructurados. El script exporta un archivo .xlsx segmentado en pestañas, listo para la revisión técnica del equipo de auditoría y la formulación de ajustes.

## Stack Tecnológico
* **Python 3:** Lenguaje base para el desarrollo del script.
* **Pandas:** Librería principal para el procesamiento de datos masivos y operaciones relacionales.
* **Jupyter Notebook:** Entorno de desarrollo utilizado para la trazabilidad del código y visualización de DataFrames.
* **OpenPyXL:** Motor empleado para la exportación de reportes financieros estructurados.
