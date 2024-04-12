from loguru import logger

logger.add("meu_app.log")

def somar(x,y) :
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x + y

somar(2,"3")
