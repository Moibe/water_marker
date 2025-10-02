from PIL import Image, ImageDraw, ImageFont
import time

def agregar_marca_de_agua_con_contorno(ruta_imagen_entrada, texto_marca_agua):
    """
    Agrega una marca de agua textual con texto negro y contorno blanco
    en la esquina inferior derecha.
    """
    try:
        # 1. Abrir la imagen y convertir a RGBA para soportar transparencia
        img = Image.open(ruta_imagen_entrada).convert("RGBA")
        
        # 2. Crear un objeto ImageDraw para dibujar sobre la imagen
        dibujo = ImageDraw.Draw(img)
        
        # 3. Definir la fuente y el tamaño
        try:
            # Intentar usar una fuente simple y común (ajusta el tamaño si es necesario)
            fuente = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            # Usar la fuente por defecto de Pillow si no encuentra 'arial.ttf'
            fuente = ImageFont.load_default()
            print("Usando fuente por defecto.")

        # 4. Definir colores
        color_texto_negro = (0, 0, 0, 200)   # Negro con cierta transparencia
        color_contorno_blanco = (255, 255, 255, 200) # Blanco con cierta transparencia
        ancho_contorno = 2 # Puedes ajustar el grosor del contorno

        # 5. Calcular la posición del texto
        # Obtener el ancho y alto del texto para calcular la posición
        bbox = dibujo.textbbox((0, 0), texto_marca_agua, font=fuente)
        ancho_texto = bbox[2] - bbox[0]
        alto_texto = bbox[3] - bbox[1]

        # Posición (ajustar X e Y para un margen desde la esquina inferior derecha)
        margen = 10
        x_base = img.width - ancho_texto - margen
        y_base = img.height - alto_texto - margen
        
        # 6. Dibujar el contorno (varios trazos alrededor del texto principal)
        # Esto crea un efecto de contorno dibujando el texto varias veces ligeramente desplazado
        for dx in range(-ancho_contorno, ancho_contorno + 1):
            for dy in range(-ancho_contorno, ancho_contorno + 1):
                if dx != 0 or dy != 0: # Para no dibujar el texto principal dos veces
                    dibujo.text((x_base + dx, y_base + dy), texto_marca_agua, font=fuente, fill=color_contorno_blanco)
        
        # 7. Dibujar el texto principal (negro) sobre el contorno
        dibujo.text((x_base, y_base), texto_marca_agua, font=fuente, fill=color_texto_negro)
        
        # 8. Guardar la imagen de salida

        timestamp_segundos = int(time.time())
        print(timestamp_segundos)

        ruta_imagen_entrada
        nuevo_nombre = f"{ruta_imagen_entrada}-{timestamp_segundos}.jpg"

        img.save(nuevo_nombre, "PNG")
        print(f"Marca de agua con contorno agregada con éxito a: {nuevo_nombre}")

    except FileNotFoundError:
        print(f"Error: La imagen de entrada '{ruta_imagen_entrada}' no fue encontrada.")
    except IOError:
        print(f"Error: Problema al cargar la fuente o la imagen. Asegúrate de que 'arial.ttf' exista o usa ImageFont.load_default().")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- USO DE EJEMPLO ---
# Asegúrate de tener una imagen llamada 'input.jpg' o cambia el nombre aquí
# Puedes probar con 'arial.ttf' si la tienes instalada o el código usará la fuente por defecto.
agregar_marca_de_agua_con_contorno("input.jpg", "splashmix.ink")