---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Cinemática

## Trayectoria

La trayectoria es la ley que da la posición de una partícula fluida como función del tiempo y de su posición inicial. Si se conoce el campo de velocidades, 
$\mathbf{v}(\mathbf{x},t)$, la trayectoria responde a la ecuación $$ \frac{\mathrm{d}\mathbf{x}}{\mathrm{d} t} = \mathbf{v}(\mathbf{x},t).$$    


Esta ecuación representa las trayectorias de todas las partículas fluidas por lo que para elegir una trayectoria en concreto se 
debe elegir una única partícula fluida imponiendo su posición en un instante determinado mediante una condición inicial:

$$ t = t_0: \mathbf{x} = \mathbf{x}_0. $$


La solución será de la forma:

$$ \mathbf{x} = \mathbf{x}_t(t,\mathbf{x}_0). $$



::::{tip} Ejemplo
:class: simple
Sea un campo fluido bidimensional del que se conoce su velocidad en cada punto, $(v_x, v_y) = (x, \sqrt{t})$.

¿Cuál es la trayectoria de una partícula fluida que en el instante inicial pasa por el punto $(0.1,0)$?

:::{dropdown} Solución
:open: false
Para la componente $x$ se tiene

 
\begin{equation*} 
\frac{\mathrm{d} x}{\mathrm{d} t} = v_x \rightarrow \frac{\mathrm{d}{x}}{\mathrm{d} t} = x \rightarrow \frac{\mathrm{d}{x}}{x} = \mathrm{d} t. 
\end{equation*}

Integramos y obtenemos
\begin{equation*} 
\ln{\frac{x}{x_0}} = t-t_0 \rightarrow x = x_0\exp{(t-t_0)}. 
\end{equation*}



Para la componente $y$ se tiene
\begin{equation*} 
\frac{\mathrm{d}{y}}{\mathrm{d} t} = v_y \rightarrow \frac{\mathrm{d}{y}}{\mathrm{d} t} = \sqrt{t} \rightarrow \mathrm{d}{y} = t^{1/2}\mathrm{d} t.
\end{equation*}


Integramos y obtenemos

\begin{equation*} 
y-y_0 = \frac{2}{3}(t^{3/2}-t_0^{3/2}).
\end{equation*}


Las expresiones obtenidas representan las trayectorias de todas las partículas fluidas presentes en nuestro dominio.
\begin{equation*} 
\begin{aligned}
x &= x_0\exp{(t-t_0)},\\\
y &=y_0+\frac{2}{3}(t^{3/2}-t_0^{3/2}).
\end{aligned}
\end{equation*}

El siguiente paso es particularizar estas expresiones para una partícula fluida concreta, en este caso la que en el instante $t_0 = 0$ se encuentra en el punto $(x_0, y_0) = (0.1, 0)$, quedando
\begin{equation*} 
\begin{aligned}
x &= 0.1\exp{(t)},\\\
y &=\frac{2}{3}t^{3/2}.
\end{aligned}
\end{equation*}

:::
::::
% Fin ejemplo




<embed src="./figures/Trayectoria_1.svg">

Trayectoria de la partícula fluida que inicialmente está en el punto $(0.1, 0)$.

.cite[Esperar a que se carguen las imagenes antes de reproducir.]



# Animación de Trayectoria


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

## Descripción

La trayectoria sigue las ecuaciones:
- $x(t) = x_0 e^t$ donde $x_0 = 0.1$
- $y(t) = y_0 + \dfrac{2t^{1.5}}{3}$ donde $y_0 = 0$

El parámetro temporal $t$ varía de 0 a 7.
## Descripción

La trayectoria sigue las ecuaciones:
- $x(t) = x_0 e^t$ donde $x_0 = 0.1$
- $y(t) = y_0 + \frac{2t^{1.5}}{3}$ donde $y_0 = 0$

El parámetro temporal $t$ varía de 0 a 7.


##Senda

La senda es la curva que recorre la partícula fluida en su movimiento. Para obtener la ecuación de la senda se debe eliminar el tiempo de la ecuación de la trayectoria donde actúa como un parámetro.

