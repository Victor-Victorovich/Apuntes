from pylab import *

#Imagenes mas bioitas.
import pylab
params = { 'backend': 'ps',
          'axes.labelsize': 18,
          'font.size': 18,
          'xtick.labelsize': 18,
          'ytick.labelsize': 18,
          'text.usetex': True }
pylab.rcParams.update(params)

fig = figure(figsize=(8, 6))

xlim([ 0, 100])
ylim([0, 10])

ptos = 150

T = linspace(0,7,60)
X = []
Y = []
x0 = 0.1
y0 = 0
for i, t in enumerate(T):


    x = x0*np.exp(t)
    y = y0 + 2*t**1.5/3

    X.append(x)
    Y.append(y)
    
    line, = plot(X, Y, 'b')
    pto, = plot(x, y, 'bo')
    title(f"$t={t:.2f}$")
    
    # savefig('./Images_png/Trayectoria/Traj_'+str(i) + '.png', format='png', dpi = ptos)
    # savefig('./Images_pdf/Trayectoria/Traj_'+str(i) + '.pdf', format='pdf')

    line.remove()
    pto.remove()
close()
