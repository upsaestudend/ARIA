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
    elif figura == "rombo":
        D = valores["diagonal_mayor"]
        d = valores["diagonal_menor"]
        return (D * d) / 2
    elif figura == "trapecio":
        B = valores["base_mayor"]
        b = valores["base_menor"]
        h = valores["altura"]
        return ((B + b) * h) / 2
    elif figura == "pentagono":
        lado = valores["lado"]
        return (5 * lado ** 2) / (4 * math.tan(math.pi / 5))
    elif figura == "hexagono":
        lado = valores["lado"]
        return (3 * math.sqrt(3) * lado ** 2) / 2
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
    elif figura == "rombo":
        lado = valores["lado"]
        return 4 * lado
    elif figura == "trapecio":
        return valores["lado1"] + valores["lado2"] + valores["base_mayor"] + valores["base_menor"]
    elif figura == "pentagono":
        lado = valores["lado"]
        return 5 * lado
    elif figura == "hexagono":
        lado = valores["lado"]
        return 6 * lado
    else:
        raise ValueError("Figura no válida")

def main():
    # Título e imagen superior
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Calculadora de área y perímetro de figuras geométricas")
    with col2:
        st.image("imagen5.png", width=120)

    # Menú lateral
    st.sidebar.header("Selección de figura")
    figura_opciones = {
        "Cuadrado": "cuadrado",
        "Triángulo": "triangulo",
        "Rectángulo": "rectangulo",
        "Círculo": "circulo",
        "Rombo": "rombo",
        "Trapecio": "trapecio",
        "Pentágono regular": "pentagono",
        "Hexágono regular": "hexagono"
    }

    eleccion = st.sidebar.selectbox("Elige la figura", list(figura_opciones.keys()))
    figura = figura_opciones[eleccion]

    st.sidebar.markdown("---")
    st.sidebar.write("Ajusta las dimensiones en la sección principal.")

    valores = {}

    # Entradas según figura
    if figura == "cuadrado":
        valores["lado"] = st.number_input("Lado del cuadrado (cm)", min_value=0.0, value=5.0, step=0.1)

    elif figura == "triangulo":
        valores["base"] = st.number_input("Base del triángulo (cm)", min_value=0.0, value=5.0, step=0.1)
        valores["altura"] = st.number_input("Altura (cm)", min_value=0.0, value=4.0, step=0.1)
        st.caption("Nota: se asume triángulo equilátero para el perímetro.")

    elif figura == "rectangulo":
        valores["base"] = st.number_input("Base del rectángulo (cm)", min_value=0.0, value=6.0, step=0.1)
        valores["altura"] = st.number_input("Altura (cm)", min_value=0.0, value=3.0, step=0.1)

    elif figura == "circulo":
        valores["radio"] = st.number_input("Radio del círculo (cm)", min_value=0.0, value=3.0, step=0.1)

    elif figura == "rombo":
        valores["diagonal_mayor"] = st.number_input("Diagonal mayor (cm)", min_value=0.0, value=6.0, step=0.1)
        valores["diagonal_menor"] = st.number_input("Diagonal menor (cm)", min_value=0.0, value=4.0, step=0.1)
        valores["lado"] = st.number_input("Lado del rombo (cm)", min_value=0.0, value=5.0, step=0.1)

    elif figura == "trapecio":
        valores["base_mayor"] = st.number_input("Base mayor (cm)", min_value=0.0, value=8.0, step=0.1)
        valores["base_menor"] = st.number_input("Base menor (cm)", min_value=0.0, value=4.0, step=0.1)
        valores["altura"] = st.number_input("Altura (cm)", min_value=0.0, value=3.0, step=0.1)
        valores["lado1"] = st.number_input("Lado no paralelo 1 (cm)", min_value=0.0, value=3.0, step=0.1)
        valores["lado2"] = st.number_input("Lado no paralelo 2 (cm)", min_value=0.0, value=3.0, step=0.1)

    elif figura == "pentagono":
        valores["lado"] = st.number_input("Lado del pentágono (cm)", min_value=0.0, value=4.0, step=0.1)

    elif figura == "hexagono":
        valores["lado"] = st.number_input("Lado del hexágono (cm)", min_value=0.0, value=4.0, step=0.1)

    # Cálculo y resultados
    st.markdown("---")
    if st.button("Calcular"):
        try:
            area = calcular_area(figura, valores)
            perimetro = calcular_perimetro(figura, valores)

            st.success(f"**Área:** {area:.2f} cm²")
            st.success(f"**Perímetro:** {perimetro:.2f} cm")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

    # Imagen inferior decorativa
    st.markdown("---")
    st.image("imagen6.png", caption="Representación gráfica", use_column_width=True)

if __name__ == "__main__":
    main()