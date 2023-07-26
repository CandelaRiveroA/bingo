from random import randint

def comprobar_valor_numerico(valor_a_comprobar: str) -> int:
    """ 
    Precondicion: Comprueba que el número ingresado por el usuario sea un valor númerico
                  La funcion recibe el argumento valor_a_comprobar ingresado por el usuario. Comprueba que este sea un valor 
                  numérico, de no serlo, muestra un mensaje de error y pide un nuevo ingreso continuamente hasta que el 
                  usuario ingrese un número.
    Postcondicion: Una vez que el usuario ingresa un número, lo transforma a numero entero y lo devuelve.
    """
    while not valor_a_comprobar.isnumeric():
        valor_a_comprobar = input("Error no ingresó un numero. Ingrese el número correspondiente : ")
    return int(valor_a_comprobar)

def comprobar_opciones(comprobar_menu: int, rango_inicio: int, rango_final: int) -> int:
    """ 
    Precondicion: Comprueba que el número ingresado por el usuario se encuentro entre un cierto rango
                  La funcion recibe el argumento valor_a_comprobar ingresado por el usuario. Comprueba que este valor 
                  numérico se encuentre entre el rango de rango_inicio y rango_final determinados por el programador.
    Postcondicion: Una vez que el usuario ingresa un número en este rango, lo transforma a numero entero y lo devuelve.
    """
    while ( comprobar_menu < rango_inicio or comprobar_menu > rango_final):
        comprobar_menu = int(comprobar_valor_numerico(input(f"Error. No eligió ninguna de las opciones. Eliga una de las opciones de {rango_inicio} a {rango_final}: ")))
    return comprobar_menu

def comprobar_si_no(texto: str) -> str:
    """ 
    Precondicion: Comprueba que el texto ingresado por el usuario sea un "si" o un "no".
                  La funcion recibe el argumento "texto" ingresado por el programador, esto es para que la función sea
                  iterable en distintas situaciones, cambiando la pregunta. Comprueba que el valor ingresado en la 
                  variable "palabra" sea "si" o "no", de no serlo, muestra un mensaje de error y pide un nuevo ingreso
                  continuamente hasta que el usuario ingrese un "si" o un "no".
    Postcondicion: Una vez que el usuario ingresa un "si" o un "no", lo devuelve.
    """
    palabra: str = input(f"¿Desea {texto}? Si / No : ")
    while (palabra.upper() != "SI" and palabra.upper() != "NO"):
        palabra = input("Error. Por favor solo ingrese Si o No: ")
    return palabra

def crear_numeros_no_repetidos(rango_inicial: int, rango_final: int, largo: int) -> list:
    """ 
    Precondicion: Crea una lista de números no repetidos dentro de un rango especifico de un cierto largo.
                  Recibe un rango inicial y un rango final que se convierte en el rango el cual se crearán números
                  aleatorios. Estos se guardan en un lista y esa lista se pasa por un set, el cual comprueba que los
                  no se repiten. La funcion sigue hasta que el set de números no repetidos llege al "largo" solicitado.
    Postcondicion: Una vez que la lista de números no repetidos llega a la longitud solicitada, la convierte en lista
                   para que sea más facil manipularla y la devuelve.
    """
    lst_num : list = []
    valor : str = str(randint(rango_inicial, rango_final))
    lst_num.append(valor)
    lista_numeros_no_repetidos : set = set(lst_num)
    while(len(lista_numeros_no_repetidos)<largo):
        valor : str = str(randint(rango_inicial, rango_final))
        lst_num.append(valor)
        lista_numeros_no_repetidos : set = set(lst_num)
    return list(lista_numeros_no_repetidos)

def crear_matriz(filas: int, columnas: int) -> list:
    """ 
    Precondicion: Crea una matriz de una cierta cantidad de filas y columnas.
                  Crea una matriz a partir de un número de filas y un número de columnas como lista de listas. Con 
                  esto se puede formar cualquier tipo de matriz de m x n o m x m. Todas las posiciones tienen un 0.
                  Solo crea la matriz y la rellena con información no relevante.
    Postcondicion: Una vez creada la matriz, la devuelve.
    """
    matriz : list = []
    for i in range(0,filas):
        filas : list = []
        for j in range(0,columnas):
            ingreso_num: int = 0
            filas.append(int(ingreso_num))
        matriz.append(filas)
    return matriz

