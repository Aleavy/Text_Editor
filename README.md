# Tkinter Text Editor Project

## Descripción
Este proyecto es una aplicación de editor de texto creada con Python y la biblioteca Tkinter. La aplicación proporciona funcionalidades básicas para editar texto y permite agregar resaltado de colores que persiste al guardar el archivo.

## Características
1. **Incrementar el tamaño de la fuente:** Cambia el tamaño del texto en el editor a uno mayor.
2. **Reiniciar la fuente al estado inicial:** Restaura el tamaño de la fuente al valor predeterminado.
3. **Guardar archivo:** Permite guardar el contenido del editor en un archivo de texto, conservando cualquier resaltado aplicado.
4. **Abrir archivo:** Carga un archivo de texto existente en el editor.
5. **Resaltado de texto:**
   - **Color rojo:** Presiona `Ctrl + R` para resaltar el texto seleccionado en rojo.
   - **Color azul:** Presiona `Ctrl + F` para resaltar el texto seleccionado en azul.
   - **Color amarillo:** Presiona `Ctrl + Q` para resaltar el texto seleccionado en amarillo.
6. **Persistencia del resaltado:** Los colores de resaltado se guardan con el texto, de modo que al abrir un archivo previamente guardado, el resaltado persiste.

## Instalación
1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Clona este repositorio o descarga los archivos.
   ```bash
   git clone https://github.com/Aleavy/Text_Editor.git
   ```
3. Navega al directorio donde clonaste el repositorio Text_Editor y crea 2 carpetas "private" y dentro de ella "tags".

## Uso
1. Ejecuta el archivo principal:
   ```bash
   python text_editor.py
   ```
2. Utiliza las opciones disponibles en la interfaz para realizar ediciones y resaltados en el texto.

## Atajos de teclado
- **Ctrl + R:** Resalta el texto seleccionado en rojo.
- **Ctrl + F:** Resalta el texto seleccionado en azul.
- **Ctrl + Q:** Resalta el texto seleccionado en amarillo.
- **Ctrl + B:** Vuelve el texto en negritas.
- **Ctrl + S:** Guarda el archivo (extension por defecto: .txt).

## Estructura del proyecto
- **text_editor.py:** Archivo principal que contiene la lógica de la aplicación.


## Notas
- Asegúrate de seleccionar el texto antes de usar los atajos de resaltado.
- Los colores de resaltado se guardarán en un formato compatible al abrir el archivo posteriormente.

## Contribución
Si deseas contribuir a este proyecto:
1. Haz un fork del repositorio.
2. Crea una rama para tu función (“feature/nueva-funcionalidad”).
3. Realiza un pull request describiendo los cambios realizados.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.

