import time

class Policy:
    def _init_(self):
        self.policy = {"default": {"action": "allow"}}

    def get_policy(self):
        return self.policy

    def update_policy(self, new_policy):
        self.policy = new_policy

class LightweightPolicyUpdater:
    def _init_(self, policy, interval=60):
        self.policy = policy
        self.interval = interval

    def start(self):
        while True:
            new_policy = self.get_policy_from_server()  # Fetch policy from server
            self.policy.update_policy(new_policy)  # Update policy
            time.sleep(self.interval)  # Sleep for interval seconds

    def get_policy_from_server(self):
        # Code to fetch policy from server goes here
        return {"default": {"action": "deny"}}

if _name_ == "_main_":
    policy = Policy()
    updater = LightweightPolicyUpdater(policy)
    updater.start()
