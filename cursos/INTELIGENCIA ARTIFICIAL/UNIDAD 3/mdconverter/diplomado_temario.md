

# ===== Curso 1_ Inteligencia Artificial I/Material Clase 10 (Francisca Cattan)-20251123/Laboratorio Practico/Clase 10 - Practico optimizacion.ipynb =====
# Diplomado IA
## Parte 2: Aprendizaje Profundo II
## Clase 10: Optimización y Learning Rate
## Agenda
# Actividad 1 - Gradient Descent
    [código] import numpy as np | import matplotlib.pyplot as plt
## Gráficos de las ecuación
## Gradient Descent
## Ecuación que queremos aproximar
## Función de pérdida
## Gradiente
## Métricas
## Función Lineal
## Función Cuadrática
    [código] from sklearn.tree import DecisionTreeRegressor
    [código] from sklearn.neural_network import MLPRegressor | from sklearn.preprocessing import StandardScaler | import matplotlib.pyplot as plt | import numpy as np
# Actividad 2 - Stochastic Gradient Descent
### Datos
    [código] import torch | import torchvision | import torchvision.transforms as transforms
    [código] import matplotlib.pyplot as plt | import numpy as np
## Modelo
    [código] import torch.nn as nn | import torch.nn.functional as F
    [código] import numpy as np
## Actividad Practica 1
## Ajuste de los Hiper-Parámetros
###   Learning Rate
    [código] import torch.optim as optim | import matplotlib.pyplot as plt
### Actividad Práctica 2
    [código] import torch.optim as optim | import matplotlib.pyplot as plt
###   Momentum
    [código] import torch.optim as optim | import matplotlib.pyplot as plt
###   Nesterov
    [código] import torch.optim as optim | import matplotlib.pyplot as plt
#Actividad 3 - Métodos de gradiente adaptativos
    [código] import torch.optim as optim | import matplotlib.pyplot as plt
## Actividad Práctica 3
## Actividad 4 - Ajuste del Learning Rate durante entrenamiento
## Cantidad de épocas
    [código] import torch.optim as optim | import matplotlib.pyplot as plt
## Valor función de pérdida
    [código] import torch.optim as optim | import matplotlib.pyplot as plt


# ===== Curso 1_ Inteligencia Artificial I/Material Clase 10 (Francisca Cattan)-20251123/Laboratorio Practico/Demostraciones teoricas.ipynb =====
# Visualización de gradiente
    [código] import tensorflow as tf | import numpy as np | import matplotlib.pyplot as plt | from mpl_toolkits.mplot3d import Axes3D
# Efecto del batch size


# ===== Curso 1_ Inteligencia Artificial I/Material Clase 12_ (Felipe Del Río)/Laboratorio/Laboratorio 12 - Data Augmentation, Transferencia de conocimiento y Finetuning.ipynb =====
# **Diplomado IA: Inteligencia Artificial I - Parte 2**. <br> Laboratorio 12: Data Augmentation, Transferencia de conocimiento y Finetuning
# **Instrucciones Generales**
# **Agenda**
# Actividad I: Imágenes
## Preámbulo
    [código] import os
    [código] import random | import numpy as np | import torch
## Primeros Pasos
### Dataset
    [código] from torchvision.datasets import ImageFolder
### Entrenamos un Modelo Base
    [código] import torch.nn as nn
    [código] from torch.utils.data import DataLoader
    [código] from torchvision import transforms
    [código] import torchvision.models as models
    [código] import matplotlib.pyplot as plt | import matplotlib.ticker as ticker | from PIL import Image
    [código] from torch.optim import Adam
## Aumentación de Datos
### Reflexiones
### Recortes
### Rotaciones
### Transformaciones Afín
### Composición de transformaciones
### Transformaciones custom
    [código] from torch.nn import Module
    [código] from PIL import Image
### **Ejercicio I**
## Transfer Learning y Finetuning
### Finetuning
### **Ejercicio II (Parte 1)**
### **Ejercicio II (Parte 2)**
# Actividad II: Texto
## Preámbulo
    [código] import os
    [código] import warnings | import random | import numpy as np | import torch
    [código] import transformers | from transformers import BertTokenizer, BertModel
## Primeros Pasos
### Dataset
    [código] import textwrap
    [código] from torch.utils.data import Dataset, DataLoader
## Modelo Base
    [código] import math | import matplotlib.pyplot as plt | import matplotlib.ticker as ticker | import sklearn.metrics
    [código] from transformers import PretrainedConfig
    [código] from torch.optim import Adam | from torch.nn import BCEWithLogitsLoss
## Finetuning
## **Ejercicio III**
#### Preguntas
# Anexo: Ejemplo de código
## ¿Cómo entrenar algunas capas del modelo?


