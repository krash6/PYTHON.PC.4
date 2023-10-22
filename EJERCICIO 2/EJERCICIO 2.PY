import pyfiglet
import random

# Obtener la lista de fuentes admitidas por pyfiglet
def get_supported_fonts():
    return pyfiglet.FigletFont.getFonts()

# Solicitar al usuario el nombre de la fuente o seleccionar aleatoriamente
def get_user_selected_font():
    fonts = get_supported_fonts()
    font_name = input(f"Por favor, ingrese el nombre de la fuente ({', '.join(fonts)}): ")
    if font_name.strip() == '':
        font_name = random.choice(fonts)
    return font_name

# Solicitar al usuario el texto
def get_user_text():
    return input("Ingrese el texto que desea imprimir: ")

# Imprimir el texto utilizando la fuente seleccionada
def print_text_with_font(font, text):
    custom_fig = pyfiglet.Figlet(font=font)
    print(custom_fig.renderText(text))

if __name__ == '__main__':
    font_name = get_user_selected_font()
    user_text = get_user_text()
    print_text_with_font(font_name, user_text)