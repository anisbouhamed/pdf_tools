#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pypdf


# In[ ]:


#PDF_List is a list of pdf paths
def convert_pdf_to_docx(PDF_List):
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("result.pdf")
    merger.close()

