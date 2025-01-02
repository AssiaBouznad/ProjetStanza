#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install stanza


# In[4]:


pip install corenlp


# In[5]:


pip install stanfordnlp


# In[11]:


pip install stanfordcorenlp


# In[9]:


import stanza
#>>> stanza.download('fr') 
nlp = stanza.Pipeline('fr')
doc = nlp("Barack Obama est né à Hawaii.") 


# In[10]:


print(doc)


# In[11]:


# Téléchargez le modèle espagnol
# stanza.download('es')

# nitialise le pipeline
nlp = stanza.Pipeline('es')

folder_path = "corpusEs"


for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r') as file:
            text = file.read()

        # Annoter
        doc2 = nlp(text)

        # Parcourir les phrases et les mots
        for sentence in doc2.sentences:
            for word in sentence.words:
                print(f'Parablas: {word.text}, POS: {word.pos}, Dependency Relation: {word.deprel}')


# In[12]:


print(doc2)


# # Corpus Français

# In[4]:


import stanza
import os
from stanza.models.common.doc import Document


# In[5]:


def lire_fichier(folder_path):     
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, 'r') as file:
                text = file.read()
    return text


def annot_NLP (text): 
    doc = nlp(text)
    for phrase in doc.phrases:
            for mot in phrase.mots:
                txt_annot = f'mot: {mot.text}, POS: {mot.pos}, Dependency Relation: {mot.deprel}'


# In[11]:


chemin = "corpusFr"
nlp = stanza.Pipeline('fr')
text = lire_fichier(chemin)

doc = nlp(text)
print(doc)


# In[ ]:




