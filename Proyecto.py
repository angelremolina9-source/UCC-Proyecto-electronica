#Proyecto de ingenieria por la materia de herramientas computacionales

#Estudiantes:
#Angel Remolina
#Daniel Rovira
#Jose Mason
#Oscar Lacera

#Pondremos el dataset (Conjunto de datos) para ver como esta compuesto
import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv("dataset_eficiencia_electronica_1000.csv")

print(datos)
print(datos.describe())
print(datos.info())
print(datos["temperatura_c"])
print("Potencia:")
print(datos["potencia_kw"])

#Esto son pruebas para confirmar los datos y ver si hay datos nulos, ver sus tipos de paquetado y como haremos la distribucion de las graficas
groups = datos.groupby("equipo_id")
consumo = groups["potencia_kw"]
sumatoria = consumo.sum()
sumatoria.plot(kind="bar")

plt.title("Figura 1. Equipos que presentan consumo energetico total registrado")
plt.ylabel("Potencia (Kw)")
plt.grid(True, linestyle="--")
plt.show()

#Figura 1. Se muestran valores como todos los equipos consumen una potencia energetica, pero lo que se busca es solamente agregar o filtrar unicamente
#Las maquinas mayores a 2.5 Kw.
Maquinas_Calientes = datos[datos["potencia_kw"] > 2.5]
Grupos_Calientes = Maquinas_Calientes.groupby("equipo_id")["potencia_kw"].sum()

Grupos_Calientes.plot(kind="bar")
plt.title("Figura 2. Maquinas con potencia energetica alta (aletar media > 2.5 Kw)")
plt.ylabel("Potencia Kw")
plt.grid(True, linestyle="--")
plt.show()

#Figura 2. Se muestran los valores sumados de cada potencia mostrandono su consumo energetico en Kw y viendo lo que consumen en su totalidad.
#Esta grafica nos hace ver cuantos dispositivos estan consumiendo tanta potencia para hacer algo al respecto
print("\nAqui se muestran las fallas")
print(datos["fallas_detectadas"])
plt.scatter(datos["fallas_detectadas"],datos["temperatura_c"])
plt.title("Figura 3. Relacion de la temperatura y fallas")
plt.ylabel("Temperatura Operacional (C~)")
plt.xlabel("Cantidad de fallas registradas")
plt.grid(True, linestyle="--")
plt.show()
#Figura 3. En esta relacion al comparar las temperaturas con fallas detectadas, vemos que para 0 fallas hay equipos de 15 a 70 grados celsius y para las otras
#fallas hay equipos que fallan asi sea por temperaturas bajas, por lo que no fallan por temperaturas.
#Para ingenieria este tema se llama Ausencia de Correlacion
resumen_grupales = datos.groupby("equipo_id")[["potencia_kw","fallas_detectadas"]].sum()
plt.scatter(resumen_grupales["fallas_detectadas"],resumen_grupales["potencia_kw"])
plt.title("Figura 4. Relacion entre potencia y numero de fallas producidas por esta")
plt.ylabel("Potencia Kw")
plt.xlabel("Numero de fallas presentadas")
plt.grid(True, linestyle="--")
plt.show()
#Figura 4. En esta condicion, vemos que la potencia influye en las fallas por lo que encontramos uno de los culpables dependientes a las fallas
#Aqui se puede tomar decision sobre el mantenimiento que puedan tener o hasta donde llega la potencia de riesgo para la probabilidad de una falla
#dentro de un rango de potencia, como si fuera una probabilidad segun la moda de fallas dentro de un intervalo de potencia habitual a las fallas.

datos["fecha_registro"] = pd.to_datetime(datos["fecha_registro"])
eficiencia_promedio = datos.groupby("fecha_registro")["eficiencia_porcentual"].mean()

plt.figure(figsize=(10,5))
plt.plot(eficiencia_promedio.index, eficiencia_promedio.values, color="gold", marker="o", linestyle="-")
plt.title("Figura 5. Comportamientio de eficiencia energetica sobre el tiempo")
plt.grid(True, linestyle="--")
plt.show()
#Figura 5. Comportamiento sobre cada mes en la eficiencia energetica de 0 a 100%

#Ahora debemos examinar estos patrones segun las tablas.
#Podemos ver que la tabla 2, 4 y 5. 
#Generan patrones de errores por causas de potencias regulares que generar fallas constantes.
#Hay una ineficiencia en la tabla 5 que se puede ver en el patron con la tabla 4 y 2. Cada vez que hay un porcentaje bajo es porque la potencia sube y aumenta la
#probabilidad de fallar
#Conclusion para evitar estas fallas y aumentos de temperatura, revisiones constantes y mantenimiento con una modificacion de refrigeracion o cambio de mejor material de 
#disipacion termica
#Los riesgos son que si se continua asi es que deje de funcionar correctamente un servidor. Al aumentar la potencia aumenta el costo de energia innecesaria y por ultimo si se
#calienta tanto provocaria un incendio

#¿Qué medidas podrían implementarse para optimizar el rendimiento del sistema?

#Las medidas que se pueden tomar para nosotros los ingenieros electronicos especialisados en circuitos de baja potencia, media potencia y alta potencia.
#Tomar medidas preventivas segun el sensor que consume una potencia total. 
#Cambiar sensores por materiales mas resistentes al calor, o buscar un sistema que baje la energia cuando no se este usando, o usar datos intermediados para ahorrar
#Energia, como tomar un intervalo por hora, es decir, que cada hora tome un dato y se apague, luego de culminar esa hora se vuelve a encender y toma mediciones.




