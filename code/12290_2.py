w', y' = broadcast(w, y)
x' = f(w')
ax, bx = chunk(x')
ay, by = chunk(y')
a = g(ax, ay)
b = g(bx, by)