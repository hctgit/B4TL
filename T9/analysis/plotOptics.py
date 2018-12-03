import pybdsim
import matplotlib.pyplot as plt
import numpy as np
import pymadx
import robdsim

a = pybdsim.Data.Load("optics.root")
b = pymadx.Tfs("MADX/madx.tfs")

f = plt.figure(1,figsize=(10,7))
plt.plot(a.S(),np.sqrt(a.Sigma_x()),'.-',label='X')
plt.plot(a.S(),np.sqrt(a.Sigma_y()),'.-',label='Y')
plt.xlabel('$s$ [m]')
plt.ylabel('$\sqrt{\\beta_{x,y}\\epsilon}$ [m]')
plt.legend(loc=0)
pybdsim.Plot.AddMachineLatticeToFigure(f,b)
f.savefig("sigma.png")

f = plt.figure(2,figsize=(10,7))
plt.plot(a.S(),np.sqrt(a.Beta_x()),'.-',label='$\\beta_x$')
plt.plot(a.S(),np.sqrt(a.Beta_y()),'.-',label='$\\beta_y$')
plt.xlabel('$s$ [m]')
plt.ylabel('$\\beta_{x,y}$ [m]')
plt.legend(loc=0)
pybdsim.Plot.AddMachineLatticeToFigure(f,b)
f.savefig("beta.png")

f=plt.figure(3,figsize=(10,7))
plt.fill_between(a.S(), -np.sqrt(a.Sigma_x()), np.sqrt(a.Sigma_x()),color='blue',alpha=0.5,label='X')
plt.fill_between(a.S(), -np.sqrt(a.Sigma_y()), np.sqrt(a.Sigma_y()),color='orange',alpha=0.5,label='Y')
plt.xlabel('$s$ [m]')
plt.ylabel('$\sqrt{\\beta_{x,y}\\epsilon}$ [m]')
plt.legend(loc=0)
pybdsim.Plot.AddMachineLatticeToFigure(f,b)
f.savefig("envelopes.png")

