# SemanaTecAD2021

///SNAKE///

Uno de nuestros proyectos fue una modificacion del juego clasico de snake. 
Estas modificaciones incluyen: 

1. Colores diferentes para la serpiente.
2. La serpiente al salir de los limites sale del extremo contrario del que originalmente salio.
3. La comida se mueve sobre el mapa y, al igual que la serpiente, si se sale de los extremos sale del lado contrario.
4. Mapa nuevo con diferentes paredes y colision en cada una.

Para lograr estas cosas, primero se tuvo que hacer un analisis del codigo para entender la manera en que funcionaba y
asi poder modificarlo de una manera mas facil. 

El primer cambio que se hizo fue el de los limites. Esto se hizo eliminando un condicional que checaba que la serpiente
estuviera en los limites y, en caso de ser falso, la detenia. Este se elimino y en lugar se hizo un condicional que 
primero checara si la serpiente se habia salido del limite, despues que checara en donde se salio, y dependiendo de su 
ubicacion cambiarla para que saliera del otro lado.

Despues se agrego lo del cambio de color. Esto se logro escogiendo un valor aleatorio del 1 al 3 al inicio del programa.
Y despues, dependiendo del numero, mediante un condicional esocger el color.

El movimiento de la comida se logro ya que la funcion move(), funciona de manera recursiva. Esto es que se esta llamando
una y otra vez. Lo unico que se hizo fue sumar en 10 la posicion x o y de la comida cada vez que se manda a llamar. Esto
hace que se mueva.

El mapa nuevo se creo primero imprimiendo en la pantalla unos cuadros negros que simularan paredes. Y despues mediante
condicionales se checaba que la serpiente no estuviera en las posiciones donde se encontraban estos cuartos. Este tracker
devuelve un valor de falso en caso de que la serpiente entre en uno de estos espacios. Deteniendo el juego.


///PONG///
En este juego realizamos las siguientes modificaciones:

1. Cambio de color para las barras cada que se abra el juego.
2. Cambio de velocidad de la pelota.

Además, intentamos añadir una segunda pelota para aumentar la dificultad del juego, sin embargo, esta modificación no ha salido. 

Para lograr el primer cambio, identificamos la función rectangle como nuestro espacio para cambiar este mismo elemento. En el código original, ya se encontraban las funciones begin_fill() y end_fill(), que se utilizan justamente para rellenar un objeto. Para elegir un color en específico, introducimos el comando fillcolor(col), con 'col' siendo la variable que define el color que tomarán las figuras. Fuera de la función 'rectangle' creamos la variable 'c' ('c' siendo un valor int) para poder usarle como parámetro de una condicional 'if'. El valor de 'c' se define al azar con un comando randrange() con los parámetros siendo entre 1 y 4. De ahí definimos las condicionales, con cada valor de 'c' dándole un color diferente a 'col'. Por ejemplo, si 'c'=3 entonces 'col'='pink' le da el color rosa a los rectángulos en nuestro juego.

Luego nos enfocamos en la velocidad del juego, ya que al inicio estaba muy rápido el juego. Aquí, lo que tuvimos que modificar fue el 'ontimer' que define la velocidad. Dentro del 'ontimer' se llama a la función draw() cuyo trabajo es mostrar todos los gráficos del juego y el "tiempo" de repetición. El segundo es el factor que decidimos cambiar. Tomando en cuenta que mientras menor sea el número, más rápido se mueve la pelota, aumentamos el valor de la segunda posición.

Finalmente, trabajamos en añadir una segunda pelota en el juego. Lo intentamos de múltiples maneras. En específico con los valores de ball (creando un ball1 y ball2) al igual de 2 valores aim para evitar que las pelotas siguieran exactamente la misma trayectoria y se empalmaran. Luego nos fuimos hasta abajo a los valores vectoriales y los duplicamos con sus respectivos nombres, pero se empezó a trabar. Si le movíamos al goto(x,y), el juego fallaba y al final lo dejamos en paz. En general, creemos que la segunda pelota sí existe, pero está empalmada con la original.
