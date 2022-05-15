##matrix, zip, vector
inputs = [1, 2, 3, 2.5] #vector

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]
           ] #matrix of vectors

biases = [2, 3, 0.5]

#weights and biases are "knobs" used to adjust outputs to reach a certain value. They're not necessary but extremely helpful 

layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases): #zip combines 2 lists into a list of list element-wise
    neuron_output = 0 
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight 
    neuron_output += neuron_bias 
    layer_outputs.append(neuron_output)
    
print(layer_outputs)



