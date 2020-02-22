from opcua import ua, Server
import time
import sys
sys.path.insert(0, "..")


if __name__ == "__main__":

    # set up server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4080/freeopcua/server/")

    # set up namespace
    uri = "http://tylermyracle.com"
    idx = server.register_namespace(uri)

    # get Objects node where all nodes will go under
    objects = server.get_objects_node()

    # populate the address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 0.0)
    myvar.set_writable()

    server.start()

    try:
        count = 0
        while True:
            time.sleep(1)
            count += 1
            myvar.set_value(count)
    finally:
        server.stop()
