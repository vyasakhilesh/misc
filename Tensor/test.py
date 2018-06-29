import math
import numpy as np

def sigmoid(values):
    tmp = np.zeros(len(values))
    for i in range(0, len(values)):
        if (values[i] > 100):
            x = 1.0
        elif (values[i] < -100):
            x = -1.0
        else:
            x = (1.0/(1+math.exp(-values[i])))

        np.put(tmp, i,  x)

    return tmp

def network_activations(w1,w2,x):
    x = np.insert(x, 0, 1.0)
    net1 = np.dot(w1, x.transpose())
    a1 = sigmoid(net1)
    #print a1
    a1 = np.insert(a1, 0, 1.0)
    net2 = np.dot(w2, a1.transpose())
    a1 = np.delete(a1, 0)
    a2 = sigmoid(net2)
    #print (a1, a2)
    #print a2

    return (a1,a2)

def predict(w1,w2,x):
    (a1, a2) = network_activations(w1, w2, x)
    print a2
    num = 0
    max = a2.item(0)
    for i in range(0, a2.size):
        if(a2.item(i) > max):
            num = i
            max = a2.item(i)
    return num

def gradient_for_an_instance(w1,w2,x,y):

    return (grad_w1, grad_w2)




x1 = np.array([-0.5,1.2,-0.5])
x2 = np.array([0.5,0.3,0.2])

# Note that the first column contains bias weights therefore, the number of columns in
# the w1 matrix is one more than the length of the vector, and the number of columns in
# the w2 matrix is one more than the number of hidden units
w1 = np.array( [ [  0.1,  0.1, -0.2,  0.3 ], \
                 [ -0.1,  0.2,  0.5, -0.8 ], ] )
w2 = np.array( [ [  0.1,  0.5, -0.3 ], \
                 [ -0.1, -0.2,  0.7 ] ])
print(predict(w1,w2,x1))
print(predict(w1,w2,x2))

MINIBATCH_SIZE = 100
NUM_HIDDEN_UNITS = 100
NUM_ATTRIBUTES = len(mnist.train.images[0])
NUM_CLASSES = len(mnist.train.labels[0])
np.random.seed(42)
w1 = (np.random.random((NUM_HIDDEN_UNITS, NUM_ATTRIBUTES + 1))) - 0.5
w2 = (np.random.random((NUM_CLASSES, NUM_HIDDEN_UNITS + 1))) - 0.5
eps = 0.5

for iteration in range(10000):
    grad_w1all = np.zeros((NUM_HIDDEN_UNITS, NUM_ATTRIBUTES + 1))
    grad_w2all = np.zeros((NUM_CLASSES, NUM_HIDDEN_UNITS + 1))
    train_images, labels = mnist.train.next_batch(MINIBATCH_SIZE)
    for instance in range(MINIBATCH_SIZE):
        grad_w1, grad_w2 = gradient_for_an_instance( \
            w1, w2, train_images[instance], labels[instance])
        grad_w1all += grad_w1 / MINIBATCH_SIZE
        grad_w2all += grad_w2 / MINIBATCH_SIZE
    w1 += eps * grad_w1all
    w2 += eps * grad_w2all

    if iteration % 100 == 0:
        print(iteration, " out of 10000 finished")