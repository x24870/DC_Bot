import configparser

conf = configparser.ConfigParser()
conf.read("conf")

if __name__ == "__main__":
    print(conf.sections())
    for sec in conf.sections():
        print(sec)
        for key in conf[sec]:
            print(key, conf[sec][key])