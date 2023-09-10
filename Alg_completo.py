class No:
    def __init__(self, nome: str, funcao_h: float):
        self.nome = nome
        self.funcao_h = funcao_h
        self.funcao_f = 0
        self.funcao_g = 0
        self.adjacentes = []
        self.no_antecessor = None

    def get_nome(self):
        return self.nome

    def get_funcao_h(self):
        return self.funcao_h

    def get_funcao_f(self):
        return self.funcao_f

    def get_funcao_g(self):
        return self.funcao_g

    def get_no_antecessor(self):
        return self.no_antecessor

    def get_adjacentes(self):
        return self.adjacentes

    def set_funcao_g(self, funcao_g: float):
        self.funcao_g = funcao_g

    def set_funcao_f(self, funcao_f: float):
        self.funcao_f = funcao_f

    def set_no_antecessor(self, no_antecessor):
        self.no_antecessor = no_antecessor

    def set_adjacentes(self, adjacentes: list):
        self.adjacentes = adjacentes

class Aresta:
    def __init__(self, custo: float, no_alvo: No):
        self.custo = custo
        self.no_alvo = no_alvo

    def get_custo(self):
        return self.custo

    def get_no_alvo(self):
        return self.no_alvo

class AEstrela:
    def busca_a_estrela(self, no_origem: No, no_destino: No):
        #criar as listas vazias
        prioridades = []
        explorados = []
        #listaPrioridade adiciona origem
        prioridades.append(no_origem)

        #se origem == destino finaliza
        if no_origem == no_destino:
            return []
        no_atual = prioridades[0]
        #Enquanto filaPrioridade não vazia e destino não encontrado
        while len(prioridades)>0 and (no_atual != no_destino):
            # No atual = no com menor função f
            no_atual = self.menor_funcao_f(prioridades)
            prioridades.remove(no_atual)
            # Fila explorados adiciona nó atual
            explorados.append(no_atual)
            # Se no atual == destino -> parar
            if no_atual == no_destino:
                return self.percorrer_caminho(no_atual)
            # Senao
            # Para cada aresta adjacente do no atual
            for aresta_temp in no_atual.get_adjacentes():
                # No filho = aresta.alvo
                no_filho = aresta_temp.get_no_alvo()
                # funcaoGTemp = noAtual.FuncaoG() + aresta.custo;
                g_temp = no_atual.get_funcao_g() + aresta_temp.get_custo()
                # funcaoFTemp = funcaoGTemp + noFilho.FuncaoH();
                f_temp = g_temp + no_filho.get_funcao_h()
                # Se caso o nó filho já tenha sido explorado e seu valor de função f é maior que a função f do pai, então ele é desconsiderado
                if no_filho in explorados and f_temp >= no_filho.get_funcao_f():
                    continue
                # senão se o nó filho não está na filaPrioridades ou sua função f é maior que a funcaoFTemp
                if no_filho not in prioridades or f_temp < no_filho.get_funcao_f():
                    # filho.Adjacente = atual;
                    no_filho.set_no_antecessor(no_atual)
                    # filho.funcaoG = funcaoGTemp;
                    no_filho.set_funcao_g(g_temp)
                    # filho.funcaoF= funcaoFTemp;
                    no_filho.set_funcao_f(f_temp)
                    # Se filaPrioridades não contem filho --> FilaPrioridades adiciona filho
                    if no_filho not in prioridades:
                        prioridades.append(no_filho)
        return None
    # melhorada chatGPT
    def menor_funcao_f(self, prioridades):
        return min(prioridades, key=lambda x: x.get_funcao_f())
    # melhorada chatGP
    def percorrer_caminho(self, alvo: No):
        caminho = []
        while alvo:
            caminho.insert(0, alvo.get_nome())
            alvo = alvo.get_no_antecessor()
        return caminho


# Main
arad = No("Arad", 366)
bucarest = No("Bucarest", 0)
craiova = No("Craiova", 160)
dobreta = No("Dobreta", 242)
eforie = No("Eforie", 161)
fagaras = No("Fagaras", 176)
giurgiu = No("Giurgiu", 77)
hirsova = No("Hirsova", 151)
iasi = No("Iasi", 226)
lugoj = No("Lugoj", 244)
mehadia = No("Mehadia", 241)
neamt = No("Neamt", 234)
oradea = No("Oradea", 380)
pitesti = No("Pitesti", 100)
rimnicuVilcea = No("Rimnicu Vilcea", 193)
sibiu = No("Sibiu", 253)
timisoara = No("Timisoara", 329)
urziceni = No("Urziceni", 80)
vaslui = No("Vaslui", 199)
zerind = No("Zerind", 374)

arad.set_adjacentes([Aresta(75, zerind), Aresta(140, sibiu), Aresta(118, timisoara)])
bucarest.set_adjacentes([Aresta(85, urziceni), Aresta(211, fagaras), Aresta(101, pitesti), Aresta(90, giurgiu)])
craiova.set_adjacentes([Aresta(138, pitesti), Aresta(146, rimnicuVilcea), Aresta(120, dobreta)])
dobreta.set_adjacentes([Aresta(120, craiova), Aresta(75, mehadia)])
eforie.set_adjacentes([Aresta(86, hirsova)])
fagaras.set_adjacentes([Aresta(99, sibiu), Aresta(211, bucarest)])
giurgiu.set_adjacentes([Aresta(90, bucarest)])
hirsova.set_adjacentes([Aresta(86, eforie)])
iasi.set_adjacentes([Aresta(92, vaslui), Aresta(87, neamt)])
lugoj.set_adjacentes([Aresta(111, timisoara), Aresta(70, mehadia)])
mehadia.set_adjacentes([Aresta(75, dobreta), Aresta(70, lugoj)])
neamt.set_adjacentes([Aresta(87, iasi)])
oradea.set_adjacentes([Aresta(71, zerind), Aresta(151, sibiu)])
pitesti.set_adjacentes([Aresta(97, rimnicuVilcea), Aresta(101, bucarest), Aresta(138, craiova)])
rimnicuVilcea.set_adjacentes([Aresta(97, pitesti), Aresta(146, craiova), Aresta(80, sibiu)])
sibiu.set_adjacentes([Aresta(99, fagaras), Aresta(80, rimnicuVilcea), Aresta(140, arad), Aresta(151, oradea)])
timisoara.set_adjacentes([Aresta(118, arad), Aresta(111, lugoj)])
urziceni.set_adjacentes([Aresta(85, bucarest), Aresta(142, vaslui), Aresta(98, hirsova)])
vaslui.set_adjacentes([Aresta(92, iasi), Aresta(142, urziceni)])
zerind.set_adjacentes([Aresta(71, oradea), Aresta(75, arad)])

a_estrela = AEstrela()
caminho = a_estrela.busca_a_estrela(arad, bucarest)
if caminho:
    print("Caminho:", caminho)
else:
    print("Caminho não encontrado.")
