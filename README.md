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
