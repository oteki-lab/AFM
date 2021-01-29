import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

filename = ''
sns.set(font_scale=5)
sns.set_style("ticks", {'axes.grid': True, 'xtick.top': True,  'ytick.right': True, "xtick.direction": "in", "ytick.direction": "in"})

csv_input = pd.read_csv(filepath_or_buffer=filename+'.csv', encoding="ms932", sep=",")
x = npdata=np.array(csv_input[["diameter [nm]"]].values.flatten())
y = npdata=np.array(csv_input[["height [nm]"]].values.flatten())
data = np.stack([x, y], 1)#np.random.randn(100, 2)  #
df = pd.DataFrame(data, columns=['X', 'Y'])

g = sns.JointGrid(x="X", y="Y", data=df, space=0, xlim=(0,80), ylim=(0,15), height=8, ratio=4)
g.plot_joint(sns.kdeplot, shade=False, cmap="jet", n_levels=10)
g.plot_joint(plt.scatter, facecolor='None', edgecolors='gray', s=20)
g.plot_marginals(sns.distplot, kde=True)

g.set_axis_labels(r'$diameter \quad [nm]$', r'$height \quad [nm]$')
g.fig.set_size_inches((20,16))

plt.savefig(filename)

mean = np.array([np.mean(x), np.mean(y)])
var = np.array([np.var(x), np.var(y)])
std = np.array([np.std(x), np.std(y)])
cov = np.cov(data.T, bias=0)
print('Mean(D,H): ', mean)
print('Variant(D,H): ', var)
print('Standard deviation(D,H): ', std)
print('Covariance matrix: ', cov)

data_1 = np.random.multivariate_normal(mean, cov, size=400)
#print(np.cov(data_1, rowvar=False)) # 分散共分散の確認
#print(np.mean(data_1, axis=0))      # 期待値の確認

df = pd.DataFrame(data_1, columns=['X', 'Y'])

g = sns.JointGrid(x="X", y="Y", data=df, space=0, xlim=(0,80), ylim=(0,16), height=8, ratio=4)
g.plot_joint(sns.kdeplot, shade=False, cmap="jet", n_levels=10)
g.plot_joint(plt.scatter, facecolor='None', edgecolors='gray', s=20)
g.plot_marginals(sns.distplot, kde=True)

g.set_axis_labels(r'$diameter \quad [nm]$', r'$height \quad [nm]$')
g.fig.set_size_inches((16,16))

plt.savefig(f'{filename}_Multivariate normal distribution')