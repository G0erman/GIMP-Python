###########################################################################
# Parámetros
# x #Coordenada x de la posición inicial del texto
# y #Coordenada y de la posición inicial del texto
# color #utliza RGB
#		#(255, 255, 255)Color blanco.
# Texto #string
###########################################################################
def efecto_escritura(x, y, color,texto):
    texto_completo = texto
    ultimo_texto=''
    imagen_inicial = gimp.image_list()[0]    
    #Color del texto 
    gimp.set_foreground(color)
	
	# Parámetros Fuente
    fontname= 'Sans' #Tipo de letra
    size_type=PIXELS 
    size= 30 #Tamaño
    antialias = True
    border = 0
    #y = 0 
    #x = 0 
    drawable = None
    image = imagen_inicial    
    for i in texto_completo:
        ultimo_texto=ultimo_texto+i
        layer = pdb.gimp_text_fontname(image, drawable, x, y, ultimo_texto, border, antialias, size, size_type, fontname)
        print(ultimo_texto)
