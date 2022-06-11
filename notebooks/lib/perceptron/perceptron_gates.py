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
        perceptron_gates = PerceptronGates()
    
    def visualize_and_gate(self):
        
        
        return