def crear_carton(filas: int, columnas: int) -> list:
    """ 
    Precondicion: Crea un carton de juego de bingo.
                  Se crea una matriz de 3 filas y 9 columnas con la funcion crea_matriz. La variable inicio sirve para
                  que las columnas se creen dentro de los rangos especificados por trabajo, por eso se le suma 11 en 
                  cada ciclo. La lista columna recibe una lista de números no repetidos, los cuales se guardan en la
                  lista números uno por uno, para no generar una lista de listas. Debido a que esta lista esta compuesta
                  por las columnas, se guardan en la fila de cambiando el indice de 3. En lista_blanca se guardan las 
                  posiciones de los espacios blancos representados por "-". Se los agrega a la fila y esta se agrega al 
                  carton. Esto se realiza con las 3 filas del carton.
    Postcondicion: Una vez que el carton se termina de rellenar, se retorna el carton.
    """
    carton : list = []
    carton = crear_matriz(filas,columnas)
    numeros : list = []
    inicio = 1
    for i in range(0, columnas):
        columna : list = crear_numeros_no_repetidos(inicio,inicio+10,filas)
        for j in range (0,len(columna)):
            numeros.append(columna[j])
        inicio = inicio + 11
    indice = 0
    num_fila = 0
    for fila in carton:
        for j in range(0,len(fila)):
            fila[j] = numeros[indice]
            indice = indice + filas
        indice = num_fila + 1
        ##Espacios blancos
        lista_blanca : list = crear_numeros_no_repetidos(0,8,4)
        lista_blanca.sort()
        for j in range(0, 4):
            fila[int(lista_blanca[j])] = "-"
        carton[num_fila] = fila
        num_fila = num_fila + 1
    return carton

def crear_color(color: str) -> list:
    """ 
    Precondicion: Crea un matriz donde se guardan los colores de cada posición de un carton de juego de bingo.
                  Se crea una matriz de 3 filas y 9 columnas con la funcion crea_matriz. Se recorre cada fila y 
                  cada posición guardando un cierto color pasado como parametro. 
    Postcondicion: Una vez que la lista de lista de color se termina de rellenar, se retorna.
    """
    lista_color : list = []
    lista_color = crear_matriz(3, 9)
    for fila in lista_color:
        for j in range(0,len(fila)):
            fila[j] = color           
    return lista_color

def cambiar_color_numero(dic_colores: dict, carton_selecionado: int, fila_selecionado: int,
                         posicion_selecionado:int, color:str) -> None:
    """ 
    Precondicion: Cambia el color de una cierta posicion en la dic_colores.
                  La función recibe la posición de un numero a cambiarle el color a traves del número del carton, la
                  fila en la que se encuentra y su posicion. Ademas del color al cual se lo quiere cambiar. 
    """
    #color
    color_carton_auxiliar : list = dic_colores[carton_selecionado]
    color_fila_auxiliar : list = color_carton_auxiliar[fila_selecionado]
    color_fila_auxiliar[posicion_selecionado] = color

def crear_color_jugador(dic_colores: dict, num_cartones_jugador: list) -> None:
    """ 
    Precondicion: Cambia el color de los cartones seleccionados por el jugador.
                  Recibe la lista de colores según sus posiciones y una lista de los numeros seleccionados por el
                  jugador y los cambia de color con crear_color a el color Rojo.
    """
    for i in range(0,len(num_cartones_jugador)):
        dic_colores[num_cartones_jugador[i]] = crear_color("\033[91m")

def crear_color_fila_valida(cartones:dict, colores:dict, carton_selec:int, fila:int) -> None:
    """ 
    Precondicion: Cambia el color de los números de una fila cuando es declarada como premio y fue validada.
                  Recibe el diccionario de cartones y de colores, justo con el cartón y fila que fueron declaradas 
                  como premio. Evita los espacios en blanco y cambia de color solo los números a color Verde. 
    """
    j = 0
    while (j<len(cartones[carton_selec][fila])):
        if str(cartones[carton_selec][fila][j]).isnumeric():
            cambiar_color_numero(colores, carton_selec, fila, j, "\033[92m")
        j = j + 1

def crear_lista_numerica_fila(lista: list) -> list:
    """ 
    Precondicion: Toma una lista cualquiera y extrae todo número que exista en ella.
                  La función recorre la lista guardando todos los numeros encontrados en "lst_num".
    Postcondicion: Devuelve una lista unicamente de números enteros.
    """
    lst_num : list = []
    for i in range(0,len(lista)):
            if (str(lista[i]).isnumeric()):
                lst_num.append(int(lista[i]))
    return lst_num

