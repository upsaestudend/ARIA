import streamlit as st
import math

def calcular_area(figura, valores):
    """Devuelve el área de la figura geométrica."""
    if figura == "cuadrado":
        lado = valores["lado"]
        return lado ** 2
    elif figura == "triangulo":
        base = valores["base"]
        altura = valores["altura"]
        return (base * altura) / 2
    elif figura == "rectangulo":
        base = valores["base"]
        altura = valores["altura"]
        return base * altura
    elif figura == "circulo":
        radio = valores["radio"]
        return math.pi * (radio ** 2)
    else:
        raise ValueError("Figura no válida")

def calcular_perimetro(figura, valores):
    """Devuelve el perímetro de la figura geométrica."""
    if figura == "cuadrado":
        lado = valores["lado"]
        return 4 * lado
    elif figura == "triangulo":
        base = valores["base"]
        return 3 * base  # Triángulo equilátero
    elif figura == "rectangulo":
        base = valores["base"]
        altura = valores["altura"]
        return 2 * (base + altura)
    elif figura == "circulo":
        radio = valores["radio"]
        return 2 * math.pi * radio
    else:
        raise ValueError("Figura no válida")

def main():
    # Crear columnas para título e imagen
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Calculadora de área y perímetro de figuras geométricas")
    with col2:
        st.image("imagen5.png", width=120)

    st.sidebar.header("Selección de figura")
    figura_opciones = {
        "Cuadrado": "cuadrado",
        "Triángulo": "triangulo",
        "Rectángulo": "rectangulo",
        "Círculo": "circulo"
    }
    eleccion = st.sidebar.selectbox("Elige la figura", list(figura_opciones.keys()))
    figura = figura_opciones[eleccion]

    st.sidebar.markdown("---")
    st.sidebar.write("Ajusta las dimensiones en la sección principal.")

    valores = {}

    # Entradas dinámicas según la figura
    if figura == "cuadrado":
        valores["lado"] = st.number_input("Lado del cuadrado (cm)", min_value=0.0, value=5.0, step=0.1)

    elif figura == "triangulo":
        valores["base"] = st.number_input("Base del triángulo (cm)", min_value=0.0, value=5.0, step=0.1)
        valores["altura"] = st.number_input("Altura (cm)", min_value=0.0, value=4.0, step=0.1)
        st.caption("Nota: se asume triángulo equilátero para el cálculo del perímetro.")

    elif figura == "rectangulo":
        valores["base"] = st.number_input("Base del rectángulo (cm)", min_value=0.0, value=6.0, step=0.1)
        valores["altura"] = st.number_input("Altura (cm)", min_value=0.0, value=3.0, step=0.1)

    elif figura == "circulo":
        valores["radio"] = st.number_input("Radio del círculo (cm)", min_v)
