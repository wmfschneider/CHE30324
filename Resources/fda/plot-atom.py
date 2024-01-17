import matplotlib.pyplot as plt
import numpy as np

# Lets open the file in read mode
with open('./Resources/Ar.dmp', 'r') as f:

    # Reading all the lines in the file
    # Each line is stored as an element of a list
    lines = f.readlines()

    # First we read the grid points and the total charge densities
    grid_points = []
    total_charge_densities = []

    for line in lines[3:303]:

        # Each is a string with two columns
        grid_point, tot_charge_density = line.split()

        # We need to convert each line to a float add it to our lists
        grid_points.append(float(grid_point))
        total_charge_densities.append(float(tot_charge_density))
    
    # Now for the 1s orbital
    one_s = []
    one_s = [float(x) for x in lines[304:604]]

    two_s = []
    two_s = [float(x) for x in lines[605:905]]

    two_p = []
    two_p = [float(x) for x in lines[906:1206]]

    three_s = []
    three_s = [float(x) for x in lines[1207:1507]]

    three_p = []
    three_p = [float(x) for x in lines[1508:1808]]
#    for x in lines[304:604]:
#        one_s_charge_density.append(float(x))
 

plt.figure()
#plt.semilogx(grid_points, total_charge_densities)
plt.plot(grid_points, total_charge_densities)
plt.xlabel('Grid Points')
plt.ylabel('Charge Density')
plt.title('Overall')
plt.savefig('./Images/Ar-overall-charge-density.png')

plt.figure()
plt.plot(grid_points, one_s,label='1s')
plt.plot(grid_points, two_s,label='2s')
plt.plot(grid_points, two_p,label='2p')
plt.plot(grid_points, three_s,label='3s')
plt.plot(grid_points, three_p,label='3p')
plt.legend()
plt.xlim(0,6)

plt.xlabel('Distance (bohr)')
plt.ylabel('Wavefunction rR(r)')
plt.title('Ar radial wavefunctions')
plt.savefig('images/Ar-wave-functions.png')
