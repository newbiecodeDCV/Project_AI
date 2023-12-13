from queue import PriorityQueue
import math
from flask import Flask, render_template, request, jsonify
from Toa_do import g
app = Flask(__name__)

class Node:
    def __init__(self, position, cost, parent=None):
        self.position = position
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def heuristic(a, b):
    return euclidean_distance(a, b)

def find_nearest_graph_point(target_point, graph_nodes):
    nearest_point = None
    min_distance = float('inf')

    for node in graph_nodes:
        node_pos = graph_nodes[node]['pos']
        distance = euclidean_distance(target_point, node_pos)

        if distance < min_distance:
            min_distance = distance
            nearest_point = node_pos

    return nearest_point

def astar(start, end, graph):
    open_set = PriorityQueue()
    start_node = Node(start, 0)
    open_set.put(start_node)

    start_tuple = tuple(start)
    end_tuple = tuple(end)

    came_from = {start_tuple: None}
    cost_so_far = {start_tuple: 0}

    while not open_set.empty():
        current_node = open_set.get()
        current_position_tuple = tuple(current_node.position)

        if current_position_tuple == end_tuple:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = came_from[current_node.position]

            print("Path:", path[::-1])  # In ra đường đi khi thuật toán kết thúc
            return path[::-1]
        else:
            if current_position_tuple not in graph:
                continue  # Bỏ qua nếu node không tồn tại trong đồ thị

            for neighbor in graph.neighbors(current_position_tuple):
                neighbor_pos = find_nearest_graph_point(neighbor, graph.nodes())

                new_cost = cost_so_far[current_position_tuple] + graph[current_position_tuple][neighbor_pos]['weight']
                neighbor_tuple = tuple(neighbor_pos)

                if neighbor_tuple not in cost_so_far or new_cost < cost_so_far[neighbor_tuple]:
                    cost_so_far[neighbor_tuple] = new_cost
                    priority = new_cost + heuristic(neighbor_tuple, end_tuple)
                    neighbor_node = Node(neighbor_tuple, priority, parent=current_node)
                    open_set.put(neighbor_node)
                    came_from[neighbor_tuple] = current_node

            # In ra các bước của đường đi trong quá trình thực hiện
            print("Current Position:", current_position_tuple)
            print("Open Set:", [node.position for node in open_set.queue])
            print("Came From:", came_from)
            print("Cost So Far:", cost_so_far)

    return None


@app.route('/')
def index():
    return render_template('interactive_map.html')

@app.route('/get_coordinates', methods=['POST'])
def get_coordinates():
    data = request.json
    print('Received data from client:', data)
    start = tuple(data['start'])
    end = tuple(data['end'])

    # Sử dụng đồ thị tạo từ NetworkX
    start = find_nearest_graph_point(start, g.nodes())
    end = find_nearest_graph_point(end, g.nodes())
    path_coordinates = astar(start, end, g)
    return jsonify({'path': path_coordinates})

if __name__ == '__main__':
    app.run(debug=False)
