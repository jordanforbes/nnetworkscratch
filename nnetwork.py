#every neuron has a unique connection to every other neuron

inputs = [1,2,3]
weights = [0.2,0.8,-0.5]
bias = 2

#first step for a neuron: add up all the inputs * the weights, + bias 

def inWt(i):
    return inputs[i]*weights[i]

output = inWt(0)+inWt(1)+inWt(2) + bias
print(output)

#selected a single neuron from network 
#neuron had 3 inputs to it 
#each input has its own weight 
#each neuron has one bias