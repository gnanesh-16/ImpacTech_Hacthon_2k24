from dotenv import load_dotenv
# load_dotenv() 
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Load Gemini pro vision model
model=genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image,user_prompt):
    response=model.generate_content([input,image[0],user_prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

st.set_page_config(page_title="MULTI LANGUAGE INVOICE Extractorr")

st.header("MultiLanguage Invoice Extractor")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the invoice")

input_prompt="""
You are an expert in understanding invoices. We will upload a image as invoice
and you will have to answer any questions based on the uploaded invoice image 
and also you can give it in Table formate of invoice Details.
"""

## if submit button is clicked

if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Rresponse is")
    st.write(response)

##############################################################################################################################


# from dotenv import load_dotenv
# # load_dotenv() 
# import streamlit as st
# import os
# from PIL import Image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Load Gemini pro vision model
# model = genai.GenerativeModel('gemini-pro-vision')

# def get_gemini_response(input, images, user_prompt):
#     response = model.generate_content([input, images[0], user_prompt])
#     return response.text

# def input_image_details(uploaded_files):
#     image_parts = []
#     for uploaded_file in uploaded_files:
#         if uploaded_file is not None:
#             # Read the file into bytes
#             bytes_data = uploaded_file.getvalue()

#             image_parts.append({
#                 "mime_type": uploaded_file.type,
#                 "data": bytes_data
#             })
#         else:
#             raise FileNotFoundError("No file uploaded")
    
#     return image_parts

# st.set_page_config(page_title="MULTI LANGUAGE INVOICE Extractor")

# st.header("MultiLanguage Invoice Extractor")
# input_text = st.text_input("Input Prompt:", key="input")
# uploaded_files = st.file_uploader("Choose images of the invoice...", accept_multiple_files=True)

# if uploaded_files is not None:
#     for uploaded_file in uploaded_files:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image.", use_column_width=True)

# submit = st.button("Tell me about the invoices")

# input_prompt = """
# You are an expert in understanding invoices. We will upload multiple images as invoices
# and you will have to answer any questions based on the uploaded invoice images 
# and also provide the details in a table format.
# """

# ## if submit button is clicked

# if submit:
#     image_data = input_image_details(uploaded_files)
#     response = get_gemini_response(input_prompt, image_data, input_text)
#     st.subheader("The Response is:")
#     st.write(response)


#############MAIN########MAIN###############MAIN################MAIN#########MAIN############MAIN#################################################################
# from dotenv import load_dotenv
# # load_dotenv() 
# import streamlit as st
# import os
# from PIL import Image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Load Gemini pro vision model
# model = genai.GenerativeModel('gemini-pro-vision')

# def get_gemini_response(input, images, user_prompt):
#     response = model.generate_content([input, images[0], user_prompt])
#     return response.text

# def input_image_details(uploaded_files):
#     image_parts = []
#     for uploaded_file in uploaded_files:
#         if uploaded_file is not None:
#             # Read the file into bytes
#             bytes_data = uploaded_file.getvalue()

#             image_parts.append({
#                 "mime_type": uploaded_file.type,
#                 "data": bytes_data
#             })
#         else:
#             raise FileNotFoundError("No file uploaded")
    
#     return image_parts

# st.set_page_config(page_title="MULTI LANGUAGE INVOICE Extractor")

# st.header("MultiLanguage Invoice Extractor")
# input_text = st.text_input("Input Prompt:", key="input")
# uploaded_files = st.file_uploader("Choose images of the invoice...", accept_multiple_files=True)

# if uploaded_files is not None:
#     for uploaded_file in uploaded_files:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image.", use_column_width=True)

# submit = st.button("Tell me about the invoices")

# input_prompt = """
# You are an expert in understanding invoices. We will upload multiple images as invoices
# and you will have to answer any questions based on the uploaded invoice images 
# and also provide the details in a table format.
# """

# ## if submit button is clicked

# if submit:
#     image_data = input_image_details(uploaded_files)
#     response_text = get_gemini_response(input_prompt, image_data, input_text)
#     st.subheader("The Response is:")
#     st.write(response_text)

#     # Add a download button for the response text
#     if response_text:
#         with open("invoice_response.txt", "w") as file:
#             file.write(response_text)
#         st.download_button(label="Download Response", data=response_text, file_name="invoice_response.txt", mime="text/plain")

############################################################################################################################################
# from dotenv import load_dotenv
# load_dotenv() 
# import streamlit as st
# import os
# from PIL import Image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Load Gemini pro vision model
# model = genai.GenerativeModel('gemini-pro-vision')

# def get_gemini_response(input, images, user_prompt):
#     response = model.generate_content([input, images, user_prompt])
#     return response.text

# def input_image_details(uploaded_files):
#     image_parts = []
#     for uploaded_file in uploaded_files:
#         if uploaded_file is not None:
#             # Read the file into bytes
#             bytes_data = uploaded_file.getvalue()

#             image_parts.append({
#                 "mime_type": uploaded_file.type,
#                 "data": bytes_data
#             })
#         else:
#             raise FileNotFoundError("No file uploaded")
    
#     return image_parts

# st.set_page_config(page_title="MULTI LANGUAGE INVOICE Extractor")

# st.header("MultiLanguage Invoice Extractor")
# input_text = st.text_input("Input Prompt:", key="input")
# uploaded_files = st.file_uploader("Choose images of the invoice...", accept_multiple_files=True)

# if uploaded_files is not None:
#     images = []
#     for uploaded_file in uploaded_files:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image.", use_column_width=True)
#         images.append({
#             "mime_type": uploaded_file.type,
#             "data": uploaded_file.getvalue()
#         })

# submit = st.button("Tell me about the invoices")

# input_prompt = """
# You are an expert in understanding invoices. We will upload multiple images as invoices
# and you will have to answer any questions based on the uploaded invoice images 
# and also provide the details in a table format.
# """

# ## if submit button is clicked

# if submit:
#     response = get_gemini_response(input_prompt, images, input_text)
#     st.subheader("The Response is:")
#     st.write(response)


