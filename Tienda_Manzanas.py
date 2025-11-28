import streamlit as st

# Configuración básica
st.title("🍎 Tienda de Manzanas")
st.title("**** Los PIU PIU ****")

# Tu lógica original preservada
nombre = st.text_input("Por favor ingresa tu nombre")

if nombre:
    st.write("Hola,", nombre + "!")
    st.write("Actualmemte contamos con 20 manzanas disponibles")
    st.write("Cada manzana tiene un valor de 5 pesos,")
    st.write("Cuantas manzanas desea comprar?")
    
    cantidad_manz = st.number_input("Cantidad:", min_value=0, max_value=20, value=0)
    
    if st.button("Calcular"):
        # TODO TU CÓDIGO ORIGINAL AQUÍ
        if cantidad_manz > 0 and cantidad_manz <= 20:
            valor_unidad = 5
            manza_totales = 20
            manzanas_restantes = manza_totales - cantidad_manz
            valor_total = valor_unidad * cantidad_manz
            
            st.write("¡Genial!",":", "usted ha comprado",cantidad_manz,"manzanas, el precio total es de:", valor_total, "pesos,")
            st.write("actualmente nos quedan", manzanas_restantes, "manzanas disponibles.")
            st.write("Gracias por comprar.¡Regresa pronto!")
        else:
            st.error("No contamos con esa cantidad")
            st.info("Ingrese el valor correcto")








 
