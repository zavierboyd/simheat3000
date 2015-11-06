# v2.0
from __future__ import division
from matrix_class import *
import numpy as np
import numpy.linalg as la

def setup():
    # init material temperatures K
    wall_Temp = 18.0
    inside_Temp = 20.0
    window_Temp = 13.0
    outside_Temp = 12.0

    # init thermal masses J/K
    wall_mass = 278666.0 + (2 / 3)
    inside_mass = 45600.0
    window_mass = 47040.0
    outside_mass = 10.0**9

    # init interfaces W/K
    wall_inside_conduction = 269.2656
    inside_window_conduction = 40.65
    window_outside_conduction = 90.90909091

    # init joules
    wall_Joules = wall_Temp * wall_mass
    inside_Joules = inside_Temp * inside_mass
    window_Joules = window_Temp * window_mass
    outside_Joules = outside_Temp * outside_mass
    # init time
    time = 0.0
    dt = 60
#####################################################################################
    # class1
    # matrices
    wam = MatrixImpN([[0.0, wall_inside_conduction, 0.0],
                      [wall_inside_conduction, 0.0, inside_window_conduction],
                      [0.0, inside_window_conduction, 0.0]])

    mass = MatrixImpN([[1/wall_mass], [1/inside_mass], [1/window_mass]]).diagonal()

    I = MatrixImpN.identityMatrix(3)

    neg_c = (wam * MatrixImpN([[-1], [-1], [-1]])).diagonal()

    M = mass * (neg_c + wam) * dt + I
#####################################################################################
    # class 2
    a = MatrixImpN([[1 - wall_inside_conduction * dt * (1 / wall_mass), wall_inside_conduction * dt * (1 / wall_mass), 0.0],
                    [wall_inside_conduction * dt * (1 / inside_mass), 1 - wall_inside_conduction * dt * (1 / inside_mass) - inside_window_conduction * dt * (1 / inside_mass), inside_window_conduction * dt * (1 / inside_mass)],
                    [0.0, inside_window_conduction * dt * (1 / window_mass), 1 - inside_window_conduction * dt * (1 / window_mass)]])
#####################################################################################
    # class 3
    print a2 == a

    b = MatrixImpN([[wall_Temp], [inside_Temp], [window_Temp]])
    b2 = MatrixImpN([[wall_Temp], [inside_Temp], [window_Temp]])

    # simulation
    for i in range(60):
        b2 = a2 * b2
        b = a * b
        print
        print
        print b
        print b2
        # calculate energy flow part 1 Watts
        wall_to_inside_Watts = wall_inside_conduction * wall_Temp
        inside_to_wall_Watts = wall_inside_conduction * inside_Temp
        inside_to_window_Watts = inside_window_conduction * inside_Temp
        window_to_inside_Watts = inside_window_conduction * window_Temp
        # window_to_outside_Watts = window_outside_conduction * window_Temp
        # outside_to_window_Watts = window_outside_conduction * outside_Temp
        ##################################################################
        # calculate energy flow part 2 Joules
        wall_to_inside_Joules = wall_to_inside_Watts * dt
        inside_to_wall_Joules = inside_to_wall_Watts * dt
        inside_to_window_Joules = inside_to_window_Watts * dt
        window_to_inside_Joules = window_to_inside_Watts * dt
        # window_to_outside_Joules = window_to_outside_Watts * dt
        # outside_to_window_Joules = outside_to_window_Watts * dt
        #######################################################
        # calculate joules in each mass
        wall_Joules += inside_to_wall_Joules - wall_to_inside_Joules
        # inside_Joules += wall_to_inside_Joules - inside_to_wall_Joules
        inside_Joules += wall_to_inside_Joules + window_to_inside_Joules - inside_to_wall_Joules - inside_to_window_Joules
        window_Joules += inside_to_window_Joules - window_to_inside_Joules
        # window_Joules += inside_to_window_Joules + outside_to_window_Joules\
        # - window_to_inside_Joules - window_to_outside_Joules
        # outside_Joules += window_to_outside_Joules - outside_to_window_Joules
        ####################################################################################################################
        # calculate new temperatures
        wall_temp_test = wall_Temp * (1 - wall_inside_conduction * dt * (1 / wall_mass)) + \
            inside_Temp * (wall_inside_conduction * dt * (1 / wall_mass))

        # wall_Temp * (wall_inside_conduction * dt) + inside_Temp * (-wall_inside_conduction * dt)
        wall_Temp = wall_Joules * (1 / wall_mass)
        print wall_temp_test, wall_Temp
        inside_Temp = inside_Joules * (1 / inside_mass)
        window_Temp = window_Joules * (1 / window_mass)
        outside_Temp = outside_Joules * (1 / outside_mass)
        ##################################################
        print "{wall_Temp:4.2f} K Wall".format(wall_Temp=wall_Temp),
        print "{inside_Temp:4.2f} K Inside".format(inside_Temp=inside_Temp),
        print "{window_Temp:4.2f} K Window".format(window_Temp=window_Temp),
        # print "{outside_Temp:4.2f} K Outside".format(outside_Temp=outside_Temp)
        time += dt


    print time, "Time t"


