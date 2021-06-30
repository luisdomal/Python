print("Ingresa el nombre de la tarjeta: ")
nombre = input()
print("Ingresa la tasa de interes anual: ")
tasa = input()
tasa1 = float(tasa)
print("Ingresa el monto de la deuda: ")
deuda = input()
deuda1 = float(deuda)
print("Ingresa pago a realizar: ")
pago = input()
pago1 = float(pago)
print("Ingresa nuevos cargos: ")
nuevos_cargos = input()
nuevos_cargos1 = float(nuevos_cargos)

interes_mensual = (tasa1 / 12)
deuda_recalculada = (deuda1 - pago1) * (1 + interes_mensual)
nueva_deuda = deuda_recalculada + nuevos_cargos1

print("La nueva deuda es: {}".format(nueva_deuda))


