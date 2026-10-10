import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Ensure assets directory exists for saving outputs
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Simulated Path Data (x, y coordinates)
path_x = [2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
path_y = [2, 2, 2, 3, 4, 5, 6, 7, 8, 8, 8,  9,  10, 11, 12, 13, 14, 14, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
grid_size = 30

def generate_output_1_3d_spatial():
    """Generates a 3D topographical map mimicking Lidar obstacle detection (like image_e6f077.jpg)"""
    x = np.arange(grid_size)
    y = np.arange(grid_size)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros((grid_size, grid_size))
    
    # Inject Random Obstacles (Elevated Terrain)
    np.random.seed(42)
    for _ in range(40):
        ox, oy = np.random.randint(2, grid_size-2, 2)
        Z[ox-1:ox+2, oy-1:oy+2] = 5  
        
    path_z = [0.2] * len(path_x) 
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5, edgecolor='k', linewidth=0.2)
    ax.scatter(path_x[0], path_y[0], 1, color='orange', s=150, label='Start Node')
    ax.scatter(path_x[-1], path_y[-1], 1, color='cyan', s=150, label='Destination')
    ax.plot(path_x, path_y, path_z, color='purple', linewidth=4, label='A* Optimal Path')
    
    ax.set_title("Output 1: 3D Autonomous Navigation Spatial Map")
    ax.set_xlabel("X Coordinates")
    ax.set_ylabel("Y Coordinates")
    ax.set_zlabel("Obstacle Elevation")
    ax.legend()
    
    plt.savefig(os.path.join(ASSETS_DIR, "3d_spatial_output.png"))
    plt.show()

def generate_output_2_heuristic_heatmap():
    """Generates a 2D Heatmap showing the AI's f-score calculation cost."""
    # Simulate a cost map where obstacles are 'inf' (rendered as highest value) and path is lowest cost
    cost_map = np.random.uniform(10, 50, (grid_size, grid_size))
    
    # Map obstacles from Output 1
    np.random.seed(42)
    for _ in range(40):
        ox, oy = np.random.randint(2, grid_size-2, 2)
        cost_map[ox-1:ox+2, oy-1:oy+2] = 100 # High cost for walls
        
    # Lower cost along the chosen path
    for px, py in zip(path_x, path_y):
        cost_map[px, py] = 5
        
    plt.figure(figsize=(8, 6))
    plt.imshow(cost_map, cmap='magma', origin='lower')
    plt.colorbar(label='A* Heuristic Cost (f-score)')
    plt.plot(path_x, path_y, color='cyan', linewidth=2, label='Selected Path')
    plt.scatter(path_x[0], path_y[0], color='orange', s=100, label='Start')
    plt.scatter(path_x[-1], path_y[-1], color='lime', s=100, label='Goal')
    
    plt.title("Output 2: AI Pathfinding Search Cost Heatmap")
    plt.xlabel("X Grid")
    plt.ylabel("Y Grid")
    plt.legend()
    
    plt.savefig(os.path.join(ASSETS_DIR, "heuristic_heatmap.png"))
    plt.show()

def generate_output_3_telemetry():
    """Generates a Kinematic Telemetry graph showing vehicle speed and distance remaining."""
    time_steps = np.arange(len(path_x))
    
    # Simulate Distance to Goal decreasing
    distance_to_goal = np.linspace(100, 0, len(path_x))
    
    # Simulate Vehicle Speed (Accelerating, Cruising, Decelerating)
    speed = np.zeros(len(path_x))
    speed[:5] = np.linspace(0, 25, 5)        # Acceleration
    speed[5:-5] = 25 + np.random.normal(0, 1, len(path_x)-10) # Cruising with slight noise
    speed[-5:] = np.linspace(25, 0, 5)       # Deceleration to stop
    
    fig, ax1 = plt.subplots(figsize=(10, 5))
    
    # Distance Axis
    color = 'tab:red'
    ax1.set_xlabel('Time Steps (s)')
    ax1.set_ylabel('Distance to Destination (m)', color=color)
    ax1.plot(time_steps, distance_to_goal, color=color, linewidth=3, label='Distance Remaining')
    ax1.tick_params(axis='y', labelcolor=color)
    
    # Speed Axis
    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel('Vehicle Speed (km/h)', color=color)  
    ax2.plot(time_steps, speed, color=color, linestyle='--', linewidth=2, label='Velocity Profile')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.fill_between(time_steps, speed, alpha=0.1, color=color)
    
    plt.title("Output 3: Autonomous Vehicle Telemetry & Kinematics")
    fig.tight_layout() 
    
    plt.savefig(os.path.join(ASSETS_DIR, "vehicle_telemetry.png"))
    plt.show()

if __name__ == "__main__":
    print("Generating Advanced AI Outputs...")
    generate_output_1_3d_spatial()
    generate_output_2_heuristic_heatmap()
    generate_output_3_telemetry()
    print("All outputs generated and saved to the 'assets/' folder.")