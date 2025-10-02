from PIL import Image, ImageDraw, ImageFont

def agregar_marca_de_agua_simple(ruta_imagen_entrada, ruta_imagen_salida, texto_marca_agua):
    """
    Agrega una marca de agua textual simple en la esquina inferior derecha.
    """
    try:
        # 1. Abrir la imagen
        img = Image.open(ruta_imagen_entrada).convert("RGBA")
        
        # 2. Crear un objeto ImageDraw para dibujar sobre la imagen
        dibujo = ImageDraw.Draw(img)
        
        # 3. Definir la fuente y el tamaño (ajusta la ruta a una fuente TTF si quieres otra)
        # Se usa una fuente por defecto del sistema o una genérica
        try:
            # Intentar usar una fuente simple y común (ajusta el tamaño si es necesario)
            fuente = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            # Usar la fuente por defecto de Pillow si no encuentra 'arial.ttf'
            fuente = ImageFont.load_default()
            print("Usando fuente por defecto.")

        # 4. Definir el color y la posición
        # Color blanco semitransparente (R, G, B, Alpha)
        color = (255, 255, 255, 150) 
        
        # Obtener el ancho y alto del texto para calcular la posición
        # (Esto requiere Pillow 9.2.0 o superior; usa dibujo.textsize() si usas una versión antigua)
        bbox = dibujo.textbbox((0, 0), texto_marca_agua, font=fuente)
        ancho_texto = bbox[2] - bbox[0]
        alto_texto = bbox[3] - bbox[1]

        # Posición (ajustar X e Y para un margen desde la esquina inferior derecha)
        margen = 10
        x = img.width - ancho_texto - margen
        y = img.height - alto_texto - margen
        
        # 5. Dibujar el texto en la posición calculada
        dibujo.text((x, y), texto_marca_agua, font=fuente, fill=color)
        
        # 6. Guardar la imagen de salida
        # Usamos 'PNG' para conservar la transparencia si la capa Alpha es necesaria.
        img.save(ruta_imagen_salida, "PNG")
        print(f"Marca de agua agregada con éxito a: {ruta_imagen_salida}")

    except FileNotFoundError:
        print(f"Error: La imagen de entrada '{ruta_imagen_entrada}' no fue encontrada.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# --- USO DE EJEMPLO ---
# Asegúrate de tener una imagen llamada 'input.jpg' o cambia el nombre aquí
agregar_marca_de_agua_simple("input.jpg", "output_watermarked.png", "© Mi Marca de Agua")