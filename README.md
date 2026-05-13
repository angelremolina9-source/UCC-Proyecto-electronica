# UCC-Proyecto-electronica
Tema: Análisis de eficiencia energética y comportamiento operativo de sistemas electrónicos.
Escenario / contexto del problema:
Una empresa industrial ha instalado sensores en sus sistemas electrónicos para monitorear
variables como consumo energético, tiempo de operación, fallas y condiciones de
funcionamiento.
La información recolectada busca apoyar decisiones orientadas a mejorar la eficiencia energética,
reducir costos y prolongar la vida útil de los equipos.
El equipo deberá interpretar los datos disponibles y justificar técnicamente las conclusiones
obtenidas.



Estudiantes: Angel Remolina, Daniel Rovira, Oscar Lacera, Jose Mason

Se adopto utilizar como herramienta computacional Python por su libertad de hacer varias cosas, no solo ver graficos. 
Se nos proporciono  una libreria CSV de un conjunto de 1000 registros de operacion de equipos electronicos. 
El objetivo es identificar y aplicar el ser, saber y hacer sobre estas herramientas, nos piden hallar patrones de
consumo, fallas y ausencia de autocorrelacion.

Antes de empezar, se debe leer la serie de preguntas que nos piden, con eso podemos hacer una ruta para el camino mas 
visible en vez de ir a ciegas. Segun sigamos avanzando y encontrando tablas relacionadas, veremos patrones.
Procesaremos los datos en Python, por lo que agregamos Pandas, insertamos la variable "datos" como la caja para 
el dataset que nos proporsionaron.

Antes de seguir a trabajar, revisaremos el dataset, haremos comandos como .describe(), .info() y .head()
Esto para verificar que no se presenten datos nulos, sepamos cuantas columnas y como estan los datos y sus unidades.

Preguntas que nos piden analizar y ver patrones relacionados:
• ¿Qué equipos o sistemas presentan mayor consumo energético?
• ¿Existe relación entre condiciones de operación y fallas registradas?
• ¿Cómo se comporta la eficiencia energética en el tiempo?
• ¿Qué patrones indican posibles ineficiencias o riesgos operativos?
• ¿Qué medidas podrían implementarse para optimizar el rendimiento del sistema?

Al hacer las graficas con matplotlib, la primera grafica figura 1 nos muestra la sumatoria de toda la potencia consumida
por cada sensor electronico, tambien nos preguntan que sensores estan consumiendo mas potencia Kw, por lo que se hace un
filtro para hacer la misma tabla. Esto nos ayuda a tener un orden de analisis mas objetivo y encaminado a lo que 
estamos embarcando.

Los resultados mostraron patrones producidas por la columna potencia, demostraron tener una causa-efecto para las fallas
y la eficiencia energetica. Todo menos la temperatura, se denoto que la temperatura si estuviera baja o alta, de todas
formas fallaba. Esto es importante, pues, esto indicaria una falta de mantenimiento en vez de sobrecalentamiento.
<img width="1905" height="989" alt="image" src="https://github.com/user-attachments/assets/04836b82-31c6-4b5a-a65c-113d78303d0a" />
<img width="1699" height="911" alt="image" src="https://github.com/user-attachments/assets/fc8c747c-38c9-42dc-98c2-1f1ba5119cb5" />

Segun el analisis que se logro hacer gracias a los datos reales de la tabla y una visualizacion que detecto un patron
Se llego a la dicha que la potencia Kw puede ser un problema si este no se le da un mantenimiento adecuado.

<img width="1680" height="883" alt="image" src="https://github.com/user-attachments/assets/e02e820e-0b03-472a-b0c8-d86ac94e430c" />

#Datos mensuales
<img width="1622" height="867" alt="image" src="https://github.com/user-attachments/assets/37f988c6-27f2-416b-92e7-5d7f2c5c010b" />

Nuestra evidencia se dicta que, al calentarse aparatos de 4 Kw hacia abajo, no presentan un riesgo, siempre y cuando 
los materiales sean capaz de resistir el golpe de temperatura.
Aunque hablando de temperaturas y potencia, se noto que sin importar de la temperatura, existian fallas asi seria de
20 o 25 grados celsius. Esto se denota en la tabla scartter. Nuestra evidencia y un hecho absoluto en los sensores, es 
que si no se hace un buen mantenimiento, tiende a fallar produciendo mas temperaturas, mayor consumo innecesario y 
perdida total del sensor.

Es nuestra responsabilidad como ingenieros electronicos, saber la duracion, mantener un mantenimiento y un conocimiento 
preventivo para evitar tragedias, razones como no hacer estas cosas, se llevan a incendios, colapso de servidores, 
seguridad ineficiente y perdida en el consumo electrico que llega a costar aun mas que una nueva sensor es algo que 
esta como prioridad evitar, ya que un paso en falso y podemos poner en riesgos a demasiadas personas, somos la columna 
que dia tras dia no se ve y se toma medidas para no dañar la integridad de algun trabajador o genere perdidas en los 
activos de la empresa. Es una responsabilidad como profesional u un valor etico que se llama, honestidad.

La forma en que se controla los dispositivos debe ser igual al mantenimiento, si se usa mucho se le hace de vez en 
cuando, si se usa poco se hace 1 vez cada 2 semanas y asi. La recomendacion es tener un analisis critico enfrente de 
estas situaciones, garantizando el funcionamiento optimo por parte de los dispositivos electronicos








(Muchos se aprovechan del no saber del cliente y hace que se tome problemas innecesarios para cobrar un poco mas, 
siendo antietico, y poco profesional)



