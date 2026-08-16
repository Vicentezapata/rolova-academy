

# ===== U3 Evaluación Anexo Entregable_EVU3.ipynb =====


--- celda 1 (markdown) ---
 **Evaluación 3**, enfocada en las fases 4 y 5 de CRISP-DM, junto con el código base y la rúbrica correspondiente.

-----

### **Actividad: Evaluación 3 - Modelado y Evaluación con Redes Neuronales**

**Evidencia de Logro:** Implementación, evaluación y comparación de modelos de redes neuronales (LSTM y Transformer) para tareas de clasificación de imágenes o generación de texto.

**Modalidad:** Trabajo grupal (2-3 estudiantes)

#### **Contexto**

Este proyecto es la continuación directa de la "Evaluación 2". Los equipos utilizarán los datos que ya han limpiado y preparado para abordar las fases de **Modelado** y **Evaluación** del ciclo de vida de un proyecto de IA, según el modelo CRISP-DM.

Se implementarán y compararán dos arquitecturas de redes neuronales profundas: una red **Recurrente (LSTM)** y un **Transformer básico**.

#### **Objetivos del Proyecto**

1.  **Aplicar las fases 4 (Modelado) y 5 (Evaluación) del modelo CRISP-DM**. La fase 6 (Despliegue) no será abordada.
2.  **Implementar y entrenar un modelo LSTM** para la tarea seleccionada clasificación de imágenes de Los Simpson o generación de texto con Don Quijote.
3.  **Implementar y entrenar un modelo Transformer básico** para la misma tarea.
4.  **Evaluar y comparar el rendimiento** de ambos modelos utilizando métricas apropiadas.
5.  **Realizar un proceso de *fine-tuning*** para intentar mejorar el rendimiento del mejor modelo.

#### **Requisitos de la Entrega**

Se deberá entregar un único **Jupyter Notebook** que contenga:

  * **Código funcional** que parta del entregable de código base proporcionado.
  * **Implementación clara** de los modelos LSTM y Transformer.
  * Una sección de **Evaluación** que compare los modelos con métricas y visualizaciones (ej. curvas de pérdida/exactitud, matriz de confusión si aplica).
  * Una sección de **Fine-Tuning** donde se documenten los experimentos realizados para mejorar el rendimiento.
  * **Análisis y justificación** de las decisiones tomadas en la selección de hiperparámetros y en la comparación de modelos.
  * **Conclusiones finales** que sinteticen los hallazgos del proyecto.

-----

### **Entregable: Código Base para Estudiantes**

A continuación, se proporciona una propuesta de código en Python (usando TensorFlow/Keras) para que los estudiantes inicien su trabajo. Deben completar las secciones marcadas con `# TO-DO`.

--- celda 2 (code) ---
# -*- coding: utf-8 -*-
"""
 propuesta de Código para Evaluación 3 - Modelado y Evaluación
"""

# ## 1. Importación de Librerías
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# ## 2. Carga de Datos Pre-procesados
# TO-DO: Carguen aquí los datos que prepararon en la Evaluación 2.
# Asegúrense de que estén en el formato correcto (ej. X, y).
# X, y = cargar_datos_procesados('ruta/a/sus/datos.pkl')

# print("Datos cargados. Forma de X:", X.shape)
# print("Datos cargados. Forma de y:", y.shape)

# TO-DO: Dividir los datos en conjuntos de entrenamiento, validación y prueba.
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# ## 3. Modelo 1: Red Neuronal Recurrente (LSTM)

def crear_modelo_lstm(input_shape, num_clases):
    """Crea un modelo LSTM secuencial."""
    model = keras.Sequential()
    model.add(layers.Input(shape=input_shape))
    # TO-DO: Si es texto, añadan una capa de Embedding.
    # model.add(layers.Embedding(input_dim=vocab_size, output_dim=128))

    # TO-DO: Añadan una o más capas LSTM.
    model.add(layers.LSTM(128, return_sequences=False)) # O True si apilan LSTMs
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(num_clases, activation='softmax')) # 'softmax' para clasificación

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# # TO-DO: Instanciar y compilar el modelo
# input_shape_lstm = X_train.shape[1:]
# num_clases = y_train.shape[1]
# modelo_lstm = crear_modelo_lstm(input_shape_lstm, num_clases)
# modelo_lstm.summary()

# # TO-DO: Entrenar el modelo
# history_lstm = modelo_lstm.fit(X_train, y_train,
#                                epochs=10,
#                                batch_size=32,
#                                validation_data=(X_val, y_val))

# ## 4. Modelo 2: Transformer Básico

# Para simplificar, crearemos un bloque Transformer como una capa personalizada.
class TransformerBlock(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):
        super().__init__()
        self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
        self.ffn = keras.Sequential(
            [layers.Dense(ff_dim, activation="relu"), layers.Dense(embed_dim),]
        )
        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = layers.Dropout(rate)
        self.dropout2 = layers.Dropout(rate)

    def call(self, inputs, training):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.layernorm2(out1 + ffn_output)