def crear_lista_numerica_de_carton(lista: list) -> list:
    """ 
    Precondicion: Toma una lista de listas cualquiera y extrae todo número que exista en ella.
                  La función recorre las listas guardando  los elementos de las listas retornadas por la funcion
                  crear_lista_numerica_fila en "numeros".
    Postcondicion: Devuelve una lista "numeros" unicamente de números enteros.
    """
    numeros : list = []
    for elemento in lista:
        fila : list = crear_lista_numerica_fila(elemento)
        for i in range(0,len(fila)):
            numeros.append(fila[i])
    numeros.sort()
    return numeros

def comparar_dos_listas(lista_principal: list, lista_para_comparar: list, largo_comparar: int) -> int:
    """ 
    Precondicion: Compara la lista principal con la lista para comparar, pasando como parametro "largo_comparar" para
                  determinar hasta que posicion de la lista para comparar se debe revisar. 
    Postcondicion:
    """
    cantidad_de_repetidos : int = 0
    for j in range(0,len(lista_principal)):
        marca_repetido: bool = False
        k = 0
        while (k < largo_comparar and marca_repetido != True):
            if int(lista_principal[j]) == int(lista_para_comparar[k]):
                ### Cambiar a que devuelva una lista
                cantidad_de_repetidos = cantidad_de_repetidos + 1
                marca_repetido = True
            k = k + 1
    return cantidad_de_repetidos

def validar_carton_no_repetido(dic_carton:dict, carton_nuevo:list, indice:list) -> list:
    """ 
    Precondicion: Comprueba que no se repita un cartón creado con otro preexistente.
                  Revisa que el carton creado sea diferente a todo carton ya existente en la lista de cartones. 
    Postcondicion: Si el cartón está repetido, crea uno nuevo y lo retona. Sino retorna el argumento carton_nuevo.
    """
    repetido : bool = False
    cartones_no_repetidos : int = 0
    while (cartones_no_repetidos != len(dic_carton)):
        cartones_no_repetidos = 0
        lst_num_carton_nuevo : list = crear_lista_numerica_de_carton(carton_nuevo)
        g = 0
        repetido : bool = True
        while (repetido and g < len(dic_carton)):
            clave : int = indice[g]
            carton : list = dic_carton[clave]
            lst_num_carton : list = crear_lista_numerica_de_carton(carton)
            cantidad_de_repetidos : int = comparar_dos_listas(lst_num_carton_nuevo, lst_num_carton, len(lst_num_carton))
            if cantidad_de_repetidos >= 15 :
                repetido = False
                carton_nuevo : list = crear_carton(3,9)
            else:                    
                repetido = True
                cartones_no_repetidos = cartones_no_repetidos + 1
            g = g + 1
    return carton_nuevo

def imprimir_carton(lst_num: list, lista_color: list) -> None:
    """ 
    Precondicion: Imprime un carton solo entero.
                  Resive una lista numerico con sus lista de colores correspondiente y la imprime.
    """
    i = 0
    for f in lst_num: 
        color : list = lista_color[i]
        print ("{}{:<5} {}{:<5} {}{:<5} {}{:<5} {}{:<5} {}{:<5} {}{:<5} {}{:<5} {}{:<5} \033[00m".format(color[0], f[0], color[1], f[1], color[2], f[2], color[3], f[3], color[4], f[4], color[5], f[5], color[6], f[6], color[7], f[7], color[8], f[8]))
        i = i + 1

def imprimir_cartones(cartones: dict, colores: dict) -> None:
    """ 
    Precondicion: Imprime todos los cartones en pantalla.
                  Recive los cartones y sus colores, los imprime en pantalla en 2 columnas. Donde la columna 1 son los
                  impares y la columna 2 son los pares. 
    """
    i = 1
    while (i<len(cartones)):
        carton = i
        print(f"\nCartón {carton:<60} Cartón {carton+1}")
        j = 0
        num_fila = 0
        while (num_fila<3):
            print (f"{colores[carton][num_fila][0]}{cartones[carton][num_fila][0]:<5} {colores[carton][num_fila][1]}{cartones[carton][num_fila][1]:<5} {colores[carton][num_fila][2]}{cartones[carton][num_fila][2]:<5} {colores[carton][num_fila][3]}{cartones[carton][num_fila][3]:<5} {colores[carton][num_fila][4]}{cartones[carton][num_fila][4]:<5} {colores[carton][num_fila][5]}{cartones[carton][num_fila][5]:<5} {colores[carton][num_fila][6]}{cartones[carton][num_fila][6]:<5} {colores[carton][num_fila][7]}{cartones[carton][num_fila][7]:<5} {colores[carton][num_fila][8]}{cartones[carton][num_fila][8]:<20} {colores[carton+1][num_fila][0]}{cartones[carton+1][num_fila][0]:<5} {colores[carton+1][num_fila][1]}{cartones[carton+1][num_fila][1]:<5} {colores[carton+1][num_fila][2]}{cartones[carton+1][num_fila][2]:<5} {colores[carton+1][num_fila][3]}{cartones[carton+1][num_fila][3]:<5} {colores[carton+1][num_fila][4]}{cartones[carton+1][num_fila][4]:<5} {colores[carton+1][num_fila][5]}{cartones[carton+1][num_fila][5]:<5} {colores[carton+1][num_fila][6]}{cartones[carton+1][num_fila][6]:<5} {colores[carton+1][num_fila][7]}{cartones[carton+1][num_fila][7]:<5} {colores[carton+1][num_fila][8]}{cartones[carton+1][num_fila][8]:<20}\033[00m")
            num_fila = num_fila + 1
        i = i + 2

def crear_cartones(dic_cartones: dict, dic_colores: dict) -> None:
    """ 
    Precondicion: Crea los 10 cartones junto a sus lista de colores para el juego de bingo.
                  Crea uno por uno los 10 cartones, revisando que no se repitan entre ellos. Luego crea una lista
                  donde se guarda el color correspondiante a cada posición. Como es el inicio del juego todos los
                  cartones son azules. Una vez terminados los 10 cartones los imprime en pantalla.
    """
    i = 1
    while (i < 11):
        carton_auxiliar : list = crear_carton(3,9)
        carton_auxiliar = validar_carton_no_repetido(dic_cartones, carton_auxiliar, list(dic_cartones.keys()))
        dic_cartones[i] = carton_auxiliar
        dic_colores[i] = crear_color("\033[94m")
        i = i + 1
    imprimir_cartones(dic_cartones, dic_colores)

def elegir_numeros_de_cartones_jugador() -> list:
    """ 
    Precondicion: El jugador elige con cuales y cuantos cartones desea jugar.
                  El jugador ingresa los numeros de los cartones que desea, y se revisa que el maximo a elegir sea 5. 
                  Tambien se le permite al usuario ingresar 0 si desea jugar con una cantidad de cartones menor a 5.
    Postcondicion: Una vez seleccionados los cartones del jugador, retona los numeros en forma de lista.
    """
    lista_no_repetidos : set = {}
    lista : list = []
    numero_c = elegir_numero("Ingrese el número del cartón que quiere elegir (Ingrese 0 si terminó de elegir sus cartornes)",1,10)
    while (len(lista_no_repetidos)<5 and numero_c != 0):
        lista.append(numero_c)
        lista.sort()
        lista_no_repetidos = set(lista)
        if len(lista_no_repetidos)<5:
            numero_c = elegir_numero("Ingrese el número del cartón que quiere elegir (Ingrese 0 si terminó de elegir sus cartornes)",0,10)
    return list(lista_no_repetidos)

def elegir_numeros_de_cartones_computadora(num_jugador: list) -> list:
    """ 
    Precondicion: Determina cuales son los cartones con los cuales jugará la computadora.
                  Recibe los números de los cartones selecciones por el jugador y guarda en una lista todo número que el
                  jugador no halla elegido.
    Postcondicion: Retorna una lista de los numeros de los cartones de la computadora.
    """
    num_computadora : list = []
    j = 0
    for i in range(1,11):
        if num_jugador[j] == i:
            if (len(num_jugador)-1)>j:
                j = j + 1
        else:
            num_computadora.append(i)
    return num_computadora

def elegir_numero(texto: str, rango_inicial: int, rango_final: int) -> int:
    """ 
    Precondicion: Permite ingresar un número dentro de un rango.
                  La funcion recibe un texto sobre la condición o información del número deseado. Se comprueba que el
                  valor ingresado sea un número y dentro de un cierto rango.
    Postcondicion: Se devuelve ese valor ingresado como un número entero.
    """
    numero = int(comprobar_valor_numerico(input(f"{texto}: ")))
    numero = int(comprobar_opciones(numero, rango_inicial, rango_final))
    return numero

def esta_numero_en_list_numeros(lst_num: list, largo: int, numero: list) -> bool:
    """ 
    Precondicion: Comprueba si un numero especifico está en una lista de números.
    Postcondicion: Devuelve Falso si el número no es encontrado y verdadero si lo es encontrado.
    """
    marca_repetido : bool = False
    i = 0
    while (not marca_repetido and i<largo):
        if numero == int(lst_num[i]):
            marca_repetido = True
        i = i + 1
    return marca_repetido

