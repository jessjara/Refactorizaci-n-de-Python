def introducirComentario(point):
        print( 'Introduzca sus comentarios.' )
        comment = input()
        post = f'punto: {point} comentario: {comment}'
        file_pc = open("data.txt", 'a')
        file_pc.write( f'{ post } \n' )
        file_pc.close()




def verificarPuntajeResenha(point):
    while True:
        point = int(point)
        if point <= 0 or point > 5:
            print( 'Por favor, introduzca un valor entre el 1 y 5' )
            point = input()
        else:
            introducirComentario(point)
            break
            

def ingresar_resenha():
   while True:
                print( 'Por favor, introduzca una puntuación en una escala de 1 a 5' )
                point = input()
                if point.isdecimal():
                    point = int(point)
                    if  point <= 0 or point > 5: 
                        verificarPuntajeResenha(point)
                        break
                    else:
                        introducirComentario(point)
                        break
                else:
                    print( 'Introduzca los puntos de valoración como números' )

def imprimirResenhasGuardadas():
        print( 'Resultados hasta la fecha' )
        read_file = open("data.txt", "r")
        print( read_file.read() )
        read_file.close()


while True:
    print( 'Seleccione el proceso que desea aplicar' )
    print( '1:Introducir puntos de evaluación y comentarios' )
    print( '2:Comprueba los resultados hasta ahora' )
    print( '3:Terminar.' )
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            ingresar_resenha()
        elif num == 2:
            imprimirResenhasGuardadas()
        elif num == 3:
          print( 'Terminación.' )
          break
        else:
            print( 'Introduzca de 1 a 3' )
    else:
        print( 'Por favor, introduzca del 1 a 3' )