class House():
    """A thermal model of the house"""
    def __init__(self, wam, thermal_mass):
        self.thermal_mass = MatrixImpN(thermal_mass).diagonal()  # J/Kg*K --> J/K
        self.wam = MatrixImpN(wam)  # W/m^2*K --> W/K
        self.npwam = np.array(wam)
        self.npthermal_mass = np.diagflat(np.array(thermal_mass))
        print self.wam,"super wam"

    def matrix_simulation(self, temp, dt, t):
        size = self.wam.width
        time = 0
        I = MatrixImpN.identityMatrix(size)
        neg_c = (self.wam * MatrixImpN([[-1]]*size)).diagonal()
        M = self.thermal_mass * (self.wam + neg_c)
        print M, "Tdot"
        M = M * dt + I
        print self.thermal_mass,"thermal mass"
        print self.wam, "wam"
        print neg_c, "other wam"
        print dt, "dt"
        print I, "I"
        print M, "M"
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

        dt = dt
        temp = MatrixImpN(temp)  # K
        #temps = [x for x in temp.matrix]
        temps = list(temp.matrix)
        # finish matrix simulation
        hour = 60*60*3
        idx = 0
        qhour = 2
        while time < t:
            tempn = M * temp
            temp = tempn
            if qhour >= 2:
                for i in range(tempn.height):
                    temps[i].append(temp.matrix[i][0])
                    qhour = 0
            time += dt
            qhour += dt

        return temps

    def matrix_simulstionnp(self, temp, dt, t, outtemps):
        size = len(self.npwam[0])
        time = 0
        dt = dt
        I = np.diagflat(np.array([[1]*size]))
        neg_c = np.diagflat((self.npwam.dot(np.array([[-1]]*size))))
        M = self.npthermal_mass.dot(self.npwam + neg_c).dot(dt) + I
        print M, "Tdot"
        temp = np.array(temp)  # K
        #temps = [x for x in temp.matrix]
        temps = [[cell for cell in row] for row in temp]
        # finish matrix simulation
        hour = 60*60*3
        idx = 0
        qhour = 15*60
        while time < t:
            if hour == (60*60*3):
                temp[3][0] = outtemps[idx][0]
                hour = 0
                idx += 1
            tempn = M.dot(temp)
            temp = tempn
            if qhour >= 15*60:
                for i in range(len(tempn)):
                    temps[i].append(temp[i][0])
                    qhour = 0
            time += dt
            hour += dt
            qhour += dt

        return temps

    def matrix_simulstionnppower(self, temp, dt, t, outtemps):
        size = len(self.npwam[0])
        time = 0
        dt = dt
        kWhpJ = 3.6*(10**6)
        I = np.diagflat(np.array([[1]*size]))
        neg_c = np.diagflat((self.npwam.dot(np.array([[-1]]*size))))
        M = self.npthermal_mass.dot(self.npwam + neg_c).dot(dt) + I
        print M, "Tdot"
        bomb = np.array([[((2000 * 900)*self.npthermal_mass[0][0])], [0], [0]])
        print "energy", 2000*900
        print "thermal capacity", self.npthermal_mass[0][0]
        print "bomb", bomb
        M900 = (la.matrix_power(M, 900))
        temp = np.array(temp)  # K
        print temp
        temps = [[cell for cell in row] for row in temp]
        hour = 60*60*3
        idx = 0
        bombcount = 0
        while time < t:
            if hour == (60*60*3):
                temp[2][0] = outtemps[idx][0]
                hour = 0
                idx += 1
            tempn = M900.dot(temp)
            temp = tempn
            for i in range(len(tempn)):
                temps[i].append(temp[i][0])
            if temp[0][0] < 18:
                temp = temp+bomb
                bombcount += 1
            time += 900
            hour += 900
        print bombcount
        J = 2000*900*bombcount
        kWh = J/kWhpJ
        money = kWh*0.27
        print kWh, "kWh"
        return temps, kWh, money
# print House([[0, 269.2656], [269.2656, 0]], [[1/278666.667], [1/45600.0]]).matrix_simulation([[17.0], [20.0]], 1, 1)