def jugar_numeros_tachar(continuar: str, dic_cartones: dict, dic_colores: dict, num_jugador: list) -> None:
    """ 
    Precondicion: Pregunta al usuario si desea tachar (cambiar de color) un número y de ser asi hace, hasta que el 
                  jugador diga que no.
    """
    while(continuar.upper() == "SI"):
        numero: int = elegir_numero("Ingrese el número",1,99)
        buscar_numero(dic_cartones,dic_colores,num_jugador,numero)    
        continuar = comprobar_si_no("tachar algún número")  

def buscar_numero(dic_cartones: dict, dic_colores: dict, lst_num: list, num_buscado: int) -> None:
    """ 
    Precondicion: Busca un número dentro de un rango de cartones indicado por la lista de números "lst_num".
                  Revisa que número buscado este en alguna parte de los cartones seleccionados, sean los de la compu o los 
                  del jugador. Comprueba que lo que está por comparar sean números, para que no los compare con los blancos.
                  De encontrar el número, marca_repetido se convierte en verdadero y cambia de carton para buscarlo en el 
                  siguiente. Esto se debe a que si está bien hecho el cartón, solo puede aparecer 1 número por cartón
    """
    i = 0
    marca_repetido: bool = False
    while(i< len(lst_num)):
        marca_repetido = False
        num_fila = 0
        for fila in dic_cartones[lst_num[i]]:
            if not comprobar_fila_repetida(dic_colores,lst_num[i],num_fila):
                k = 0
                while (k < len(fila) and not marca_repetido):
                    if str(fila[k]).isnumeric() == True:
                        if num_buscado == int(fila[k]):
                            cambiar_color_numero(dic_colores, lst_num[i], num_fila, k, "\033[93m")
                            marca_repetido = True                        
                    k = k + 1
            num_fila = num_fila + 1
        if marca_repetido:
            print(f"\nCarton {lst_num[i]}")
            imprimir_carton(dic_cartones[lst_num[i]], dic_colores[lst_num[i]])
        i = i + 1

def buscar_lista_numero(cartones: dict, colores: dict, carton_selc: list, lst_num_buscar: list, ciclos: int) -> None:
    """ 
    Precondicion: Busca los numeros de una lista de numeros en los o el carton seleccionado y los tacha.  
    """
    h = 0
    while (h < ciclos-1):
        buscar_numero(cartones, colores, carton_selc, int(lst_num_buscar[h])) 
        h = h + 1 

def jugar_salio_seca (dic_cartones: dict, dic_colores: dict, bolillas: list,
                      nums_especiales: list, num_jugador: list, turno: int) -> None:
    """ 
    Precondicion: Juega el escenario en el cual la moneda de la jugada especial sale seca. Esto significa que uno de los cartones
                  del jugador es eliminado y reemplazado por uno nuevo. Este carton nuevo se comprueba que no se repita con todos
                  los otros cartones previos. El cartón eliminado es elegido de manera aleatoria. Compara con las listas de bolillas y con la de numeros de la jugada especial para tachar 
                  todos los números que hallan salido. Imprime todos los cambios en pantalla.
    """
    posicion : int = (randint(0,len(num_jugador)-1))
    eliminado : list = []
    eliminado.append(num_jugador[posicion])
    print(f"\033[96m Salió seca! \033[00m El cartón {eliminado[0]} será eliminado y se creará uno nuevo.")
    carton_auxiliar : list = crear_carton(3,9)
    carton_auxiliar = validar_carton_no_repetido(dic_cartones, carton_auxiliar, list(dic_cartones.keys()))
    dic_cartones[eliminado[0]] = carton_auxiliar
    dic_colores[eliminado[0]] = crear_color("\033[91m")
    # Tachar el carton
    buscar_lista_numero(dic_cartones, dic_colores, eliminado, bolillas, turno-1)
    buscar_lista_numero(dic_cartones, dic_colores, eliminado, nums_especiales, len(nums_especiales))

def jugar_salio_cara(dic_cartones: dict, dic_colores: dict,  num_jugador: list,
                     bolillas: list, turno: int, nums_especiales: list) -> str:
    """ 
    Precondicion: Juega el escenario en el cual la moneda de la jugada especial sale seca. Esto significa que el usuario puede
                  elegir un número que no halla salido previamente para tachar de todos sus cartones. La funcion comprueba que
                  no halla salido previamente y continua preguntando hasta que ingrese un número que aún no salió. 
    Postcondicion: Devuelve el número tachado para luego agregarlo a una lista de numeros especiales por la jugada. Esto
                   simplifica la comparación al momento de confimar linea, bingo, entre otras cosas.
    """
    print("\033[96m Salió cara! \033[00m Puede tachar un número de sus cartones. ")
    marca_repetido : bool = True
    while (marca_repetido):
        marca_repetido = False
        numero: int = elegir_numero("Ingrese el número", 1, 99)
        marca_repetido = esta_numero_en_list_numeros(bolillas, turno, numero)
        if not marca_repetido:
            marca_repetido = esta_numero_en_list_numeros(nums_especiales, len(nums_especiales), numero)   
        if marca_repetido:
            print(f"Error. El número {numero} ya apareció anteriormente.")
    buscar_numero(dic_cartones, dic_colores, num_jugador, numero)    
    return str(numero)