# ===== Curso 1_ Inteligencia Artificial I/Material Clase 13 (Gabriel Sepúlveda)-20260108/Laboratorio/Practico_clase_13_parte_1.ipynb =====
# **Diplomado IA: Inteligencia Artificial I - Parte 1**. <br> Práctico 13.1: Seq2Seq y Mecanismos de Atención
# **Instrucciones Generales**
# Import Base Dependencies
    [código] from collections import defaultdict | import matplotlib.pyplot as plt | from tqdm.notebook import tqdm, trange | from tqdm import tqdm, trange
    [código] import torch | import torch.nn as nn | import torch.nn.functional as F | from torch.utils.data import Dataset, DataLoader
# General Utilities
# Sequence to sequence (seq2seq): Translation
## Encoder
## Decoder
## Data
### Download dataset
    [código] import requests
### Load data
## Train Utils
## Full Model


# ===== Curso 1_ Inteligencia Artificial I/Material Clase 13 (Gabriel Sepúlveda)-20260108/Laboratorio/Practico_clase_13_parte_2.ipynb =====
# **Diplomado IA: Inteligencia Artificial I - Parte 1**. <br> Práctico 13.2: Seq2Seq y Mecanismos de Atención
# **Instrucciones Generales**
# Import Base Dependencies
    [código] from collections import defaultdict | import matplotlib.pyplot as plt | from tqdm.notebook import tqdm, trange | from tqdm import tqdm, trange
    [código] import torch | import torch.nn as nn | import torch.nn.functional as F | from torch.utils.data.dataset import Dataset
# General Utilities
# Sequence to sequence (seq2seq) with attention
## Encoder
## Decoder
### Attention:
### Attention Module
## Decoder Module
## Data
### Download dataset
    [código] import requests
### Load data
## Train Utils
## Full Model
## Visualize attentions
### Hidden code for visualization
### Run trained model and save attentions
## Visualize attentions
    [código] import seaborn as sns


# ===== Curso 1_ Inteligencia Artificial I/Material Clase 13 (Gabriel Sepúlveda)-20260108/Laboratorio/Practico_clase_13_parte_3.ipynb =====
# **Diplomado IA: Inteligencia Artificial I - Parte 1**. <br> Práctico 13.3: Seq2Seq y Mecanismos de Atención
# **Instrucciones Generales**
# Import Base Dependencies
    [código] from collections import defaultdict | import matplotlib.pyplot as plt | from tqdm.notebook import tqdm, trange | from tqdm import tqdm, trange
    [código] import torch | import torch.nn as nn | import torch.nn.functional as F | from torch.utils.data import Dataset, DataLoader
# General Utilities
# Sequence to sequence (seq2seq): Translation
## Encoder
## Decoder
### <b><u>TEACHER FORCING</u></b>
## Data
### Download dataset
    [código] import requests
### Load data
## Train Utils
## Full Model
## Actividad
### Actividad 1.1
### Actividad 1.2


# ===== Curso 1_ Inteligencia Artificial I/Material Clase 14 Transformer (Felipe Del Río)-20260108/Laboratorio/Laboratorio_14_Transformers_Parte_1.ipynb =====
# **Diplomado IA: Inteligencia Artificial II - Parte 1**. <br> Laboratorio 14: Transformers
# **Instrucciones Generales**
# **Agenda**
# Parte I: Inspeccionando las atenciones de un Transformer
## Preámbulo
    [código] import string | import IPython | from bertviz import head_view, model_view | from bertviz.neuron_view import show
## Representación del Input para BERT
## NER
    [código] from spacy import displacy
## Visualización de Atenciones
### Head View
### Model View
### Neuron View
    [código] from bertviz.transformers_neuron_view import BertModel as VizBertModel, BertTokenizer as VizBertTokenizer | from bertviz.neuron_view import show
### Actividad 1
## Actividad 2: Atenciones en el Decoder
## Traducción


# ===== Curso 1_ Inteligencia Artificial I/Material Clase 14 Transformer (Felipe Del Río)-20260108/Laboratorio/Laboratorio_14_Transformers_Parte_2.ipynb =====
# **Diplomado IA: Inteligencia Artificial II - Parte 1**. <br> Laboratorio 14: Transformers
# **Instrucciones Generales**
# **Agenda**
# Parte III: Inspeccionando a CLIP
## Preámbulo
    [código] import os | import skimage | import random | import IPython.display
## Cargamos el Modelo
    [código] import clip
# Classificación zero-shot utilizando CLIP
## Dataset Food101
    [código] from torchvision.datasets import Food101
### *Queries* para Predicción
### Visualización de Predicciones
### Rendimiento del Modelo
    [código] from tqdm.auto import tqdm | from torch.utils.data import DataLoader
### Actividad 3
## Dataset Stanford Cars
    [código] from torchvision.datasets import StanfordCars
### Visualización de Predicciones
### Rendimiento en Test
    [código] from torch.utils.data import DataLoader
    [código] from tqdm.auto import tqdm
