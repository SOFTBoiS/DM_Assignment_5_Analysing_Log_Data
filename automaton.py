class Automaton:
    START_STATE = 'q0'
    END_STATE = 'q3'
    instances = {}

    def create_instance(self, instance_id):
        self.instances[instance_id] = self.START_STATE

    # q0 = before login
    # q1 = logged in (maybe selected and bought item)
    # q2 = selected item
    # q3 = logged out
    # A(B|BC)*D
    def make_action(self, instance_id, action):
        if not self.instance_is_running(instance_id) and action == 'A':
            self.create_instance(instance_id)

        instance_state = self.instances[instance_id]
        if instance_state == 'q0':
            if action == 'A':
                self.instances[instance_id] = 'q1'
            else:
                raise Exception('Invalid action')
        elif instance_state == 'q1':
            if action == 'B':
                self.instances[instance_id] = 'q2'
            elif action == 'D':
                del self.instances[instance_id]
            else:
                raise Exception('Invalid action')
        elif instance_state == 'q2':
            if action == 'C':
                self.instances[instance_id] = 'q1'
            elif action == 'D':
                del self.instances[instance_id]
            elif action != 'B':
                raise Exception('Invalid action')
        elif instance_state == 'q3':
            del self.instances[instance_id]
            raise Exception('Invalid action for logged out')
        else:
            raise Exception('Invalid state')

    def instance_is_running(self, instance_id):
        return instance_id in self.instances

    def number_of_instances(self):
        return len(self.instances)
