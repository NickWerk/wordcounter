from sys import argv
from PyPDF2 import PdfReader
import streamlit as st

def count_words(upload_pdf, first_page, last_page):

    reader = PdfReader(upload_pdf)

    content = ""

    page_number = 1
    for page in reader.pages:
        if page_number >= int(first_page) & page_number <= int(last_page):
            content += page.extract_text()
        page_number += 1

    # Remove multiple spaces and newlines
    content = " ".join(content.split())

    return len(content.split(" "))

st.title("PDF Word Counter")
st.write("Laden Sie eine PDF-Datei hoch, um die Anzahl der Wörter zu zählen.")

uploaded_file = st.file_uploader("Wählen Sie eine PDF-Datei aus", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    total_pages = len(reader.pages)
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
        words = count_words(uploaded_file, first_page, last_page)
        st.write(f"Die Arbeit enthält {words} Wörter.")
