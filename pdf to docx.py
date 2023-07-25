#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pdf2docx


# In[ ]:


# Importing the Converter() class
from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file, docx_file):
    # Converting PDF to Docx
    cv_obj = Converter(pdf_file)
    cv_obj.convert(docx_file)
    cv_obj.close()

