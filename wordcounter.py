import fitz
import streamlit as st

def count_words(pdf_bytes, first_page, last_page):
    reader = fitz.open(stream=pdf_bytes, filetype="pdf")

    content = ""
    for page_number in range(reader.page_count):
    if int(first_page) <= page_number + 1 <= int(last_page):
        page = reader.load_page(page_number)
        content += page.get_text()

    # Clean up whitespac
    content = " ".join(content.split())
    return len(content.split())

st.title("PDF Word Counter")
st.write("Laden Sie eine PDF-Datei hoch, um die Anzahl der Wörter zu zählen.")

uploaded_file = st.file_uploader("Wählen Sie eine PDF-Datei aus", type="pdf")

if uploaded_file is not None:
    pdf_bytes = uploaded_file.read()  # Read the file
    reader = fitz.open(stream=pdf_bytes, filetype="pdf")
    total_pages = reader.page_count
    st.write(f"Die PDF-Datei hat insgesamt {total_pages} Seiten.")

    # Use a range slider to select the page range
    page_range = st.slider(
        "Wählen Sie den Seitenbereich aus",
        min_value=1,
        max_value=total_pages,
        value=(1, total_pages),
    )
    first_page, last_page = page_range

    if st.button("Wörter zählen"):
        words = count_words(pdf_bytes, first_page, last_page)
        st.write(f"Die Arbeit enthält {words} Wörter.")
