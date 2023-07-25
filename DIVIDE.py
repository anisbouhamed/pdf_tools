#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install PyPDF2


# In[26]:


from PyPDF2 import PdfWriter, PdfReader

def split_pdf_pages(input_pdf_path, split_page_numbers_List):
    part=0
    split_page_numbers_List = [x - 1 for x in split_page_numbers_List]
    inputpdf = PdfReader(open(input_pdf_path, "rb"))
    output = PdfWriter()
    for i in range(len(inputpdf.pages)):
        output.add_page(inputpdf.pages[i])
        if ((i in split_page_numbers_List) or ((i==len(inputpdf.pages)-1))):
            part = part+1
            output_file_path = "C:/Users/anisb/OneDrive/Desktop/test/"+str(part)+".pdf"
            with open(output_file_path, "wb") as outputStream:
                output.write(outputStream)
            output = PdfWriter()