La diferencia entre la senda y el trayectoria, es que no podemos conocer la posición instantánea de la partícula fluida sobre la senda, sino únicamente el camino que ha recorrido.

La solución será de la forma:

$$ \mathbf{x} = \mathbf{x}_s(\mathbf{x}_0). $$


##Ejemplo
<br/>
Para el ejemplo propuesto anteriormente, la senda de una partícula fluida que en el instante inicial se encuetra en el punto $(x_0, y_0)$ responde a la expresión
$$x = x_0\exp\left[\left(\frac{3}{2}(y-y_0)\right)^{3/2}\right] .$$

Esta expresión se ha obtenido despejando $t$ como función de $y$ e $y_0$, y sustituyendo en la expresión de $x$ de la trayectoria. Particularizando queda
$$x = 0.1\exp\left[\left(\frac{3}{2}y\right)^{3/2}\right] .$$


##Ejemplo

<embed src="./figures/Trayectoria_2.svg">

Senda de la partícula fluida que inicialmente está en el punto $(0.1, 0)$ en azul y trayectoria de la partícula fluida que inicialmente está en el punto $(5, 0.5)$ en rojo.


##Ejemplo

<embed src="./figures/Trayectoria_3.svg">

Trayectorias de dos partículas fluidas que inicialmente están en los puntos $(0.1, 0)$ y $(5, 0.5)$.

---
class: left
##Línea de traza
<br/>
Si a partir de un instante inicial se introduce un colorante en un punto $\mathbf{x}_T$ en el seno de un fluido, de tal forma que toda partícula fluida que pase por ese punto quede marcada, 
la línea formada por estas partículas coloreadas se denomina *línea de traza*.

--

En un instante $t$ dado, las partículas fluidas que forman la línea de traza han pasado necesariamente por el punto $\mathbf{x}_T$ en algún instante intermedio $\tau$ que cumple la expresión $0\le \tau \le t$.

---
class: left
##Línea de traza
<br/>
La línea de traza responde a la misma equación que la trayectoria, 
$$ \frac{\mathrm{d}\mathbf{x}}{\mathrm{d} t} = \mathbf{v}(\mathbf{x},t).$$ 

--

Se distingue de la trayectoria por la condición inicial. Se debe imponer la condición de que las partículas fluidas han pasado por el punto $\mathbf{x}_T$ en el instante $t=\tau$.

$$ t = \tau: \mathbf{x} = \mathbf{x}_T. $$

--
La solución tiene la forma 

$$ \mathbf{x} = \mathbf{x}\_{z}(t, \tau, \mathbf{x}_T).$$

---
class: left
##Ejemplo
<br/>
Volviendo al ejemplo anterior para el que ya conocemos las trayectorias de todas las partículas del campo fluido que en el instante $t=0$ se encuentran en la posición $(x,y)=(x_0,y_0)$:
$$ x = x_0\exp{(t)}. $$
$$ y = y_0 + \frac{2}{3}t^{3/2}. $$

--
Lo único que se necesita es identificar cuáles han pasado en el instante $\tau$ por el marcador situado en el punto $\mathbf{x}_T$.

---
class: left
##Ejemplo

Para imponer esta condición se impone que en el instante $t=\tau$ la posición de la partícula fluida es $(x,y)=(x_T,y_T)$. Recurriendo a la expresión de la trayectoría, se tiene:
$$ x_T = x_0\exp{(\tau)}, $$
$$ y_T = y_0 + \frac{2}{3}\tau^{3/2}. $$

--
De esta expresion podemos despejar la posición inicial, $x_0$ e $y_0$. Este punto inicial selecciona de entre todas las trayectorias la de la partícula fluida
 que en el instante $t=\tau$ pasan por el punto $\mathbf{x}_T$.
$$x_0 = \frac{x_T}{\exp(\tau)} $$
$$y_0 = y_T - \frac{2}{3}\tau^{3/2}$$

---
class: left
##Ejemplo
<br/><br/>

Finalmente la expresión de la traza quedaría
$$ x = x_T\exp(t-\tau), $$
$$ y = y_T + \frac{2}{3}\left(t^{3/2}-\tau^{3/2}\right).$$

