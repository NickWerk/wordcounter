import fitz
import streamlit as st

def main():
    count_words()
    streamlit_app_config()

def count_words(pdf_bytes, first_page, last_page):
    reader = fitz.open(stream=pdf_bytes, filetype="pdf")

    content = ""
    for page_number in range(reader.page_count):
        if int(first_page) <= page_number + 1 <= int(last_page):
            page = reader.load_page(page_number)
            content += page.get_text()

    # Clean up whitespace
    content = " ".join(content.split())
    return len(content.split())

def streamlit_app_config():

    st.set_page_config(page_title="PDF Word Counter", layout="wide")
    st.title("PDF Word Counter")
    st.write("Upload a PDF file to count the number of words.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        pdf_bytes = uploaded_file.read()  # Read the file
        reader = fitz.open(stream=pdf_bytes, filetype="pdf")
        total_pages = reader.page_count
        st.write(f"The PDF file has a total of {total_pages} pages.")

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
            st.balloons()

st.title("PDF Word Counter")
st.write("Upload a PDF file to count the number of words.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    pdf_bytes = uploaded_file.read()  # Read the file
    reader = fitz.open(stream=pdf_bytes, filetype="pdf")
    total_pages = reader.page_count
    st.write(f"The PDF file has a total of {total_pages} pages.")

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
        st.balloons()

if __name__ == "__main__":
    main()
