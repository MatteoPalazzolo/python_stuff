from __future__ import annotations
from collections import deque
from typing import Any, cast

class Graph:
    class Node:
        def __init__(self, id: int, el: Any):
            self._id: int = id
            self._el: Any = el
        
        def __str__(self):
            return f"Node({self._el})"
            
    def __init__(self):
        self._lstid: int = 0
        self._nodes: dict[int, Graph.Node] = {}
        self._links: set[tuple[int, int]] = set()
        
    def add_node(self, el: Any) -> int:
        id = self._lstid 
        self._nodes[id] = Graph.Node(id,el)
        self._lstid += 1
        return id
    
    def add_link(self, id1: int, id2: int):
        if id1 == id2:
            return
        if id1 < id2:
            tpl: tuple[int,int] = (id1, id2)
        else:
            tpl: tuple[int,int] = (id2, id1)
        self._links.add(tpl)
    
    def _get_neighbor_ids(self, id: int) -> list[int]:
        out: list[int] = []
        for l in self._links:
            if id == l[0]:
                out.append(l[1])
            elif id == l[1]:
                out.append(l[0])
        return out
        
    def find_path(self, id1: int, id2: int) -> list[int]:
        queue: deque[tuple[int|None,int]] = deque(((None,id1),))
        visited: set[int] = set()
        path_dict: dict[int,int|None] = {}
        while len(queue)>0:
            prvs,id = queue.popleft()
            if id in visited:
                continue
            else:
                visited.add(id)
            path_dict[id] = prvs
            if id == id2: #FOUND!
                break
            [queue.append((id,nbr_id)) for nbr_id in self._get_neighbor_ids(id) if nbr_id not in visited]
        else:
            return []
        # print(path_dict)
        v: int|None = id2
        out: list[int|None] = [id2]
        while True:
            v = path_dict[v]
            if v == None:
                break
            out.append(v)
        return cast(list[int], out)
        
    def __str__(self):
        out = ""
        for k,n in self._nodes.items():
            out += f"{k}: {n}\n"
        out += "-"*10+"\n"
        for i, (id1,id2) in enumerate(self._links):
            out += f"{id1} <-> {id2}"
            if i != len(self._links)-1:
                out += "\n"
        return out

if __name__ == "__main__":
    graph = Graph()
    n1 = graph.add_node("ciao")
    n2 = graph.add_node("cioo")
    n3 = graph.add_node("hey")
    n4 = graph.add_node("formaggio")
    n5 = graph.add_node("mozzarella")
    n6 = graph.add_node("mozza")
    n7 = graph.add_node("rella")
    graph.add_link(n1, n2)
    graph.add_link(n1, n3)
    graph.add_link(n1, n4)
    graph.add_link(n4, n5)
    graph.add_link(n5, n6)
    graph.add_link(n4, n7)
    graph.add_link(n6, n7)
    print(graph)
    print("path:", graph.find_path(n2, n5))