---
class: center
##Ejemplo

<embed src="./figures/STraza.svg">

Línea de traza para un marcador situado en el punto $(5, 2)$.

---
class: center
##Ejemplo

<embed src="./figures/Traza.svg">

Línea de traza para un marcador situado en el punto $(5, 2)$ junto a las trayectorias de las partículas fluidas que pasan por ese punto en los instantes $\tau = 0,\ 1\ \mathrm{y}\ 3$.


---
class: left
##Línea de corriente
<br/>
La línea de corriente es una línea que, en un instante dado, es tangente en cada uno de sus puntos a la velocidad local del fluido. Indica gráficamente cómo se está moviendo el fluido en ese instante.

--

Utilizando como parámetro la longitud $l$ sobre la línea de corriente, su tangente se puede expresar como
$$ \mathbf{t} = \frac{\mathrm{d}\mathbf{x}}{\mathrm{d}l}. $$

--

De esta forma la ecuación que describe la línea de corriente queda:
$$ \frac{\mathrm{d}\mathbf{x}}{\mathrm{d}l} = \frac{\mathbf{v}(\mathbf{x},t)}{\| \mathbf{v}(\mathbf{x},t) \|} \quad \mathrm{con}\ \mathbf{x}=\mathbf{x}_0\ \mathrm{en} \ l=0. $$

---
name: ejlc
class: left
##Ejemplo
<br/>
Volviendo al ejemplo del campo fluido bidimensional con $(v_x, v_y) = (x, \sqrt{t})$, se pretende calcular la línea de corriente que pasa por el punto $(x_0, y_0)$ en $l=0$.

--

La ecuación que decribe las líneas de corriente se puede escribir para cada componente por separado,
$$ \frac{\mathrm{d}x}{\mathrm{d}l} = \frac{v_x}{\| \mathbf{v} \|} \qquad \frac{\mathrm{d}y}{\mathrm{d}l} = \frac{v_y}{\| \mathbf{v} \|}. $$

--
Eliminando el parámetro $l$ y el módulo de la velocidad de estas ecuaciones se obtiene la igualdad que describe las líneas de corriente para este caso bidimensional,
$$ \frac{\mathrm{d}x}{v_x} = \frac{\mathrm{d}y}{v_y}. $$

---
class: left
##Ejemplo
<br/>
Incorporando la condición de contorno se obtiene la expresión de la línea de corriente que pasa por el punto $(x_0, y_0)$.

$$ y = y_0 + \sqrt{t}\ln \left(\frac{x}{x_0}\right). $$

--

En la expresión obtenida se puede ver claramente que la línea de corriente varía con el tiempo, aunque siempre esté anclada al punto fijo $(x_0, y_0)$.

---
class: center
##Ejemplo

<embed src="./figures/SLC.svg">

Línea de corriente que pasa por el punto $(10, 0)$ en rojo junto con los vectores de velocidad en algunos de sus puntos. Se puede apreciar la tangencia de estos vectores a la línea de corriente.

---
class: center
##Ejemplo

<embed src="./figures/LC.svg">

Evolución de líneas de corriente ancladas en $x=0$ y equiespaciadas una unidad en dirección $y$. Superpuesto se presenta el campo de vectores de velocidad.

---
class: left
##Conclusión
<br/>
En esta presentación se ha intentado mostrar mediante un resumen teórico y un sencillo ejemplo las diferencias que hay entre las distintas líneas que 
aparecen en la cinemática de los fluidos.

La intención de esta presentación es esclarecer cuáles son las diferencias entre los distintos tipos de líneas en el caso **no estacionario**. En el caso estacionario las líneas coinciden.

Se ha recurrido a 
animaciones con botones de control para que, a diferencia de lo que ocurre con los apuntes tradicionales, el alumno pueda participar activamente en el aprendizaje de los conceptos 
aquí presentados.

Se pretende que el hecho de poder parar y analizar los gráficos para distintos instantes de tiempo, consiga mejorar el aprendizaje de los conceptos aquí expuestos.

