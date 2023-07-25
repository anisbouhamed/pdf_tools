#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install ocrmypdf


# In[2]:


pip install tesseract


# In[3]:


pip install -U Pillow


# In[4]:


from PIL import Image
import ocrmypdf
def ocr(file_path, save_path):
    ocrmypdf.ocr(file_path, save_path, rotate_pages=True,language="eng", deskew=True, force_ocr=True)


# In[7]:


ocr("C:/Users/anisb/Downloads/scanned pdf example.pdf","C:/Users/anisb/OneDrive/Desktop/test/12345678.pdf")


# In[ ]:




