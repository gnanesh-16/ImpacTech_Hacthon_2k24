# from dotenv import load_dotenv
# # load_dotenv() 
# import streamlit as st
# import os
# from PIL import Image
# import google.generativeai as genai
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Load Gemini pro vision model
# model=genai.GenerativeModel('gemini-pro-vision')

# def get_gemini_response(input,image,user_prompt):
#     response=model.generate_content([input,image[0],user_prompt])
#     return response.text

# def input_image_details(uploaded_file):
#     if uploaded_file is not None:
#         # Read the file into bytes
#         bytes_data = uploaded_file.getvalue()

#         image_parts = [
#             {
#                 "mime_type": uploaded_file.type,  
#                 "data": bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         raise FileNotFoundError("No file uploaded")
    

# st.set_page_config(page_title="MULTI LANGUAGE INVOICE Extractorr")

# st.header("MultiLanguage Invoice Extractor")
# input=st.text_input("Input Prompt: ",key="input")
# uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     image=Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image.", use_column_width=True)

# submit=st.button("Tell me about the invoice")

# input_prompt="""
# You are an expert in understanding invoices. We will upload a image as invoice
# and you will have to answer any questions based on the uploaded invoice image 
# and also you can give it in Table formate of invoice Details.
# """

# ## if submit button is clicked

# if submit:
#     image_data=input_image_details(uploaded_file)
#     response=get_gemini_response(input_prompt,image_data,input)
#     st.subheader("The Rresponse is")
#     st.write(response)

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
#################################################################################################################################################################################3METIRCSPAGE_ETCCCC
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import datetime
import pandas as pd

# Load .env variables
load_dotenv()

# Configure Google GenAI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini pro vision model
model = genai.GenerativeModel('gemini-pro-vision')

# Define functions
def get_gemini_response(input, images, user_prompt):
    response = model.generate_content([input, images[0], user_prompt])
    return response.text

def input_image_details(uploaded_files):
    image_parts = []
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            # Read the file into bytes
            bytes_data = uploaded_file.getvalue()
            image_parts.append({
                "mime_type": uploaded_file.type,
                "data": bytes_data
            })
        else:
            raise FileNotFoundError("No file uploaded")
    return image_parts

# Initialize session state for real-time data tracking
if 'invoices_processed' not in st.session_state:
    st.session_state['invoices_processed'] = 0
if 'successful_extractions' not in st.session_state:
    st.session_state['successful_extractions'] = 0
if 'extraction_failures' not in st.session_state:
    st.session_state['extraction_failures'] = 0

# Set Streamlit page config
st.set_page_config(page_title="MULTI LANGUAGE INVOICE Extractor")

# Sidebar for navigation
page = st.sidebar.selectbox("Choose your page", ["Home", "Metrics", "History", "Settings"])

# Home Page
if page == "Home":
    st.header("MultiLanguage Invoice Extractor")
    input_text = st.text_input("Input Prompt:", key="input")
    uploaded_files = st.file_uploader("Choose images of the invoice...", accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image.", use_column_width=True)
    submit = st.button("Tell me about the invoices")

    input_prompt = """
    You are an expert in understanding invoices. We will upload multiple images as invoices
    and you will have to answer any questions based on the uploaded invoice images 
    and also provide the details in a table format.
    """

    if submit:
        image_data = input_image_details(uploaded_files)
        response_text = get_gemini_response(input_prompt, image_data, input_text)
        st.subheader("The Response is:")
        st.write(response_text)

        # Update session state
        st.session_state['invoices_processed'] += len(uploaded_files)
        if response_text:
            st.session_state['successful_extractions'] += 1
        else:
            st.session_state['extraction_failures'] += 1

        # Download button for the response text
        if response_text:
            with open("invoice_response.txt", "w") as file:
                file.write(response_text)
            st.download_button(label="Download Response", data=response_text, file_name="invoice_response.txt", mime="text/plain")

# Metrics Page
elif page == "Metrics":
    st.title("Invoice Processing Metrics")

    accuracy_rate = ((st.session_state['successful_extractions'] / max(1, st.session_state['invoices_processed'])) * 100)

    metrics = {
        "Total Invoices Processed": st.session_state['invoices_processed'],
        "Successful Extractions": st.session_state['successful_extractions'],
        "Extraction Failures": st.session_state['extraction_failures'],
        "Accuracy Rate": f"{accuracy_rate:.2f}%"
    }

    for metric, value in metrics.items():
        st.metric(label=metric, value=value)

    st.text(f"Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# History Page
elif page == "History":
    st.title("Processed Invoices History")
    if 'invoice_history' not in st.session_state:
        st.session_state['invoice_history'] = pd.DataFrame(columns=['Timestamp', 'Invoice Details'])
    st.table(st.session_state['invoice_history'])

# Settings Page
elif page == "Settings":
    st.title("API Settings")
    api_key = st.text_input("Enter your Google API Key:", type="password")
    save_api_key = st.button("Save API Key")
    if save_api_key and api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
        st.success("API Key Updated Successfully")

def get_gemini_response(input_text, images, user_prompt):
    try:
        # Assuming the API expects a dictionary with 'input', 'images', and 'user_prompt' keys
        # Note: This is a hypothetical structure; please adjust according to the actual API requirements
        input_data = {
            "input": input_text,
            "images": images,  # Ensure images is a list of dictionaries with the correct structure
            "user_prompt": user_prompt
        }
        response = model.generate_content(input_data)
        return response.text
    except Exception as e:
        print(f"Error during generating content: {e}")
        return None

##############################################################################################################################################################################



