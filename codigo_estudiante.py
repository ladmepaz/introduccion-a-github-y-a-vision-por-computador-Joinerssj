import numpy as np
from PIL import Image

def leer_imagen(ruta_imagen):
    """
    Lee una imagen a partir de una ruta y retorna el objeto imagen usando la librería PIL.
    """
    img = Image.open(ruta_imagen)
    return img

def obtener_info_imagen(img):
    """
    Recibe una imagen y retorna el número de canales y las dimensiones.
    """
    modo = img.mode
    if modo == 'L':
        num_canales = 1
    elif modo == 'RGB':
        num_canales = 3
    elif modo == 'RGBA':
        num_canales = 4
    else:
        num_canales = len(modo)
    
    dimensiones = img.size
    return num_canales, dimensiones

def imagen_a_arreglo(img):
    """
    Convierte una imagen de tipo PIL a un arreglo de NumPy.
    """
    arreglo = np.array(img)
    return arreglo

def estadisticas_intensidad(arreglo_img):
    """
    Calcula el promedio y la desviación estándar de las intensidades de los píxeles.
    """
    promedio = np.mean(arreglo_img)
    desviacion_estandar = np.std(arreglo_img)
    return promedio, desviacion_estandar

def estadisticas_por_canal(arreglo_img):
    """
    Calcula el promedio y la desviación estándar de las intensidades de los píxeles por canal.
    """
    if len(arreglo_img.shape) == 2:
        promedio = np.mean(arreglo_img)
        desviacion_estandar = np.std(arreglo_img)
        resultados = {
            'Canal_1': {
                'Promedio': promedio,
                'Desviación Estándar': desviacion_estandar
            }
        }
    elif len(arreglo_img.shape) == 3:
        resultados = {}
        num_canales = arreglo_img.shape[2]
        
        for canal in range(num_canales):
            promedio = np.mean(arreglo_img[:, :, canal])
            desviacion_estandar = np.std(arreglo_img[:, :, canal])
            resultados[f'Canal_{canal+1}'] = {
                'Promedio': promedio,
                'Desviación Estándar': desviacion_estandar
            }
    else:
        raise ValueError("El arreglo de imagen debe tener 2 o 3 dimensiones.")
    
    return resultados
