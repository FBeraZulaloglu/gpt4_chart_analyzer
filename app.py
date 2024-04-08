import streamlit as st
import base64
import requests
import os

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to interact with OpenAI API
def analyze_image(image_path,api_key):
    base64_image = encode_image(image_path)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What’s in this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()

# Streamlit app
def main():
    st.title('Image Analyzer with GPT-4 Vision')
    api_password = st.sidebar.text_input("Enter Your OpenAI API ", type="password")

    st.write("Upload an image to analyze:")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        if st.button('Analyze'):
            # Save the uploaded file temporarily
            temp_image_path = os.path.join(os.getcwd(), "temp_image.jpg")
            with open(temp_image_path, "wb") as temp_file:
                temp_file.write(uploaded_file.read())

            # Analyze the uploaded image
            response = analyze_image(temp_image_path,api_password)
            st.subheader('Analysis Results:')
            st.write(response)

            # Remove the temporary file
            os.remove(temp_image_path)

if __name__ == '__main__':
    main()
