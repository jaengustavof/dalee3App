# Librerías
import streamlit as st
import fire
import os
import openai 
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def call_dalle_model(text_to_image_model, prompt, size, quality):

    client = OpenAI()

    response = client.images.generate(
        model= text_to_image_model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=1,
    )

    return response.data[0].url


# Método principal del script que contiene toda la configuración de la
# aplicación de Streamlit
def main():
    # Escribimos el encabezado en formato Markdown con el signo '#'. También
    # se puede escribir con el método 'st.title()'.
    st.write("# Imágenes para marketplace NFT")

    with st.sidebar:
        text_to_image_model = st.radio(
            "Elige modelo",
            ("Dalle3", "Dalle2")
        )

    model_name_map = {
        "Dalle3": "dall-e-3",
        "Dalle2": "dall-e-2"
    }
    
    prompt = st.text_input(
        label="Prompt",
        value="imagen de un partido vintage de futbol (soccer) para un nft, puedes agregar aspectos historicos, mitologicos y distintas epocas"
    )


    size = st.selectbox(
            "size",
            ("1792x1024", "1024x1792", "1024x1024")
        )

    alta_calidad_bool = st.toggle("Alta calidad")
    if alta_calidad_bool:
        quality = "hd"
    else:
        quality ="standard"

    if st.button("Generar img", type="primary"):
        with st.spinner('Generando imagen..'):
            image_url = call_dalle_model(model_name_map[text_to_image_model], prompt, size, quality)
        st.image(image_url, caption=prompt)


# Control de código
if __name__=="__main__":
    fire.Fire(main)
