import numpy as np

class PerceptronGates:
    @classmethod
    def activation_function_unit_step(cls, inputs, weights, bias):        
        if np.dot(inputs, weights) + bias <= 0:
            return 0
        else:
            return 1
    
    @classmethod
    def and_gate(cls, input1, input2):
        inputs = np.array([input1, input2])
        weights = np.array([0.5, 0.5])
        bias = -0.7
        
        return cls.activation_function_unit_step(inputs, weights, bias)
        