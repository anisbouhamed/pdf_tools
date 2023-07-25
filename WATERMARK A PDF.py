#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pypdf


# In[5]:


pip install PyPDF2


# In[15]:


from pypdf import PdfWriter, PdfReader
def split_pdf_pages(input_pdf_path,watermark_path):
    stamp = PdfReader(watermark_path).pages[0]
    writer = PdfWriter(clone_from=input_pdf_path)
    for page in writer.pages:
        page.merge_page(stamp, over=False)  # here set to False for watermarking
    writer.write("Watermarked.pdf")

