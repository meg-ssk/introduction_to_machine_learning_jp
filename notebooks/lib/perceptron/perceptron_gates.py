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
        # make x1 (horizontal) array 
        self.horizontal_min, self.horizontal_max, self.horizontal_step = -0.5, 1.75, 0.1 
        self.x1 = np.arange(self.horizontal_min, self.horizontal_max, self.horizontal_step)
        
        self.floor_line = self.x1 * 0 - 1
        self.ceil_line = self.x1 * 0 + 2
        
        
        self.lattice_points_x, self.lattice_points_y = np.meshgrid(np.arange(2), np.arange(2))
        
    def visualize_single_perceptron_gate(self, weights, bias):
        # calculate slope and intercept
        slope = -(weights[0] / weights[1])
        intercept = -(bias / weights[1])
        
        # make x2 (vertical) array
        x2 = slope * self.x1 + intercept
        
        # equalise the aspect ratio
        plt.axes().set_aspect('equal')
        
        # show axes
        plt.axhline(0, linewidth=2, color="black")
        plt.axvline(0, linewidth=2, color="black")
        
        # set horizontal/verticallimits
        plt.xlim([-0.25, 1.5])
        plt.ylim([-0.25, 1.5])
        
        plt.plot(self.x1, x2)
        plt.scatter(self.lattice_points_x, self.lattice_points_y, s=100)
        
        if weights[1] > 0:
            upper_color, under_color = "b", "r"
        else:
            upper_color, under_color = "r", "b"
            
        plt.fill_between(x= self.x1, y1= x2, y2 = self.ceil_line, color= upper_color, alpha= 0.2)
        plt.fill_between(x= self.x1, y1= x2, y2 = self.floor_line, color= under_color, alpha= 0.2)
        plt.show()
        
        return 
    
    def visualize_two_layer_perceptron_gate(self, weights1, weights2, bias1, bias2):
        # to be modified
        
        # calculate slope and intercept
        slope1, slope2 = -(weights1[0] / weights1[1]), -(weights2[0] / weights2[1])
        intercept1, intercept2 = -(bias1 / weights1[1]), -(bias2 / weights2[1]) 
        print(intercept1, intercept2)
        
        # make two vertical array
        y1, y2 = slope1 * self.x1 + intercept1, slope2 * self.x1 + intercept2
        
        # equalise the aspect ratio
        plt.axes().set_aspect('equal')
        
        # show axes
        plt.axhline(0, linewidth=2, color="black")
        plt.axvline(0, linewidth=2, color="black")
        
        # set horizontal/verticallimits
        plt.xlim([-0.25, 1.5])
        plt.ylim([-0.25, 1.5])
        
        plt.plot(self.x1, y1, "c")
        plt.plot(self.x1, y2, "c")
        plt.scatter(self.lattice_points_x, self.lattice_points_y, s=100)
        
            
        plt.fill_between(x= self.x1, y1= y1, y2 = self.ceil_line, color= "r", alpha= 0.2)
        plt.fill_between(x= self.x1, y1= y1, y2 = y2, color= "b", alpha= 0.2)
        plt.fill_between(x= self.x1, y1= y2, y2 = self.floor_line, color= "r", alpha= 0.2)
        plt.show()
        
        return 
    
    def visualize_and_gate(self):
        weights, bias = self.perceptron_gates.weights_and_gate, self.perceptron_gates.bias_and_gate
        
        # visualize perceptron by linear activate function
        self.visualize_single_perceptron_gate(weights, bias)
        return
    
    def visualize_or_gate(self):
        weights, bias = self.perceptron_gates.weights_or_gate, self.perceptron_gates.bias_or_gate
        
        # visualize perceptron by linear activate function
        self.visualize_single_perceptron_gate(weights, bias)
        return
    
    def visualize_nand_gate(self):
        weights, bias = -self.perceptron_gates.weights_and_gate, -self.perceptron_gates.bias_and_gate
        
        # visualize perceptron by linear activate function
        self.visualize_single_perceptron_gate(weights, bias)
        return
    
    def visualize_xor_gate(self):
        weights1, bias1 = -self.perceptron_gates.weights_and_gate, -self.perceptron_gates.bias_and_gate
        weights2, bias2 = self.perceptron_gates.weights_or_gate, self.perceptron_gates.bias_or_gate
        
        # visualize perceptron by linear activate function
        self.visualize_two_layer_perceptron_gate(weights1, weights2, bias1, bias2)
        return
    