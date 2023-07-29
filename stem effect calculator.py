from math import pi

# VARIABLES

# geometry
probe_diameter      = 1
probe_wall          = 1
probe_length        = 1
wire_diameter       = 1
wire_wall           = 1
wire_length_norm    = 1
wire_length_exposed = 1
coat_thickness      = 1
sensor_diameter     = 1
epoxy_length        = 1

# material characteristics
probe_conductivity  = 1
epoxy_conductivity  = 1
wire_conductivity   = 1
coat_conductivity   = 1

# system characteristics
temperature_delta   = 1
convection_coeff    = 1

# SYSTEM OF EQUATIONS

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

Ra1 = Ra1(k=wire_conductivity, r=wire_diameter/2, l=wire_length_norm)
Ra2 = Ra2(k=coat_conductivity, r1=wire_diameter/2, r2=coat_thickness+(wire_diameter/2), l=wire_length_norm)
Ra3 = Ra3(k=epoxy_conductivity, r1=coat_thickness+(wire_diameter/2), r2=(probe_diameter/2)-probe_wall, l=epoxy_length)

Ra = Ra(Ra1=Ra1, Ra2=Ra2, Ra3=Ra3)
Rb = Rb(k=epoxy_conductivity, r1=sensor_diameter, r2=(probe_diameter/2)-probe_wall, l=epoxy_length)

R3 = R3(Ra=Ra, Rb=Rb)
R2 = R2(k=probe_conductivity, r1=(probe_diameter/2)-probe_wall, r2=probe_diameter/2, l=probe_length)
R1 = R1(h=convection_coeff, r=probe_diameter/2, l=probe_length)

Rtot = Rtotal(R1=R1, R2=R2, R3=R3)

HT_Rate = Rtot**-1