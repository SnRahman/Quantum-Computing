from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_bloch_multivector, plot_state_qsphere
from qiskit.quantum_info import Statevector
from IPython.display import display
import ipywidgets as widgets
import matplotlib.pyplot as plt

# Create a simple UI with dropdowns for gate selection
gate_dropdown = widgets.Dropdown(
    options=['Hadamard (H)', 'Pauli-X (X)', 'Pauli-Y (Y)', 'Pauli-Z (Z)'],
    value='Hadamard (H)',
    description='Gate:',
)

# Output widget to display visualization
output = widgets.Output()

# Define a function to apply the gate and display results
def on_gate_change(change):
    with output:
        output.clear_output()
        
        gate = change['new']
        qc = QuantumCircuit(1)

        # Apply selected gate
        if gate == 'Hadamard (H)':
            qc.h(0)
        elif gate == 'Pauli-X (X)':
            qc.x(0)
        elif gate == 'Pauli-Y (Y)':
            qc.y(0)
        elif gate == 'Pauli-Z (Z)':
            qc.z(0)

        # Simulate using statevector
        state = Statevector.from_instruction(qc)

        # Show Bloch sphere and Qsphere
        fig1 = plot_bloch_multivector(state)
        fig2 = plot_state_qsphere(state)
        display(fig1)
        display(fig2)
        plt.show()

# Run once at start
on_gate_change({'new': gate_dropdown.value})

# Set up callback
gate_dropdown.observe(on_gate_change, names='value')

# Display UI
display(gate_dropdown, output)
