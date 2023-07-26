from math import pi

# Q = (k*A/x)*(Tf-Ti)                 (linear heat conduction)
# Q = ((k*2pi*x)/ln(r2/r1))*(Tf-Ti)   (radial heat conduction)
# Q = h*A*(Tf-Ti)                     (convective heat transfer)

# Rtot = R1 + R2 + R3                 (total resistance)
# R1^-1  = h*2*pi*r*l                 (convection off probe)
# R2^-1  = (k*2*pi*x)/ln(r2/r1)       (radial heat transfer through wall)
# R3^-1  = ((Ra**-1) + (Rb**-1))**-1  (branch combination)
# Ra^-1  = Ra1 + Ra2 + Ra3            (branch A: wire to R2)
# Rb^-1  = (k*2*pi*x)/ln(r2/r1)       (branch B: epoxy to R2)
# Ra1^-1 = k*pi*(r**2)/x              (conduction through wire)
# Ra2^-1 = (k*2*pi*x)/ln(r2/r1)       (radial heat transfer through plastic)
# Ra3^-1 = (k*2*pi*x)/ln(r2/r1)       (radial heat transfer through epoxy)

def Rtotal(R1, R2, R3):
    Rtot = R1 + R2 + R3
    return Rtot

def R1(h, r, l):
    R1 = (h*2*pi*r*l)**-1
    return R1

def R2(k, r1, r2, l):
    R2 = ((k*2*pi*x)/ln(r2/r1))**-1
    return R2

def R3(Ra, Rb):
    R3 = ((Ra**-1) + (Rb**-1))**-1
    return R3

def Ra(Ra1, Ra2, Ra3):
    Ra = Ra1 + Ra2 + Ra3
    return Ra

def Rb(k, r1, r2, l):
    Rb = ((k*2*pi*x)/ln(r2/r1))**-1
    return Rb

def Ra1(k, r, l):
    Ra1 = k*pi*(r**2)/l
    return Ra1

def Ra2(k, r1, r2, l):
    Ra2 = ((k*2*pi*x)/ln(r2/r1))**-1
    return Ra2

def Ra3(k, r1, r2, l):
    Ra3 = ((k*2*pi*x)/ln(r2/r1))**-1
    return Ra3



