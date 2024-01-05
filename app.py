# import streamlit as st
# import openai
# from azure.storage.blob import BlobServiceClient
# import requests

# openai.api_type = "azure"
# openai.api_base = "https://cog-ps4mawleuhav4.openai.azure.com/"
# openai.api_version = "2023-06-01-preview"
# openai.api_key = "d8280e16a8c44a49bf3b833a73a6cc52"
# azure_connection_string = "DefaultEndpointsProtocol=https;AccountName=sitecoredemoblobstorage;AccountKey=NV6YxWWitdhtSm0rzzX6xrTux/RmtgxWIY+Psobwz4vJM3GBMg+2KgLi7C6XUHtiuWFa3LfhoSID+AStZEFo2g==;EndpointSuffix=core.windows.net"

# def generate_image(image_prompt):

#     response = openai.Image.create(
#         prompt=image_prompt,
#         size='1024x1024',
#         n=1
#     )

#     image_urls = [obj.url for obj in response["data"]] 

#     return image_urls

# def upload_to_blob_storage(image_url, container_name, blob_name):
#     blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)
#     response = requests.get(image_url, stream=True)
#     blob_client = blob_service_client.get_blob_client(container_name, blob_name)
#     blob_client.upload_blob(response.raw, overwrite=True)

# if __name__ == "__main__":
#     st.title("Image Generator")
#     st.write("Provide the prompt of image you want to generate:")
#     image_prompt = st.text_input("Image Prompt", "")

#     if image_prompt:
#         st.write("Generating image...")
#         result = generate_image(image_prompt)[0]

#         if result:
#             blob_name = f"generated_image.png"
#             upload_to_blob_storage(result, "testcontainer", blob_name)
#             st.image(result, width=600, caption=f"Image")

import streamlit as st
import openai
from azure.storage.blob import BlobServiceClient
import requests

openai.api_type = "azure"
openai.api_base = "https://cog-rob2nleooqzme.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = "d8280e16a8c44a49bf3b833a73a6cc52"
azure_connection_string = "DefaultEndpointsProtocol=https;AccountName=sitecoredemoblobstorage;AccountKey=NV6YxWWitdhtSm0rzzX6xrTux/RmtgxWIY+Psobwz4vJM3GBMg+2KgLi7C6XUHtiuWFa3LfhoSID+AStZEFo2g==;EndpointSuffix=core.windows.net"

def generate_image(image_prompt):

    response = openai.Image.create(
        prompt=image_prompt,
        size='1024x1024',
        n=1
    )

    image_urls = [obj.url for obj in response["data"]] 

    return image_urls

def upload_to_blob_storage(image_url, container_name, blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)
    response = requests.get(image_url, stream=True)
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)
    blob_client.upload_blob(response.raw, overwrite=True)

def summarize_text(text):
    response = openai.Completion.create(
        engine="chat",        
        prompt=text,
        temperature=1.0,
        max_tokens=2000
    )
    return response.choices[0].text.strip()

def upload_text_to_blob_storage(text, container_name, blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)
    blob_client.upload_blob(text.encode(), overwrite=True)


if __name__ == "_main_":
    st.title("Image Generator")
    st.write("Provide the prompt of image you want to generate:")
    image_prompt = st.text_input("Image Prompt", "")

    if image_prompt:
        st.write("Generating image...")
        result = generate_image(image_prompt)[0]

        if result:
            blob_name = f"generated_image.png"
            upload_to_blob_storage(result, "testcontainer", blob_name)
            st.image(result, width=600, caption=f"Image")

    summary_prompt = st.text_input("Summary Prompt", "")
    if summary_prompt:
            st.write("Summarizing text...")
            summary = summarize_text(summary_prompt)
            blob_name = "summary.txt"
            upload_text_to_blob_storage(summary, "testcontainer", blob_name)
            st.write("Summary uploaded to blob storage.")