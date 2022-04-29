import ast
from msilib.schema import CheckBox
import random
import networkx as nx
import matplotlib.pyplot as plt

# Hasse diagram for given POSset(partially ordered set)
# ornek input: (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 2), (2, 4), (2, 6),(2, 8), (3, 3), (3, 6), (3, 9),(4, 4), (4, 8), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)

# Kullanicinin girecegi eleman listesi
mylist1 = []

# Elemanlar alinir
mylist2 = ast.literal_eval(input('Enter the values: '))
for a, b in mylist2:
      mylist1.append(a and b)

for i in list(range(1, 10)):
      for a in mylist1:
            while mylist1.count(a) > 1:
                  mylist1.remove(a)
# Listede siralama yaptik
mylist1.sort()

# Sonuclari tutmasi icin bir dict olusturduk
result = {}

for first, second in mylist2:
      result.setdefault(first, []).append(second)

reflexive_list = []
for a, b in list(mylist2):
      if a == b:
            reflexive_list.append((a, b))

primes = []

for num in mylist1:
      prime = True
      for i in range(2, num):
            if num % i == 0:
                  prime = False

      if prime:
            primes.append(num)


def check_reflexive():
      if len(reflexive_list) == len(mylist1):
            print(reflexive_list, "is reflexive")
            return True
      else:
            print("Not reflexive")
            return False


def check_asymmetric():
      asymmteric_list = []
      for b in mylist2:
            swap1 = b[0]
            swap2 = b[1]
            newtuple = (swap2, swap1)
            asymmteric_list.append(newtuple)
      for u in reflexive_list:
            if u in asymmteric_list:
                  asymmteric_list.remove(u)
            else:
                  None
      print(asymmteric_list)

      for q in asymmteric_list:
            if q in mylist2:
                  print("Not asymmetric")
                  return False

      print("Asymmetric")
      return True


def check_transitive():
      for a, b in mylist2:
            for x in result[b]:
                  if x in result[a]:
                        None
                  else:
                        print("Transitive check failed")
                        return False
      print("It is transitive")
      return True


def draw_diagram():
      pos = {}

      randlist = list(range(1, len(list(result.keys())) + 1))
      for a in list(result.keys()):
            if a == 1:
                  pos.setdefault(a, ((len(list(result.keys())) / 2), -len(list(result.keys())) * 2 - 4))
            elif a in primes:
                  pos.setdefault(a, (a, -len(list(result.keys())) * 2))
            elif len(list(result[a])) == 1:
                  exitr = random.choice(randlist)
                  pos.setdefault(a, (exitr, 0))
                  randlist.remove(exitr)
            else:
                  exitr = random.choice(randlist)
                  pos.setdefault(a, (exitr, (-len(list(result[a]))) * 2))

      edges = {}
      mylist1_reverse = list(mylist1)
      for a in mylist1_reverse:
            for b in mylist1_reverse:
                  if a % b == 0 and a != b:
                        edges.setdefault(a, []).append(b)

      edge_list = [(x, y) for x, y in mylist2 if x != y]
      for i in list(range(1, 10)):
            for a, b in edge_list:
                  if b in list(edges.keys()):
                        for z in edges[b]:
                              if z != a and z % a == 0:
                                    while (a, b) in edge_list:
                                          edge_list.remove((a, b))

      T = nx.DiGraph()
      T.add_nodes_from(list(pos.keys()))
      T.add_edges_from(edge_list)
      plt.figure()
      if check_reflexive() == True and check_asymmetric() == True and check_transitive() == True:
            nx.draw(T, pos, node_color="black", node_size=600, font_size=15, font_color="yellow", with_labels=True,
                    arrowsize=18, edge_color="green")
      else:
            return "No hasse"
      plt.savefig("Hasse diagram.png")


draw_diagram()