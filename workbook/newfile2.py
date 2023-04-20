import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
squares1 =[1,3,7,12,21]
x_vals = [1,2,3,4,5]
plt.style.use('seaborn')
fix, ax = plt.subplots()
style= dict(size=15,color="grey")
ax.plot(x_vals,squares,squares1, linewidth=3)

for i in range(1,5):
    ax.text(x_vals[i],squares[i],str(squares[i]), ha='right', **style)
    ax.text(x_vals[i],squares1[i],str(squares1[i]), ha='right', **style)
ax.set_title("Square values", fontsize = 24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares", fontsize=14)

ax.tick_params(axis='both',labelsize = 14)
plt.show()