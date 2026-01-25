
```{code-cell} ipython3

import plotly.graph_objects as go
import numpy as np

# 1. Configuración de datos
Q = 3
t_max = 200
r0_val = 5        # Valor inicial fijo para r0
theta0_val = 0    # Valor inicial fijo para theta0

# Creamos un rango de pasos para el slider (por ejemplo, el tiempo 't')
t_steps = np.arange(0, t_max + 1, 5) 

# 2. Crear la figura
fig = go.Figure()

# Añadimos una traza por cada paso del tiempo 't'
for t in t_steps:
    T_range = np.linspace(0, t, max(2, int(t)))
    theta = np.full(T_range.shape, theta0_val)
    r = np.sqrt(r0_val**2 + Q / (2 * np.pi) * T_range)
    
    fig.add_trace(
        go.Scatterpolar(
            r=r,
            theta=np.degrees(theta), # Plotly usa grados por defecto
            mode='lines',
            name=f't={t}',
            visible=False,
            line=dict(color="firebrick", width=2)
        )
    )

# Hacer visible solo la primera traza
fig.data[0].visible = True

# 3. Crear el Slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": f"Evolución temporal: t = {t_steps[i]}"}],
        label=str(t_steps[i])
    )
    step["args"][0]["visible"][i] = True
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Tiempo (t): "},
    pad={"t": 50},
    steps=steps
)]

# 4. Ajustar diseño polar
fig.update_layout(
    sliders=sliders,
    polar=dict(
        radialaxis=dict(range=[0, 10], gridcolor="lightgrey"),
        angularaxis=dict(gridcolor="lightgrey")
    ),
    showlegend=False,
    width=700,
    height=600
)

fig.show()
```

```{code-cell} ipython3
import plotly.graph_objects as go
import numpy as np

# 1. Configuración de parámetros
Q = 3
r0_list = [2, 5, 8, 10]  # Valores para los botones
t_steps = np.arange(0, 201, 10)  # Pasos para el slider

fig = go.Figure()

# 2. Generar todas las trazas (r0 * t)
for r0 in r0_list:
    for t in t_steps:
        T_range = np.linspace(0, t, max(2, int(t)))
        theta = np.zeros(T_range.shape)
        r = np.sqrt(r0**2 + Q / (2 * np.pi) * T_range)
        
        fig.add_trace(
            go.Scatterpolar(
                r=r,
                theta=np.degrees(theta),
                mode='lines',
                name=f'r0={r0}, t={t}',
                visible=False,
                line=dict(width=4, color="#1f77b4")
            )
        )

# Activar la primera traza
fig.data[0].visible = True

# 3. Lógica de los Botones (Cambian el bloque de trazas)
buttons = []
for i, r0 in enumerate(r0_list):
    # Al pulsar un botón, queremos que se vea el t=0 de ese r0 específico
    # y que el slider sepa que ahora manda ese bloque.
    visibility = [False] * len(fig.data)
    visibility[i * len(t_steps)] = True
    
    buttons.append(dict(
        method="update",
        label=f"r₀ = {r0}",
        args=[{"visible": visibility},
              {"title": f"Cinemática: r₀ inicial = {r0}"}]
    ))

# 4. Lógica del Slider (Mueve el tiempo dentro del r0 seleccionado)
# NOTA: En modo estático, el slider actuará sobre el bloque actual
steps = []
for j, t in enumerate(t_steps):
    step = dict(
        method="update",
        label=f"{t}",
        args=[{"visible": [False] * len(fig.data)}]
    )
    # Este es el truco: activamos el paso 'j' de TODOS los bloques r0
    # Pero como el botón solo deja uno disponible, el efecto es el correcto
    for k in range(len(r0_list)):
        step["args"][0]["visible"][j + (k * len(t_steps))] = True
    steps.append(step)

# 5. Layout mejorado para evitar solapamientos
fig.update_layout(
    width=850,   # Más ancho
    height=700,  # Más alto
    margin=dict(t=120, b=50, l=50, r=50), # Espacio para botones y título
    updatemenus=[dict(
        type="buttons",
        direction="right",
        x=0.5,
        xanchor="center",
        y=1.15, # Lo subimos por encima del título
        showactive=True,
        buttons=buttons,
        bgcolor="#f8f9fa",
        bordercolor="#ced4da"
    )],
    sliders=[dict(
        active=0,
        currentvalue={"prefix": "Tiempo acumulado (t): ", "font": {"size": 16}},
        pad={"t": 60},
        steps=steps
    )],
    polar=dict(
        radialaxis=dict(range=[0, 15], gridcolor="lightgrey"),
        angularaxis=dict(gridcolor="lightgrey")
    )
)

fig.show()

```

# Animación de Trayectoria

Esta animación muestra la evolución de una trayectoria en el tiempo.

```{code-cell} ipython3
import numpy as np
import matplotlib
#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt
from ipywidgets import interactive
import ipywidgets as widgets

Q=3
def fun2(r0,theta0,t):
    fig = plt.figure(figsize=(13,10))
    T=np.linspace(0,t,t)
    theta = theta0*np.ones(np.size(T))
    r = np.sqrt(r0**2+Q/2/np.pi*T)
    ax = plt.subplot(111, projection='polar')
    ax.plot(theta0,r0,'o', linewidth=5)
    ax.plot(theta,r)
    ax.grid(True)
    ax.set_rmax(10)
    #ax.set_rticks([])
    #ax.set_xticks([])

interactive(fun2,r0=(0,10,0.2),theta0=(0,np.pi,np.pi/12),t=(0,200))

```