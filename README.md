# Image Analyzer with GPT-4 Vision

This Streamlit application allows users to upload images for analysis using OpenAI's GPT-4 Vision API. The app processes uploaded images and generates analysis results based on the content detected in the images.

## Features

- **Image Upload:** Users can upload JPG, JPEG, or PNG images for analysis.
- **API Integration:** Utilizes OpenAI's GPT-4 Vision API for image analysis.
- **Secure API Key Input:** Users can securely input their OpenAI API key using a password input field in the sidebar.

## Setup

1. Install the required libraries:
   ```
   pip install streamlit requests
   ```

2. Obtain an OpenAI API key:
   - Sign up or log in to your OpenAI account.
   - Navigate to the API section and generate an API key.

3. Clone the repository and navigate to the project directory:
   ```
   git clone https://github.com/your-repo/image-analyzer.git
   cd image-analyzer
   ```

4. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

5. Install additional dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

7. Access the app in your browser at `http://localhost:8501`.

## Usage

1. Upon running the app, you will see a sidebar prompting you to enter your OpenAI API key.
2. Upload an image by clicking on the "Choose an image..." button and selecting a compatible image file (JPG, JPEG, or PNG).
3. Once the image is uploaded, click the "Analyze" button to initiate the analysis process.
4. The app will display the uploaded image and provide analysis results based on the image content detected by the GPT-4 Vision API.
5. The temporary image file used for analysis will be removed automatically after processing.

## Important Note

- **API Key Security:** Ensure that you keep your OpenAI API key secure and do not share it publicly. Use the password input field provided by the app to enter your API key securely.
