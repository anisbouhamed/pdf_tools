#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install PyPDF2


# In[ ]:


import PyPDF2

def scale_pdf_page(input_pdf_path, output_pdf_path, scale_factor):
    pdf = PyPDF2.PdfReader(input_pdf_path)
    page0 = pdf.pages[0]
    page0.scale_by(scale_factor)  # float representing scale factor - this happens in-place
    writer = PyPDF2.PdfWriter()  # create a writer to save the updated results
    writer.add_page(page0)
    with open(output_pdf_path, "wb+") as f:
        writer.write(f)

