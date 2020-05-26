import numpy as np
def retrieve_price(csp,rfr,ep,upvalue,downvalue):
    Rate=float(1)+float(rfr)
    upper_bound=float(upvalue)/float(csp)
    lower_bound=float(downvalue)/float(csp)
    upper_call=max(np.multiply(upper_bound,csp)-ep,float(0))
    lower_call=max(np.multiply(lower_bound,csp)-ep,float(0))
    delta=(upper_call-lower_call)/(np.multiply(csp,(upper_bound-lower_bound)))
    borrow_amount=(np.multiply(lower_bound,upper_call)-np.multiply(upper_bound,lower_call))/np.multiply((upper_bound-lower_bound),Rate)
    call_value=np.multiply(delta,csp)-borrow_amount
    return(call_value)
