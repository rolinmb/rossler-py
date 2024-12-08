import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Define the Rossler system
def rossler(t, state, a=0.2, b=0.2, c=5.7):
    x, y, z = state
    dx = -y - z
    dy = x + a * y
    dz = b + z * (x - c)
    return [dx, dy, dz]

if __name__ == "__main__":
    # Solve the Rossler system
    t_span = (0, 200)
    t_eval = np.linspace(t_span[0], t_span[1], 10000)
    initial_state = [1, 1, 1]
    sol = solve_ivp(rossler, t_span, initial_state, t_eval=t_eval)
    x, y, z = sol.y
    # Set up the figure and 3D axes
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlim([-15, 15])
    ax.set_ylim([-15, 15])
    ax.set_zlim([0, 30])
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("Rossler Attractor")
    # Initialize the plot
    line, = ax.plot([], [], [], lw=0.5, color='blue')
    # Animation function
    def update(num):
        line.set_data(x[:num], y[:num])
        line.set_3d_properties(z[:num])
        return line,
    ani = FuncAnimation(fig, update, frames=len(t_eval), interval=10, blit=True)
    plt.show()
