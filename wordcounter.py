import fitz
import streamlit as st

def main():
    streamlit_app_config()

def count_words(pdf_bytes, first_page, last_page):
    document = fitz.open(stream = pdf_bytes, filetype = "pdf")

    content = ""
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        content += page.get_text()

    # cleanup whitespace
    content = " ".join(content.split())
    return len(content.split())



def streamlit_app_config():
    # Configure the Streamlit app
    st.set_page_config(page_title="PDF Word Counter", layout="wide")
    st.title("PDF Word Counter")
    st.write("This app counts the number of words in a PDF file.")
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        pdf_bytes = uploaded_file.read() # Read the uploaded PDF file
        reader = fitz.open(stream=pdf_bytes, filetype="pdf")
        total_pages = reader.page_count
        
        # Use a range slider to select the page range
        page_range = st.slider(
            "Select the page range",
            min_value=1,
            max_value=total_pages,
            value=(1, total_pages),
        )
        first_page, last_page = page_range

        if st.button("Count Words"):
            words = count_words(pdf_bytes, first_page, last_page)
            st.write(f"The document contains {words} words.")

if __name__ == "__main__":
    main()