def menu_premios() -> int:
    """ 
    Precondicion: Muestra el menú de premios y hace que el usuario eleja una opción.
    Postcondicion: Devuelve el número de la opción elegida.
    """
    opciones_premios : list = ["\nMenú de premios:",
    "Para declarar el premio ingrese el número de la opción correspondiente sino ingrese el número 3 para salir",
    "Linea - 2000",
    "Bingo - 58000",
    "Salir"]
    print(opciones_premios[0])
    print(opciones_premios[1])
    for i in range(2,len(opciones_premios)):
        print(f"{i-1}) {opciones_premios[i]}")
    premio = elegir_numero("Ingrese alguna de las opciones", 1, 3)
    return premio

def valido_premio(lista_principal: list, bolillas: list, nums_especiales: list,
                  turno: int, valor_repetidos: int, tipo_premio: int, turno_jugador: int) -> bool:
    """ 
    Precondicion: Revisa que sea valida la declaración de un tipo de premio
    Postcondicion: De encontrar la cantidad requerida por valor_repetido devuelve verdadero si es igual o falso si no lo es.
                   Con esto luego se puede sumar puntos, cambiar el color, entre otras cosas, que ocurren dependiendo de que
                   el premio.
                   
    """
    premio_valido : bool = False
    if tipo_premio == 1:
        lista_auxiliar: list = crear_lista_numerica_fila(lista_principal)
    else:
        lista_auxiliar: list = crear_lista_numerica_de_carton(lista_principal)
    cant_repetidos : int = comparar_dos_listas(lista_auxiliar, bolillas, turno)
    if turno_jugador:
        cant_repetidos = cant_repetidos + comparar_dos_listas(lista_auxiliar, nums_especiales, len(nums_especiales))
    if cant_repetidos == valor_repetidos:
        premio_valido = True
    return premio_valido

def comprobar_fila_repetida(colores: dict, carton: int, fila: int) -> bool:
    """ 
    Precondicion: Revisa que la fila de la cual se quiere declarar premio, no fue declarada premio antes.
                  La función revisa que la fila pasada no esté pintada de verde, lo que indica que fué declarada premio
                  con anterioridad.
    Postcondicion: Retorna Falso si nunca fue declarada premio y Verdadero (True) si ya fue declarada premio anteriormente.
    """
    k = 0
    fila_repetida : bool = False
    while not fila_repetida and k<9:
        if colores[carton][fila][k] == "\033[92m":
            fila_repetida = True
        k = k + 1
    return fila_repetida

def jugar_premios(cartones: dict, colores: dict, puntos: dict, num_jugador: list, bolillas: list,
                  nums_especiales: list, turno: int, tipo_premio: int) -> bool:
    """ 
    Precondicion: El jugador elige de cual carton quiere declarar un premio. Se comprueba que el carton seleccionado sea 
                  uno de los cartones del usuario. Dependiendo el tipo de premio, se le solicita información adicional.
                  Confirma que los premios no hallan sido anteriormente declarados y luego confima que sea valida su declaración. 
                  De estar todo correcto suma los puntos y los imprime en pantalla. De no ser valido imprime un mensaje de error. 
    Postcondicion: Devuelve premio_valido como verdadero si pasa la comprobación y falso en cualquier otro caso.
    """
    carton_seleccionado = elegir_numero("Ingrese el cartón del cual quiere declarar bingo", 1, 10)
    premio_valido : bool = False
    encontrado : bool = False
    i = 0
    while (i<len(num_jugador) and not encontrado):
        if carton_seleccionado == num_jugador[i]:
            encontrado = True
            if tipo_premio == 1:
                fila_seleccionado = elegir_numero("Ingrese la fila del cartón del cual quiere declarar línea", 1, 3)
                fila_repetida : bool = comprobar_fila_repetida(colores, carton_seleccionado, fila_seleccionado-1)
                if not fila_repetida:
                    premio_valido = valido_premio(cartones[carton_seleccionado][fila_seleccionado-1], bolillas,
                                                  nums_especiales, turno, 5, tipo_premio, encontrado)
                    if premio_valido:
                        crear_color_fila_valida(cartones, colores, carton_seleccionado, fila_seleccionado-1)
                        puntos["puntos_jugador"] = puntos["puntos_jugador"] + 2000
                        print("\nPuntos del jugador: ", puntos["puntos_jugador"])
                    else:
                        print("No todos los números de la fila seleccionada han salido. No se suman puntos.")
                else:
                    print("Esta fila ya fue declarada como premio. No se suman puntos.")
            else:
                premio_valido = valido_premio(cartones[carton_seleccionado],bolillas,nums_especiales,
                                              turno,15,tipo_premio,encontrado)
                if premio_valido:
                    puntos["puntos_jugador"] = puntos["puntos_jugador"] + 58000
                    print(f"El jugador declara con el cartón {carton_seleccionado} Bingo!")
                else:
                    puntos["puntos_jugador"] = 0
                    print(f"Cantaste bingo con el cartón {carton_seleccionado} erroneamente. No todos tus números han salido. Perdiste automaticamente.\n¡Ganó la computadora!")
        i = i + 1
        if (i == len(num_jugador) and not encontrado):
            carton_seleccionado = elegir_numero("ERROR. Ingresó un número de cartón que no es suyo. Ingrese el cartón del cual quiere declarar bingo",1,10)
            i = 0
    return premio_valido

