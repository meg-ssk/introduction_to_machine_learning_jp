import numpy as np
import matplotlib.pyplot as plt

class PerceptronGates:
    def __init__(self):
        self.weights_and_gate = np.array([0.5, 0.5])
        self.bias_and_gate = -0.7
        
        self.weights_or_gate = np.array([0.5, 0.5])
        self.bias_or_gate = -0.2
    
    def perceptron_activation_function(self, inputs, weights, bias):        
        if np.dot(inputs, weights) + bias <= 0:
            return 0
        else:
            return 1
    
    def and_gate(self, input1, input2):
        inputs = np.array([input1, input2])
        weights = self.weights_and_gate
        bias = self.bias_and_gate
        
        return self.perceptron_activation_function(inputs, weights, bias)
    
    def or_gate(self, input1, input2):
        inputs = np.array([input1, input2])
        weights = self.weights_or_gate
        bias = self.bias_or_gate
        
        return self.perceptron_activation_function(inputs, weights, bias)
    
    def nand_gate(self, input1, input2):
        inputs = np.array([input1, input2])
        weights = -self.weights_and_gate
        bias = -self.bias_and_gate
        
        return self.perceptron_activation_function(inputs, weights, bias)
    
    def xor_gate(self, input1, input2):
        signal1 = self.nand_gate(input1, input2)
        signal2 = self.or_gate(input1, input2)
        return self.and_gate(signal1, signal2)

class VisualizePerceptron: 
    def __init__(self):
        self.perceptron_gates = PerceptronGates()
        self.lattice_points_x, self.lattice_points_y = np.meshgrid(np.arange(2), np.arange(2))
    
    def visualize_and_gate(self):
        # make x1 (hotizontal) array
        horizontal_min, horizontal_max, horizontal_step = -0.5, 1.75, 0.1        
        x1 = np.arange(horizontal_min, horizontal_max, horizontal_step)
        
        # calculate slope and intercept
        slope = -(self.perceptron_gates.weights_and_gate[0] / self.perceptron_gates.weights_and_gate[0])
        intercept = -(self.perceptron_gates.bias_and_gate / self.perceptron_gates.weights_and_gate[0])
        
        # make x2 (vertical) array
        x2 = slope * x1 + intercept
        
        # equalise the aspect ratio
        plt.axes().set_aspect('equal')
        
        # show axes
        plt.axhline(0, linewidth=2, color="gray")
        plt.axvline(0, linewidth=2, color="gray")
        
        # set horizontal/verticallimits
        plt.xlim([-0.25, 1.5])
        plt.ylim([-0.25, 1.5])
        
        plt.plot(x1, x2)
        plt.scatter(self.lattice_points_x, self.lattice_points_y)
        plt.show()
        
        return