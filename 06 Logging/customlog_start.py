# Demonstrate how to customize logging output

import logging

extData = {'user' : "nsen@gmail.com"}

# TODO: add another function to log from

# def newFunc():
#     logging.debug("This is debug-level log", extra=extData)

def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    frmtStr = "%(asctime)s: User: %(user)s %(filename)s %(funcName)s %(lineno)d: %(message)s"
    dtfrmt = "%d/%m/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        filemode='a',
                        format=frmtStr,
                        datefmt=dtfrmt)

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)

    # newFunc()


if __name__ == "__main__":
    main()