### Actividad 4
    [código] from google.colab import files
    [código] from PIL import Image


# ===== Curso 2_ Aplicaciones de inteligencia artificial I/Clase 16_ Introducción a NLP (Carlos Aspillaga)/Laboratorio Práctico/Lab16.ipynb =====
# **Diplomado IA: Aplicaciones 1 - NLP**. <br> Práctico 16: Introducción a NLP
# **Instrucciones Generales**
# **Índice**
# **Herramientas para manejo de texto**
## **Uso de NLTK**
    [código] import scipy | import nltk | from nltk.book import *
    [código] import matplotlib.pyplot as plt
    [código] from nltk.tokenize import sent_tokenize, TweetTokenizer
    [código] from nltk.corpus import stopwords
    [código] from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
## **Uso de spaCy**
    [código] import spacy | from spacy import displacy
    [código] import spacy | from spacy import displacy
    [código] import spacy | from spacy.lang.en import English
    [código] from spacy.lang.es import Spanish
## **Actividades**
    [código] import re | import nltk | from nltk.tokenize import sent_tokenize, TweetTokenizer
    [código] import re | import nltk | from nltk.tokenize import sent_tokenize | import spacy
# **Traducción automática usando NLLB-200**
## **Uso básico**
    [código] from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline | import torch
# **Análisis de sentimientos usando VADER**
## **Uso básico**
    [código] from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
## **Actividad**
# **Bag of Words / Bag of N-grams**
    [código] import pandas as pd | import re | import nltk | import numpy as np
## Actividades


# ===== Curso 2_ Aplicaciones de inteligencia artificial I/Clase 18_ Modelos de lenguaje, Word2Vec, GloVe y SkipThought (Pablo Messina)_/Laboratorio Práctico/Practico18.ipynb =====
# **Diplomado IA: Aplicaciones 1 - NLP**. <br> Práctico 2: Word Embeddings
# **Instrucciones Generales**
# **Importamos librerías a usar**
    [código] import re | import gdown | import random | import matplotlib.pyplot as plt
# **Descargamos Word2vec pre-entrenado**
# **Analogías con Word2vec**
## (Álgebra de vectores con interpretación semántica)
# **Word vectors en términos excluídos**
# **Visualizando Word Embeddings**
# **Análisis de Sentimiento de Tweets usando Word embeddings**
## **Generando Tweet Vectors a partir de Word Embeddings**
#### 1) Entrenamos y evaluamos un MLP con 1 capa oculta y usando **suma** de word embeddings como entrada
#### 2) Entrenamos y evaluamos un MLP con 1 capa oculta y usando **promedio** de word embeddings como entrada


# ===== Curso 2_ Aplicaciones de inteligencia artificial I/Clase 20_ ELMo, BERT, GPT, ChatGPT (Carlos Aspillaga) _/Laboratorio Práctico/Clase_20_material_complementario_opcional.ipynb =====
# **Diplomado en Inteligencia Artificial**. <br> Material complementario opcional al práctico 20: BERT y GPT
# **ChatGPT**
    [código] from openai import OpenAI
    [código] import textwrap as tr
## TIP: Usar delimitadores para evitar prompt-injection
## TIP: solicitar al modelo verificar prompts inadecuados
##TIP: solicitar output estructurado (json, html, etc)
    [código] from IPython.display import display, HTML
    [código] import json
## TIP: few-shot prompting
## TIP: Traducir idioma o formato
## TIP: Corregir texto
    [código] from redlines import Redlines | from IPython.display import display, HTML
## TIP: Personalización
## TIP: Chain of Thought


# ===== Curso 2_ Aplicaciones de inteligencia artificial I/Clase 20_ ELMo, BERT, GPT, ChatGPT (Carlos Aspillaga) _/Laboratorio Práctico/Practico_20__BERT_y_GPT.ipynb =====
# **Diplomado IA: Aplicaciones 1 - NLP**. <br> Práctico 20: Modelos de lenguaje (ElMo, BERT, GPT2, ChatGPT)
# **Instrucciones Generales**
# **Índice**
# **Librería "Transformers", de Huggingface**
## Instalación de dependencias
## Uso básico de la librería
    [código] from transformers import XLNetTokenizer, XLNetModel | import torch
    [código] from transformers import XLNetTokenizer, XLNetForQuestionAnswering | import torch
    [código] from transformers import XLNetTokenizer, XLNetForMultipleChoice | import torch
##Actividad
# Actividad
# **BERT**
##Finetuning de BERT para detectar Fake News
    [código] import pandas as pd | from sklearn.model_selection import train_test_split | import matplotlib.pyplot as plt | import torch
    [código] from torch.utils.data import DataLoader, Dataset
# **GPT-2**
## GPT-2: Generación de texto
    [código] from transformers import GPT2LMHeadModel, GPT2Tokenizer
## Actividades
# **Actividad Final**