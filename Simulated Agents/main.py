import simple_agent
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#run a simple aget
geno = np.array([0,0,0,0,10,10])
initial_pos = [7,7 ]
T=150
initial_degrees = 90
two_eyed = [-2.78829298,-0.12068399 ,0.92230641,2.16781307,-3.60323339,-3.99695858]
one_eyed2 = [ 1.22507482,0.0,1.71929014,0.0,-3.79409885,-3.81429009]
one_eyed = [1.80847401,0.0,1.0855534,0.0,3.45234368,3.54548129]
two_eyed_new_compete = [-3.96471108,1.83556632,-2.98767112,2.9698673,-2.62550624,-3.60980797]
two_eyed_long_train = [-0.42594202,2.1830096,0.04005485,-0.40849273,-3.62143105,-3.67551313]
out1  = simple_agent.run(T,initial_pos,initial_degrees,two_eyed_long_train,1)
out2  = simple_agent.run(T,initial_pos,initial_degrees,two_eyed,1)

one_x = [pos for pos in out1[0]]
one_y = [pos for pos in out1[1]]
one_eye_out = [-((one_x[i]*one_x[i])+(one_y[i]*one_y[i])) for i in range(len(out1[0]))]
#two_eye_out = [(pos[0]*pos[0])+(pos[1]*pos[1]) for pos in out2]

two_x = [pos for pos in out2[0]]
two_y = [pos for pos in out2[1]]
two_eye_out = [-((two_x[i]*two_x[i])+(two_y[i]*two_y[i])) for i in range(len(out2[0]))]
print(one_eye_out)
one = plt.plot( one_eye_out, label = 'Long allowed time')
two = plt.plot(two_eye_out, label = 'Short allowed time')
plt.xlabel('time')
plt.ylabel('fitness')
plt.legend()
plt.show()

#[1,0,0,1,1,1]

"""
w_ll = geno[0]; #left motor to left sensor
w_lr = geno[1]; #left motor to right sensor
w_rl = geno[2]; #right motor to left sensor
w_rr = geno[3]; #right motor to right sensor
"""
best = [-2.78829298,-0.12068399 ,0.92230641,2.16781307,-3.60323339,-3.99695858] #2 eyed, pop 3, 200 gen
