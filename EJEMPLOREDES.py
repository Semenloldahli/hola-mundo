import numpy as np   # Importamos la librería NumPy y le asignamos el alias 'np'

def sigmoid(x):      # Definimos una función 'sigmoid' que toma un argumento 'x'
    return 1 / (1 + np.exp(-x))   # Retorna el resultado de la función sigmoid

class NeuralNetwork:    # Definimos una clase 'NeuralNetwork'
    def __init__(self, input_size, hidden_size, output_size):   # Definimos el constructor de la clase
        self.input_size = input_size   # Atributo de la clase: tamaño de entrada
        self.hidden_size = hidden_size   # Atributo de la clase: tamaño de la capa oculta
        self.output_size = output_size   # Atributo de la clase: tamaño de salida
        self.weights1 = np.random.randn(self.input_size, self.hidden_size)   # Matriz de pesos aleatorios entre la entrada y la capa oculta
        self.weights2 = np.random.randn(self.hidden_size, self.output_size)  # Matriz de pesos aleatorios entre la capa oculta y la salida
        
    def forward(self, X):    # Método de la clase: 'forward', que toma un argumento 'X'
        self.z = np.dot(X, self.weights1)   # Producto punto entre la entrada y la matriz de pesos de la primera capa
        self.z2 = sigmoid(self.z)   # Aplicamos la función sigmoid a la salida anterior
        self.z3 = np.dot(self.z2, self.weights2)   # Producto punto entre la capa oculta y la matriz de pesos de la segunda capa
        output = sigmoid(self.z3)   # Aplicamos la función sigmoid a la salida anterior
        return output   # Retornamos el resultado de la propagación hacia adelante

    def sigmoid_derivative(self, x):   # Método de la clase: 'sigmoid_derivative', que toma un argumento 'x'
        return x * (1 - x)   # Calcula la derivada de la función sigmoid
        
    def backward(self, X, y, output):   # Método de la clase: 'backward', que toma tres argumentos 'X', 'y' y 'output'
        self.output_error = y - output   # Error en la capa de salida
        self.output_delta = self.output_error * self.sigmoid_derivative(output)   # Gradiente en la capa de salida
        self.z2_error = self.output_delta.dot(self.weights2.T)   # Error en la capa oculta
        self.z2_delta = self.z2_error * self.sigmoid_derivative(self.z2)   # Gradiente en la capa oculta
        self.weights1 += X.T.dot(self.z2_delta)   # Actualización de los pesos entre la entrada y la capa oculta
        self.weights2 += self.z2.T.dot(self.output_delta)   # Actualización de los pesos entre la capa oculta y la salida

    def train(self, X, y):   # Método de la clase: 'train', que toma dos argumentos 'X' y 'y'
        output = self.forward(X)   # Propagación hacia adelante
        self.backward(X, y, output)   # Propagación hacia atrás

X = np.array([[0, 0, 1], [0, 1,0]])
