# A number of medical equation functions for use with python programming


def bmi_calc (w, h):
    bmi = w / h**2
    return bmi

def lbm_calc(g, w, h):
    if g == 'm':
        lbm = 1.1*w-128*(w/h)**2
    elif g == 'f':
        lbm = 1.07*w-148*(w/h)**2
    return lbm

def ibw_calc():
    pass

def ebv_calc():
    pass

def abl_calc():
    pass    

def map_calc():
    pass

def co_calc():
    pass

def ci_calc():
    pass

def sv_calc():
    pass    

def svr_calc():
    pass

def svri_calc():
    pass