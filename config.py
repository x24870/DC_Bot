import configparser

conf = configparser.ConfigParser()
conf.read("conf")

if __name__ == "__main__":
    print(conf.sections())