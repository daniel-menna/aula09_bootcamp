from utils_log import log_decorator

@log_decorator
def somar(x,y) :
    return x + y

somar(2,"3")
