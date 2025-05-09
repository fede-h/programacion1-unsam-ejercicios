# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if  pago_extra_mes_comienzo - 1 < mes < pago_extra_mes_fin + 1:    
        saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    
    if saldo < 0:
        total_pagado += saldo
        saldo = 0

    mes += 1
    print(f'{mes} : ${round(total_pagado, 2)}    {round(saldo, 2)}')

print(f'Total pagado: {round(total_pagado, 2)}\nMeses: {mes}')

# 309 : $877389.99    1316.61
# 310 : $878712.08    0
# Total pagado: 878712.08
# Meses: 310