def crear_modelo_transformer(input_shape, num_clases, embed_dim=32, num_heads=2, ff_dim=32):
    """Crea un modelo de clasificación basado en un bloque Transformer."""
    inputs = layers.Input(shape=input_shape)

    # TO-DO: La entrada a un Transformer necesita embedding y codificación posicional.
    # Si es texto, usen una capa de Embedding.
    # x = layers.Embedding(input_dim=vocab_size, output_dim=embed_dim)(inputs)
    # Si son imágenes, pueden aplanar y usar una Dense para proyectar a embed_dim.

    # Placeholder - El alumno debe implementar la parte de embedding
    x = layers.Dense(embed_dim)(inputs) # Reemplazar si es necesario

    transformer_block = TransformerBlock(embed_dim, num_heads, ff_dim)
    x = transformer_block(x)
    x = layers.GlobalAveragePooling1D()(x)
    x = layers.Dropout(0.1)(x)
    x = layers.Dense(20, activation="relu")(x)
    x = layers.Dropout(0.1)(x)
    outputs = layers.Dense(num_clases, activation="softmax")(x)

    model = keras.Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    return model

# # TO-DO: Instanciar, compilar y entrenar el modelo Transformer
# input_shape_transformer = X_train.shape[1:]
# modelo_transformer = crear_modelo_transformer(input_shape_transformer, num_clases)
# modelo_transformer.summary()
# history_transformer = modelo_transformer.fit(...)

# ## 5. Evaluación y Comparación de Modelos

def plot_history(history, model_name):
    """Dibuja las curvas de accuracy y loss."""
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title(f'Accuracy - {model_name}')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title(f'Loss - {model_name}')
    plt.legend()
    plt.show()

# # TO-DO: Generar gráficos para ambos modelos
# plot_history(history_lstm, "LSTM")
# plot_history(history_transformer, "Transformer")

# # TO-DO: Evaluar en el conjunto de prueba
# print("Evaluación LSTM:")
# results_lstm = modelo_lstm.evaluate(X_test, y_test)
# print("Evaluación Transformer:")
# results_transformer = modelo_transformer.evaluate(X_test, y_test)

# # TO-DO: Si es clasificación, generar reporte y matriz de confusión
# y_pred_lstm = np.argmax(modelo_lstm.predict(X_test), axis=1)
# y_test_labels = np.argmax(y_test, axis=1)
# print("\nReporte de Clasificación LSTM:")
# print(classification_report(y_test_labels, y_pred_lstm))
# print("\nMatriz de Confusión LSTM:")
# print(confusion_matrix(y_test_labels, y_pred_lstm))

# ## 6. Fine-Tuning
# TO-DO: Basado en los resultados, elijan un modelo para mejorar.
# Experimenten con:
# - Diferentes optimizadores (RMSprop, SGD)
# - Diferentes tasas de aprendizaje
# - Aumentar/disminuir la complejidad del modelo (más capas, más neuronas)
# - Ajustar el dropout
# Documenten cada experimento y su resultado.

# ## 7. Conclusiones Finales
# TO-DO: Escriban sus conclusiones aquí.
# - ¿Qué modelo funcionó mejor y por qué creen que fue así?
# - ¿Qué desafíos encontraron?
# - ¿Cómo impactaron sus decisiones de fine-tuning en el resultado?
# - ¿Qué limitaciones tiene su mejor modelo?

--- celda 3 (markdown) ---
-----

### **Rúbrica + Matriz de Evaluación – Evaluación 3 (100 pts)**

Cada criterio tiene un peso de **10 puntos**, evaluado según el porcentaje de cumplimiento alcanzado.

