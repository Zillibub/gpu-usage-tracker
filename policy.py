import yaml
from datetime import datetime


class Policy:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(
                Policy, cls
            ).__new__(cls)
            with open('policy-config.yml', 'r') as f:
                params = yaml.load(f)
            cls.__instance.params = params
            cls.__instance.time = datetime.now()

        return cls.__instance

    def _update_time(self):
        current_time = datetime.now()
        interval = current_time - self.time
        self.time = current_time
        return interval

    def _get_message(self, interval):
        for t in self.params:
            if interval > t:
                return self.params[t]
        return None

    def check(self):
        interval = self._update_time()
        return self._get_message(interval)
