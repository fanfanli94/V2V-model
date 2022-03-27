import numpy as np


class Vehicle:
    def __init__(self, config={}):
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

        # Calculate properties
        self.init_properties()

    def set_default_config(self):
        self.l = 4
        self.s0 = 4
        #self.T = 1
        self.T = 1.1
        self.v_max = 16.6
        #self.a_max = 1.44
        self.a_max = 1
        #self.b_max = 4.61
        self.b_max = 2
        
        self.info=0

        self.path = []
        self.current_road_index = 0

        self.x = 0
        self.v = self.v_max
        self.a = 0
        self.stopped = False

    def init_properties(self):
        self.sqrt_ab = 2*np.sqrt(self.a_max*self.b_max)
        self._v_max = self.v_max
        self.info=self.info

    def update(self, lead1, lead2, lead3, lead4, lead5, dt):
        # Update position and velocity
        if self.v + self.a*dt < 0:
            self.x -= 1/2*self.v*self.v/self.a
            self.v = 0
        else:
            self.v += self.a*dt
            self.x += self.v*dt + self.a*dt*dt/2

        # Update acceleration
        alpha = 0
        if lead1 & lead2 & lead3 & lead4 & lead5:
            delta_x1 = lead1.x - self.x - lead1.l
            delta_v1 = self.v - lead1.v

            alpha1 = (self.s0 + max(0, self.T*self.v + delta_v1*self.v/self.sqrt_ab)) / delta_x1
            alpha2 = (self.s0 + max(0, self.T*self.v + delta_v2*self.v/self.sqrt_ab)) / delta_x2
            alpha3 = (self.s0 + max(0, self.T*self.v + delta_v3*self.v/self.sqrt_ab)) / delta_x3
            alpha4 = (self.s0 + max(0, self.T*self.v + delta_v4*self.v/self.sqrt_ab)) / delta_x4
            alpha5 = (self.s0 + max(0, self.T*self.v + delta_v5*self.v/self.sqrt_ab)) / delta_x5
            alpha = alpha1+alpha2+alpha3+alpha4+alpha5

        self.a = self.a_max * (1-(self.v/self.v_max)**4 - (alpha)**2)

        if self.stopped:
            self.a = -self.b_max*self.v/self.v_max

    def stop(self):
        self.stopped = True

    def unstop(self):
        self.stopped = False

    def slow(self, v):
        self.v_max = v

    def unslow(self):
        self.v_max = self._v_max
    
    def periodicinfo(self,lead1,r):
        
        return 
        