def remover_bolillas_num_especiales(nums_especiales: list, bolillas: list, turno: int) -> list:
    """ 
    Precondicion: Revisa que los números de la lista de nums_espaciales no halla salido antes en la lista de bolillas.
                  De ser que exista algún número asi lo remueve de la lista de num_espaciales. Esto es para que esta
                  ultima lista solo se componga de números que aún no han salido de la lista de bolillas y al usarla
                  no se repitan numeros en ambas listas, lo cual puede generar errores al momento de, por ejemplo, 
                  declarar premios.
    Postcondicion: Retorna la lista de num_especiales en caso de algun cambio.
    """
    j = 0
    marca_repetido: bool = False
    while (j <len(nums_especiales) and not marca_repetido):
        marca_repetido = False
        k = 0
        while (k < turno and not marca_repetido):
            if int(nums_especiales[j]) == int(bolillas[k]):
                marca_repetido = True
                nums_especiales.remove(bolillas[k])
                j = j - 1
            k = k + 1
        j = j + 1
    return nums_especiales

def jugar_turno(dic_cartones: dict, dic_colores: dict, dic_puntos: dict, num_jugador: list, num_computadora: list) -> bool:
    """ 
    Precondicion: Juega hasta que se terminen los turnos o alguien declare bingo.
                  Al comenzar crea una lista con las 99 bolillas no repetidas. Sabe cual bolilla debe sacar a traves de saber
                  en que turnos esta situado. Cada 4 turnos aparece la jugada especial, si es 1 salio seca y si es 0 salió cara.
                  Los números seleccionados por el usuario debido a la implementación de la jugada especial se guardan en una 
                  lista para usarlos en distintas situaciones como comprobaciones/validaciones de premios. Cada turno se revisa
                  que los numeros de esta lista no hallan salido, si salio algún número que existe en esta lista. Ese numero en 
                  las lista de numeros especiales es eliminado para no comprovar más de una vez el mismo numero al momento de la
                  declaracion de premios. Luego se le pregunta al usuario si desea tachar numeros. Siguente a eso se le pregunta
                  al jugador si desea declarar premios. Y a eso le sigue el turno de la computadora donde hace los mismos pasos
                  de forma automatica, tachar numeros que hallan salido, declarar linea o bingo solo si lo tiene. El ciclo termina
                  cuando uno de los 2 declara bingo. La máquina jamás declarará bingo de sin tenerlo validado. El único que puede 
                  declarar bingo de manera incorrecta es el jugador. Si el jugador declara bingo y al comprobarlo se demuesta que
                  este no es valido, pierde automaticamente, imprimiendose un mensaje por pantalla del error. De ser lo contrario,
                  y el bingo es valido, se saltea el turno de la computadora y se gana automaticamente.
    Postcondicion: Devuelve el bingo_valido como verdadero si la declaracion del bingo es valido. Devuelve falso en cualquier
                   otro caso.
    """
    bolillas : list = crear_numeros_no_repetidos(1,99,99)
    lst_num_especial : list = []
    turno : int =  1
    bingo_declarado : bool = False
    bingo_valido : bool = False

    while(turno<len(bolillas)+1 and not bingo_declarado):
        print(f"\nTurno: {turno}")
        imprimir_cartones(dic_cartones, dic_colores)
        print("\nCartones del jugador: \033[91m Rojo \033[00m                                        Cartones de la computadora: \033[94m Azul \033[00m")
        print(f"Puntos del jugador: {dic_puntos['puntos_jugador']:<47} Puntos de la computadora: {dic_puntos['puntos_computadora']}")
        print(f"Salió la bolilla número: {bolillas[turno-1]}")
        lst_num_especial = remover_bolillas_num_especiales(lst_num_especial,bolillas,turno)

        ### Turno jugador
        #Jugada especial
        if (turno % 4) == 0:
            print("\n\033[95m Jugada especial! \033[00m")
            jugada_especial : int = randint(0,1)
            if jugada_especial == 1:
                jugar_salio_seca(dic_cartones,dic_colores,bolillas,lst_num_especial,num_jugador,turno)      
            else:
                lst_num_especial.append(jugar_salio_cara(dic_cartones,dic_colores,num_jugador,bolillas,turno,lst_num_especial))

        ## Tachar números
        continuar : str = comprobar_si_no("tachar algún número")
        jugar_numeros_tachar(continuar,dic_cartones,dic_colores,num_jugador)
        
        #Premios
        continuar : str = comprobar_si_no("declarar algún premio")
        while(continuar.upper() == "SI" and bingo_declarado == False):
            elegir_premios= menu_premios()
            if elegir_premios == 1:
                fila_valido : bool = jugar_premios(dic_cartones,dic_colores,dic_puntos,num_jugador,bolillas,
                                                   lst_num_especial,turno,elegir_premios)
            elif elegir_premios == 2:
                bingo_declarado = True
                bingo_valido = jugar_premios(dic_cartones,dic_colores,dic_puntos,num_jugador,bolillas,
                                             lst_num_especial,turno,elegir_premios)
            if not bingo_declarado: 
                continuar = comprobar_si_no("declarar algún premio")
        
        if not bingo_declarado:    
            ###Turno computadora
            buscar_numero(dic_cartones,dic_colores,num_computadora,int(bolillas[turno-1]))
            if turno >= 5:
                i = 0
                while (i<len(num_computadora)):
                    num_fila = 0
                    while (num_fila < 3):
                        fila_repetida : bool = comprobar_fila_repetida(dic_colores,num_computadora[i], num_fila)
                        if not fila_repetida:
                            premio_valido = valido_premio(dic_cartones[num_computadora[i]][num_fila], bolillas,
                                                          lst_num_especial, turno, 5, 1, False)
                            if premio_valido:
                                crear_color_fila_valida(dic_cartones, dic_colores, num_computadora[i], num_fila)
                                dic_puntos["puntos_computadora"] = dic_puntos["puntos_computadora"] + 2000
                        num_fila = num_fila + 1
                    i = i + 1
                if turno >= 15:
                    i = 0
                    while (i<len(num_computadora)):
                        premio_valido = valido_premio(dic_cartones[num_computadora[i]], bolillas,
                                                      lst_num_especial, turno, 15, 2, False)
                        if premio_valido:
                            bingo_valido = True
                            bingo_declarado = True
                            print(f"La computadora declara con el cartón {num_computadora[i]} Bingo!")
                            dic_puntos["puntos_computadora"] = dic_puntos["puntos_computadora"] + 58000
                        i = i + 1
        turno = turno + 1    
    return bingo_valido

def main(): 
    lst_cartones: dict = {}
    lst_colores: dict = {}
    puntos : dict = {
        "puntos_jugador": 0,
        "puntos_computadora": 0 }
    
    #Preparativos creamos todos los cartones
    crear_cartones(lst_cartones, lst_colores)

    #Elegir cartones
    num_cartones_jugador: list = elegir_numeros_de_cartones_jugador()
    num_cartones_jugador.sort()
    num_cartones_compu: list = elegir_numeros_de_cartones_computadora(num_cartones_jugador)
    
    #Cambio colores jugador
    crear_color_jugador(lst_colores, num_cartones_jugador)

    #Juego
    bingo_valido : bool = False 
    bingo_valido = jugar_turno(lst_cartones, lst_colores, puntos, num_cartones_jugador, num_cartones_compu)

    #Final del juego
    if bingo_valido:        
        if puntos["puntos_computadora"] > puntos["puntos_jugador"]:
            print("¡Ganó la computadora! Puntos de la computadora : ", puntos["puntos_computadora"])
        else:
            print("¡Ganó el usuario! Puntos del jugador : ", puntos["puntos_jugador"])
main()