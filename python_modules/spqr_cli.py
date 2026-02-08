import json
import pprint

class SPQRSimple:
    def __init__(self):
        self.spqr_manager = SPQRManager()

    def run(self):
        self.spqr_manager.run()

    def list_attack_types(self):
        return self.spqr_manager.list_attack_types()

class SPQRManager:
    def __init__(self):
        self.attacks = []
        self.spqr_manager = self.run()

    def run(self):
        #Populate attacks list from json config
        with open("./config/config.json") as file :
            data = json.load(file)
            data = data["traffic_patterns"].keys()
            data = list(data)
            self.attacks = data

    def list_attack_types(self):
        return self.attacks

        
