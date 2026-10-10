import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_3d_path():
    print("Generating 3D Autonomous Navigation Output...")
    
    # 1. Define Grid Environment (30x30)
    grid_size = 30
    x = np.arange(grid_size)
    y = np.arange(grid_size)
    X, Y = np.meshgrid(x, y)
    
    # Base terrain elevation (flat ground = 0)
    Z = np.zeros((grid_size, grid_size))
    
    # 2. Inject Random Obstacles (Elevated Terrain/Walls)
    np.random.seed(42)
    for _ in range(40):
        ox, oy = np.random.randint(2, grid_size-2, 2)
        Z[ox-1:ox+2, oy-1:oy+2] = 5  # Wall height
        
    # 3. Simulate a calculated optimal path avoiding walls
    # (In a full integration, this array comes directly from path_planner.py)
    path_x = [2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    path_y = [2, 2, 2, 3, 4, 5, 6, 7, 8, 8, 8,  9,  10, 11, 12, 13, 14, 14, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    path_z = [0.2] * len(path_x) # Slightly elevated for visibility
    
    # 4. Render 3D Plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot terrain and walls
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, edgecolor='k', linewidth=0.2)
    
    # Plot Start Node (Orange)
    ax.scatter(path_x[0], path_y[0], 1, color='orange', s=100, label='Start Node')
    
    # Plot Destination Node (Turquoise)
    ax.scatter(path_x[-1], path_y[-1], 1, color='cyan', s=100, label='Destination Node')
    
    # Plot AI Computed Trajectory
    ax.plot(path_x, path_y, path_z, color='purple', linewidth=4, label='AI Optimal Path')
    
    ax.set_title("3D Autonomous Navigation Spatial Output")
    ax.set_xlabel("X Coordinates")
    ax.set_ylabel("Y Coordinates")
    ax.set_zlabel("Elevation / Obstacles")
    ax.legend()
    
    # Display the final 3D output
    plt.show()

if __name__ == "__main__":
    generate_3d_path()