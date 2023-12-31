from enum import Enum
from queue import Queue
import math 

modules = {}

class ModuleType(Enum):
    BROADCAST = 0
    FLIPFLOP = 1
    CONJUNCTION = 2
    OFF = 10
    ON = 11
    LOW = 20
    HIGH = 21

class Module:
    def __init__(self, name, modules):
        self.targets = [x.strip() for x in modules.split(",")]
        if name == "broadcaster":
            self.name = name
            self.type = ModuleType.BROADCAST
        else:
            self.name = name[1:]
            if name[0] == "%":
                self.type = ModuleType.FLIPFLOP
                self.state = ModuleType.OFF
            else:
                self.type = ModuleType.CONJUNCTION
                self.inputs = {}
    
    def __str__(self):
        output = self.name 
        if self.type == ModuleType.CONJUNCTION:
            output += "(C): "
            output += "Inputs: " 
            for i in self.inputs:
                output += i  
                if self.inputs[i] == ModuleType.LOW:
                    output += " (LOW): "
                else:
                    output += " (HIGH): "
        else:
            if self.type == ModuleType.BROADCAST:
                output += "(B): "
            else:
                output += "(F): "
        output += ",".join(self.targets)

        return output
    
    def add_conjunction_input(self, input):
        self.inputs[input] = ModuleType.LOW

    def all_inputs_high(self):
        all_high = True 
        for i in self.inputs:
            all_high &= (self.inputs[i] == ModuleType.HIGH)
        return all_high

    def send_pulse(self, pulse, from_module, pulse_counts):
        if self.name == "rx":
            if pulse == ModuleType.LOW:
                # this is the end state
                raise Exception
            else:
                print("Rx sent a high pulse")
        if self.type == ModuleType.BROADCAST:
            return [(x,self.name,pulse) for x in self.targets]
        if self.type == ModuleType.FLIPFLOP:
            if pulse == ModuleType.HIGH:
                pass # do nothing on high pulses
            else:
                if self.state == ModuleType.OFF:
                    self.state = ModuleType.ON
                    return [(x,self.name,ModuleType.HIGH) for x in self.targets]
                else:
                    self.state = ModuleType.OFF 
                    return [(x,self.name,ModuleType.LOW) for x in self.targets]
        if self.type == ModuleType.CONJUNCTION:
            self.inputs[from_module] = pulse
            all_high = True 
            for i in self.inputs:
                all_high &= (self.inputs[i] == ModuleType.HIGH)
            if all_high:
                if self.name == "nl":
                    print(self.name + " sending a LOW pulse since all inputs are HIGH")
                    raise Error
                return [(x,self.name,ModuleType.LOW) for x in self.targets]
            """ if len(self.targets) > 1:
                print(self.name + " sending a HIGH pulse since all inputs are LOW") """
            return [(x,self.name,ModuleType.HIGH) for x in self.targets]
        return []

def push_button():
    global modules
    pulse_counts = {ModuleType.LOW: 0, ModuleType.HIGH: 0}
    start = "broadcaster"
    q = Queue(maxsize = 0)
    q.put((start, "button", ModuleType.LOW))
    while not q.empty():
        #print("Sending pulse")
        (to_module, from_module, pulse) = q.get()
        #print(to_module)
        pulse_counts[pulse]+=1
        if to_module in modules:
            new_pulses = modules[to_module].send_pulse(pulse, from_module, pulse_counts)
            #print(new_pulses)

            for new_pulse in new_pulses:
                q.put(new_pulse)
    return pulse_counts

with open("puzzle_input.txt", "r") as inp:
#with open("/home/mshaneck/development/advent_of_code/advent_of_code_2023/20/test_input2.txt", "r") as inp:
    for line in inp:
        line = line.strip()
        #print(line)
        parts = [x.strip() for x in line.split("->")]
        #print(parts)
        m = Module(parts[0], parts[1])
        modules[m.name] = m 

# set up conjunction inputs
for name in modules:
    m = modules[name]
    for t in m.targets:
        if t in modules:
            m2 = modules[t]
            if m2.type == ModuleType.CONJUNCTION:
                m2.add_conjunction_input(name)

i=1
try:
    while True:
        push_button()
        i += 1
        print(i)
        """ print(modules["pb"])
        if modules["pb"].all_inputs_high():
            print("pb: "+ str(i))
        if modules["nl"].all_inputs_high():
            print("nl: "+ str(i))
        if modules["dj"].all_inputs_high():
            print("dj: "+ str(i))
        if modules["rr"].all_inputs_high():
            print("rr: "+ str(i)) """
except:
    print(i)

move_counts = [3797,4051,3847,3877]
lcm = 1
for i in move_counts:
    lcm = lcm*i//math.gcd(lcm,i)

print(lcm)
