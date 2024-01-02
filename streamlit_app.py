import streamlit as st
import openai

openai.api_type = "azure"
openai.api_base = "https://cog-ps4mawleuhav4.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = "d8280e16a8c44a49bf3b833a73a6cc52"

def generate_image(image_prompt):

    response = openai.Image.create(
        prompt=image_prompt,
        size='1024x1024',
        n=5
    )

    image_urls = [obj.url for obj in response["data"]] 

    return image_urls


if __name__ == "__main__":
    st.title("Image Generator")
    st.write("Provide the prompt of image you want to generate:")
    image_prompt = st.text_input("Image Prompt", "")

    if image_prompt:
        st.write("Generating image...")
        result = generate_image(image_prompt)

        if result:
            st.image(result, width=150, use_column_width=True)