import numpy as np
from scipy.integrate import solve_ivp

class NewtonSolverIVP3D:
    def __init__(self):
        # Initial conditions and forces are now vectors in 3D
        self.forces = []  # List to store 3D force functions
        self.initial_conditions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # [x, y, z, vx, vy, vz]
        self.mass = 1.0  # Assume mass = 1 for simplicity, can be adjusted if needed

    def add_force(self, force_function):
        """Add a 3D force function to the list of forces. Each force function must take time, position, and velocity as arguments and return a 3D force vector."""
        self.forces.append(force_function)

    def set_initial_conditions(self, position, velocity):
        """Set the initial conditions for the simulation. Position and velocity are 3D vectors."""
        self.initial_conditions = position + velocity

    def set_mass(self, mass):
        """Set the mass of the object."""
        self.mass = mass

    def _equations_of_motion(self, t, y):
        """Defines the equations of motion for the solver in 3D. y is a vector [x, y, z, vx, vy, vz]."""
        position = y[:3]
        velocity = y[3:]
        net_force = np.sum([force(t, position, velocity) for force in self.forces], axis=0)
        acceleration = net_force / self.mass
        return np.concatenate((velocity, acceleration))  # Return derivatives as a single flat array

    def solve_motion(self, t_span, time_step=0.01):
        """Solve the motion of the object over the given time span in 3D."""
        t_eval = np.arange(t_span[0], t_span[1], time_step)
        solution = solve_ivp(self._equations_of_motion, t_span, self.initial_conditions, method='DOP853', t_eval=t_eval)
        # Split the solution into position and velocity components
        position = solution.y[:3]
        velocity = solution.y[3:]
        return solution.t, position, velocity  # Return time, position, and velocity arrays as 3D vectors



if __name__ == '__main__':

    # Define the force function for a simple harmonic oscillator in 3D
    def simple_harmonic_oscillator(t, position, velocity):
        k = 1.0  # Spring constant
        return [-k * position[0], -k * position[1], -k * position[2]]

    # Create a NewtonSolver object for a 3D simple harmonic oscillator
    solver = NewtonSolverIVP3D()
    solver.add_force(simple_harmonic_oscillator)  # Add the force function
    solver.set_initial_conditions([1.0, 0.0, 0.0], [1.0, 1.0, 0.0])  # Set initial conditions
    solver.set_mass(1.0)  # Set
    t, position, velocity = solver.solve_motion([0, 30], time_step=0.01)


    # Plot 2D case
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(position[0], position[1])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()

