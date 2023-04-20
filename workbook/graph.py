import matplotlib.pyplot as plt

x =[
    (2002,1,1),
    (2002,2,1),
    (2002,3,1),
    (2002,4,1)
]

x1 = list(map(lambda y: str(y[0]) + "/" + str(y[1]), x))
y = [1200,900,1300,1400]
y1 = [200,200,500,800]
y2 = [800,900,1500,1800]

fig, axe = plt.subplots()
axe.plot(x1,y, linewidth=12)
axe.plot(x1,y1, linewidth=15)
axe.plot(x1,y2, linewidth=10)
axe.annotate("best value",xy = (3.0,1800), xytext =(3,2000), arrowprops=dict(arrowstyle='->',facecolor='green')   )

plt.show()