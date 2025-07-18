# -*- coding: utf-8 -*-
"""Multi_4_AgenttesInteligentes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16PG3vvmK3S-dDtcDFI0ngYIFd5EKDgcD
"""

!pip uninstall -y peft accelerate
!pip uninstall -y openai langchain langsmith langchain-openai langchain-core langchain-community

#Desinstalar paquetes que causan conflicto
!pip uninstall -y torch torchvision torchaudio diffusers transformers
#Solo usar este codigo si hay un problema en las importaciones de abajo

!pip uninstall -y numpy
#Desinstala numpy

#instala version correcta
!pip install -q numpy==1.26.4

#Instalar versiones compatibles
!pip install -q \
  torch==2.2.1 \
  diffusers==0.25.0 \
  transformers==4.38.2 \
  huggingface_hub==0.20.3 \
  safetensors==0.4.2

!pip install -q \
  openai==0.27.8 \
  langchain==0.0.310 \
  langsmith==0.0.92

#Verificar que todo esté bien
import numpy as np #arrays
import torch # deep learning  Definir y entrenar redes neuronales
import diffusers #Generar imágenes desde texto
import transformers #Traducción automática lenguajes GPT
import openai #modelos de OpenAI

print("✅ numpy:", np.__version__)
print("✅ torch:", torch.__version__)
print("✅ diffusers:", diffusers.__version__)
print("✅ transformers:", transformers.__version__)
print("✅ openai:", openai.__version__)

#Contraseña de API De open IA
import os
from getpass import getpass
os.environ["OPENAI_API_KEY"] = getpass("🔐 Ingresa tu clave de OpenAI:")

import numpy as np
print(np.__version__)#Calida numpy

#generar una imagen a partir de un texto
from diffusers import StableDiffusionPipeline# texto a imagen
import torch#detectar si hay GPU.

#Cargas el modelo Stable Diffusion 2.1.
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to("cuda" if torch.cuda.is_available() else "cpu")

#Genera una imagen de prueba desde el prompt
image = pipe("a high-resolution portrait of a young woman smiling").images[0]
image.show()

from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")#modelo ya entrenado de OpenIA

#Prueba
respuesta = llm.invoke("Describe un dragón volador con muchos detalles visuales")
print(respuesta)

from IPython.display import display
from PIL import Image

# Función para generar un prompt desde el LLM
def generar_prompt(categoria):
    instrucciones = {
        "animal": "Genera una descripción visual detallada de un animal en su hábitat natural.",
        "carro": "Genera una descripción visual detallada de un automóvil moderno o futurista en contexto.",
        "rostro": "Genera una descripción visual detallada de un rostro humano con expresión y rasgos únicos."
    }
    return llm.invoke(instrucciones[categoria]).content


# Función para generar imagen desde Stable Diffusion
def generar_imagen(prompt):
    print(f"\n🧠 Prompt generado por el LLM:\n{prompt}")
    image = pipe(prompt).images[0]
    display(image)

# Definir los agentes
def agente_animales():
    prompt = generar_prompt("animal")
    generar_imagen(prompt)

def agente_automoviles():
    prompt = generar_prompt("carro")
    generar_imagen(prompt)

def agente_rostros():
    prompt = generar_prompt("rostro")
    generar_imagen(prompt)

print("🐾 Agente de Animales:")
agente_animales()

print("🚗 Agente de Automóviles:")
agente_automoviles()

print("🙂 Agente de Rostros:")
agente_rostros()
