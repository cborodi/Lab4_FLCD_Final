

class FiniteAutomata:
    def readFile(self, fileName):
        with open(fileName) as file:
            line = file.readline()
            Q = []
            line_slice = line[3:-2]
            for e in line_slice.split(","):
                Q.append(e)
            line = file.readline()
            E = []
            line_slice = line[3:-2]
            for e in line_slice.split(","):
                E.append(e)
            line = file.readline()
            q0 = line[3:-1]
            line = file.readline()
            F = []
            line_slice = line[3:-2]
            for e in line_slice.split(","):
                F.append(e)

            file.readline()

            f = {} # transitions
            for line in file:
                if line == '}':
                    break
                from_state = line.strip().split('=')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                route = line.strip().split('=')[0].strip().replace('(', '').replace(')', '').split(',')[1]
                to_state = line.strip().split('=')[1].strip()
                print(from_state + ' ' + route + ' ' + to_state)
                if (from_state, route) in f.keys():
                    f[(from_state, route)].append(to_state)
                else:
                    f[(from_state, route)] = [to_state]

            return Q, E, f, q0, F

    def isDFA(self, f):
        for elem in f:
            if len(f[elem]) > 1:
                return False
        return True

    def isSequenceAccepted(self, sequence, q0, F, f):
        if self.isDFA(f):
            state = q0
            for symbol in sequence:
                if (state, symbol) in f.keys():
                    state = f[(state, symbol)][0]
                else:
                    return False
            if state in F:
                return True
        return False



fa = FiniteAutomata()
Q, E, f, q0, F = fa.readFile("FA.in")
print("======================================================")
print("Finite set of states> ")
print(Q)
print("Finite alphabet> ")
print(E)
print("Transition function> ")
print(f)
print("Initial state> ")
print(q0)
print("Final states> ")
print(F)
print("======================================================")

print("Is DFA> ")
print(fa.isDFA(f))

if fa.isDFA(f):
    sequence = input("Check sequence: ")
    sequence = sequence.split()
    if len(sequence) == 0:
        print(True)
    else:
        print(fa.isSequenceAccepted(sequence, q0, F, f))