| Nº | Criterio | Puntaje Máximo | Descripción | Matriz de Cumplimiento |
| :--- | :--- | :--- | :--- | :--- |
| **1️⃣** | **Implementación del Modelo LSTM** | 10 pts | El modelo LSTM está correctamente implementado, compilado y adaptado a la tarea (imagen/texto). | **100% (10 pts):** Implementación correcta, lógica y bien adaptada. \<br\> **75% (7.5 pts):** Implementación funcional pero con pequeños errores o desajustes. \<br\> **50% (5 pts):** Implementación incompleta o con errores conceptuales. \<br\> **0% (0 pts):** No se implementa el modelo. |
| **2️⃣** | **Implementación del Transformer** | 10 pts | El modelo Transformer básico está correctamente implementado, incluyendo embeddings y el bloque de atención. | **100% (10 pts):** Implementación completa y correcta del flujo del Transformer. \<br\> **75% (7.5 pts):** Implementación funcional, pero con detalles omitidos (ej. embedding posicional). \<br\> **50% (5 pts):** Implementación con errores graves en la arquitectura. \<br\> **0% (0 pts):** No se implementa el modelo. |
| **3️⃣** | **Proceso de Entrenamiento** | 10 pts | Se entrena cada modelo de forma adecuada, usando conjuntos de entrenamiento y validación. | **100% (10 pts):** Proceso de entrenamiento robusto, con separación de datos clara. \<br\> **75% (7.5 pts):** Entrenamiento correcto, pero sin uso de set de validación. \<br\> **50% (5 pts):** El entrenamiento se ejecuta pero de forma incorrecta (ej. sobreajuste evidente no abordado). \<br\> **0% (0 pts):** No se entrena los modelos. |
| **4️⃣** | **Evaluación Cuantitativa** | 10 pts | Se utilizan métricas pertinentes (loss, accuracy, precision, recall) para evaluar los modelos en el conjunto de prueba. | **100% (10 pts):** Evaluación completa con métricas bien interpretadas. \<br\> **75% (7.5 pts):** Se calculan métricas, pero con interpretación limitada. \<br\> **50% (5 pts):** Se usa solo una métrica básica (ej. accuracy) sin análisis. \<br\> **0% (0 pts):** No se realiza evaluación cuantitativa. |
| **5️⃣** | **Análisis Comparativo** | 10 pts | Se comparan explícitamente los resultados del LSTM y el Transformer, explicando fortalezas y debilidades. | **100% (10 pts):** Análisis comparativo profundo, basado en evidencia (métricas y gráficos). \<br\> **75% (7.5 pts):** Comparación válida, pero superficial. \<br\> **50% (5 pts):** Se mencionan ambos modelos pero no se comparan directamente. \<br\> **0% (0 pts):** No hay comparación. |
| **6️⃣** | **Experimentación y Fine-Tuning** | 10 pts | Se realizan y documentan al menos dos experimentos de ajuste de hiperparámetros sobre uno de los modelos. | **100% (10 pts):** Múltiples experimentos bien justificados y documentados. \<br\> **75% (7.5 pts):** Se realiza al menos un experimento de forma correcta. \<br\> **50% (5 pts):** Se mencionan ideas de ajuste pero no se implementan. \<br\> **0% (0 pts):** No se realiza fine-tuning. |
| **7️⃣** | **Visualizaciones de Evaluación** | 10 pts | Se generan y analizan gráficos clave como las curvas de entrenamiento/validación y la matriz de confusión. | **100% (10 pts):** Visualizaciones claras, bien interpretadas y que apoyan el análisis. \<br\> **75% (7.5 pts):** Gráficos presentes y funcionales, pero sin interpretación. \<br\> **50% (5 pts):** Gráficos confusos o mal generados. \<br\> **0% (0 pts):** No se incluyen visualizaciones. |
| **8️⃣** | **Calidad del Código y Documentación**| 10 pts | El notebook es legible, está bien estructurado y contiene comentarios que explican el código y las decisiones. | [cite\_start]**100% (10 pts):** Código limpio, eficiente y excelentemente documentado[cite: 18]. \<br\> **75% (7.5 pts):** Código funcional con documentación adecuada pero inconsistente. \<br\> **50% (5 pts):** Código desordenado o con documentación mínima. \<br\> **0% (0 pts):** Código no funcional o sin documentación. |
| **9️⃣** | **Justificación de Decisiones** | 10 pts | Se explican las razones técnicas detrás de la elección de arquitecturas, hiperparámetros y conclusiones. | [cite\_start]**100% (10 pts):** Justificación técnica sólida y reflexiva en todo el proyecto[cite: 19]. \<br\> **75% (7.5 pts):** Justificaciones válidas pero limitadas a ciertas partes. \<br\> **50% (5 pts):** Justificaciones genéricas o sin base técnica. \<br\> **0% (0 pts):** No se justifican las decisiones. |
| **🔟** | **Conclusiones y Reflexión Final** | 10 pts | Se presenta una sección de conclusiones que resume los hallazgos, desafíos y aprendizajes del proyecto. | [cite\_start]**100% (10 pts):** Conclusiones críticas, bien alineadas con los resultados y reflexivas[cite: 19]. \<br\> **75% (7.5 pts):** Buen resumen de resultados, pero con poca reflexión crítica. \<br\> **50% (5 pts):** Conclusiones superficiales o que no se conectan con el trabajo realizado. \<br\> **0% (0 pts):** No se incluyen conclusiones. |

--- celda 4 (markdown) ---
<div class="md-recitation">
  Sources
  <ol>
  <li><a href="https://github.com/keras-team/keras-io">https://github.com/keras-team/keras-io</a> subject to Apache - 2.0</li>
  </ol>
</div>


# ===== U3 Video IA.pptx =====


## Slide 1
- VIDEOINTELIGENCIA ARTIFICIAL

## Slide 2
- VIDEO
- https://vimeo.com/1106578210
- En el siguiente enlace encontrarás el video correspondiente a la unidad 3 de esta asignatura:

## Slide 3
- VIDEOINTELIGENCIA ARTIFICIAL