from opcua import ua, Server
import time
import random
import sys
import json
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
    mylat = myobj.add_variable(idx, "MyLat", 0.0)
    mylon = myobj.add_variable(idx, "MyLon", 0.0)

    myvar.set_writable()
    mylat.set_writable()
    mylon.set_writable()

    # server.start()

    with open('city-list.json', 'r') as cities:
        cities_dict = json.load(cities)

    try:
        count = 0
        while True:
            time.sleep(2)

            index = random.randint(0, len(cities_dict) - 1)
            city = cities_dict[index]
            name = city["name"]
            country = city["country"]
            latitude = city["coord"]["lat"]
            longitude = city["coord"]["lon"]

            count += 1
            myvar.set_value(count)
            mylat.set_value(latitude)
            mylon.set_value(longitude)
    finally:
        server.stop()
