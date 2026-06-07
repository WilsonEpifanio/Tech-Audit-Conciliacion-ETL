import pandas as pd

# 1. Datos del Sistema Operativo (Subdiario de Ventas)
subdiario_data = {
    'Fecha': ['2026-06-01', '2026-06-02', '2026-06-02', '2026-06-03', '2026-06-04'],
    'Factura': ['A-0001', 'A-0002', 'A-0003', 'A-0004', 'A-0005'], # A-0005 no estará en contabilidad
    'CUIT': ['30-11111111-1', '30-22222222-2', '30-33333333-3', '30-44444444-4', '30-55555555-5'],
    'Monto_Operativo': [150000, 200500, 85000, 320000, 100000] # A-0002 tiene 500 pesos extra
}

# 2. Datos de la Contabilidad (Mayor de Ventas)
contabilidad_data = {
    'Fecha_Contable': ['2026-06-01', '2026-06-02', '2026-06-02', '2026-06-03', '2026-06-05'],
    'Comprobante': ['A-0001', 'A-0002', 'A-0003', 'A-0004', 'A-0006'], # A-0006 es un registro fantasma
    'CUIT_Cliente': ['30111111111', '30222222222', '30333333333', '30-44444444-4', '30666666666'], # Trampa: algunos no tienen guiones
    'Monto_Contable': [150000, 200000, 85000, 320000, 50000] 
}

# Creamos los DataFrames
df_subdiario = pd.DataFrame(subdiario_data)
df_contabilidad = pd.DataFrame(contabilidad_data)

# Exportamos a archivos CSV (que simularemos descargar de los sistemas)
df_subdiario.to_csv('Subdiario_Ventas.csv', index=False)
df_contabilidad.to_csv('Mayor_Contable.csv', index=False)

print("¡Archivos generados con éxito! Listos para auditar.")