# Proyecto Final

## Resumen del problema

Este proyecto nace con el objetivo de ayudar a una empresa de paquetería a mejorar la forma en la que entrega paquetes a diferentes ciudades. El problema principal era que no se tenía una manera clara y automática de saber cuál era la mejor ruta para entregar los paquetes, lo que podía causar retrasos, recorridos más largos de lo necesario y mayor gasto en gasolina o tiempo.

Para resolver esto, se pensó en crear un sistema que, por medio de programación, pueda organizar las rutas, mostrarlas de manera clara y calcular cuál es la más corta entre dos lugares. De esta manera, el personal de la empresa puede tomar decisiones más rápidas y efectivas sobre por dónde deben pasar los vehículos de reparto.

El sistema se desarrolló por etapas, empezando con una solución básica y luego agregando más funciones y mejorando el rendimiento. Primero se usaron listas simples, luego árboles binarios y finalmente se trabajó con grafos. Cada versión fue un paso más adelante en complejidad y eficiencia.

Gracias a este proyecto, la empresa puede organizar mejor sus entregas, reducir los tiempos de viaje, evitar rutas largas o innecesarias, y mejorar la experiencia del cliente.

## Etapas Desarrolladas

### Primera etapa - Listas Enlazadas

En esta etapa inicial, se utilizó una lista simple para guardar todas las rutas. Cada ruta tenía un destino y su distancia en kilómetros. Se podían agregar nuevas rutas, mostrarlas todas y ordenarlas por distancia con un método sencillo llamado Bubble Sort. Así, se podía encontrar la ruta más corta. Aunque este enfoque era funcional, cuando se agregaban muchas rutas, el sistema empezaba a volverse lento y poco eficiente. Esta etapa fue útil para entender el problema y comenzar a organizar los datos.

### Segunda etapa - Árboles

Luego se mejoró el sistema utilizando un árbol binario de búsqueda. Este tipo de estructura permite organizar las rutas de manera automática: las rutas más cortas se colocan a la izquierda y las más largas a la derecha. Esto hace que sea mucho más rápido encontrar la ruta más cercana. También se puede ver la forma del árbol para entender cómo están distribuidas las rutas. Esta etapa permitió manejar más datos sin que el sistema se volviera lento, y mejoró bastante el rendimiento comparado con las listas.

### Tercera etapa - Grafos

En la etapa final se utilizó un grafo, que es una estructura que permite conectar muchas ciudades entre sí como si fueran puntos en un mapa con caminos. Esto hace posible representar rutas complejas entre varios lugares. Con esta estructura, el sistema puede calcular la ruta más corta entre cualquier par de ciudades usando el algoritmo de Dijkstra, que es muy eficiente. Además, se diseñó una ventana interactiva (una interfaz gráfica) donde el usuario puede escribir los datos, ver todas las rutas y calcular la mejor opción de manera visual y fácil. Esta versión es mucho más completa y práctica para usar en la vida real.

## Integrantes

Daniel Fernando Arias Rivero - 2240078

Warly Andrés Peña Rangel - 2240057

Diego Andrés Rojas Robles - 2241691

Luis Alejandro Vargas Reyes - 2240081

