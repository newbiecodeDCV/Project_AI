import json
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import folium
with open('export.geojson') as f:
    geojson_data = json.load(f)

# Trích xuất tọa độ
coordinates = []

for feature in geojson_data['features']:
    geometry = feature['geometry']
    if geometry['type'] == 'Point':
        coordinates.append(geometry['coordinates'])

# Sắp xếp tọa độ theo thứ tự
sorted_coordinates = sorted(coordinates, key=lambda x: x[0])

# Lưu trữ tọa độ vào dict với tên theo thứ tự 'point_1', 'point_2', ...
coordinate_dict = {}

for i, coord in enumerate(sorted_coordinates):
    key = f'point_{i + 1}'
    value = [coord[1],coord[0]]
    coordinate_dict[key] = value

# Danh sách các điểm mới
new_point=[[21.01125,105.84794],
           [21.01113,105.84725],
           [21.01104,105.84675],
           [21.01105,105.84664],
           [21.01109,105.84654],
           [21.0112,105.84653],
           [21.01124,105.84639],
           [21.01133,105.84593],
           [21.01331,105.84829],
           [21.01321,105.84743],
           [21.01421,105.84832],
           [21.01418,105.84763],
           [21.01323,105.84702],
           [21.01246,105.84716],
           [21.01303,105.84828],
           [21.01279,105.84821],
           [21.01256,105.84876],
           [21.01103,105.8509],
           [21.01053,105.85085],
           [21.00911,105.85062],
           [21.00993,105.85022],
           [21.00951,105.84986],
           [21.00871,105.84985],
           [21.0089,105.84598],
           [21.00968,105.84562],
           [21.01001,105.84559],
           [21.01085,105.84582],
           [21.01066,105.84606],
           [21.01061,105.84649],
           [21.01056,105.84611],
           [21.0104,105.84639],
           [21.01009,105.84628],
           [21.01002,105.84594],
           [21.00997,105.84595],
           [21.00995,105.84623],
           [21.0099,105.84623],
           [21.00968,105.84624],
           [21.00945,105.84626],
           [21.00901,105.84656],
           [21.00865,105.84681],
           [21.00824,105.84698],
           [21.00856,105.8475],
           [21.00833,105.84754],
           [21.00992,105.84674],
           [21.00984,105.84737],
           [21.00985,105.84777],
           [21.00967,105.84776],
           [21.00964,105.84751],
           [21.00967,105.84711],
           [21.00912,105.8477],
           [21.00876,105.84772],
           [21.01001,105.84779],
           [21.01006,105.84732],
           [21.01071,105.84787],
           [21.01066,105.84829],
           [21.01094,105.84837],
           [21.01118,105.84857],
           [21.01063,105.84848],
           [21.00976,105.8484],
           [21.00969,105.84834],
           [21.00905,105.84825],
           [21.00969,105.8486],
           [21.00937,105.8486],
           #mới
           [21.00773,105.84274],
           [21.00778,105.84181],
           [21.00807,105.84543],
           [21.00799,105.84466],
           [21.00789,105.84388],
           [21.00784,105.84144],
           [21.00817,105.84142],
           [21.00868,105.84141],
           [21.00873,105.84137],
           [21.01058,105.84135],
           [21.01058,105.84135],
           [21.01212,105.84136],
           [21.01267,105.84138],
           [21.01267,105.84138],
           [21.01410,105.84139],
           [21.01457,105.84142],
           [21.01503,105.84141],
           [21.01503,105.84141],
           [21.01607,105.84142],
           [21.01508,105.84193],
           [21.01508,105.84193],
           [21.01556,105.84261],
           [21.01603,105.84260],
           [21.01606,105.84199],
           [21.01560,105.84196],
           [21.01007,105.84136],
           [21.01171,105.84136],
           [21.01344,105.84140],
           [21.01559,105.84141],
           [21.01509,105.84258],
           [21.00956,105.84136],
           [21.01623,105.84753],
           [21.01428,105.84917],
           [21.01255,105.84675],
           [21.01211,105.84765],
           [21.01010,105.84962],
           ]
for i in range(len(new_point)) :
    key =f'new_point_{i+1}'
    coordinate_dict[key] = new_point[i]
    

# Tạo danh sách các cạnh

edge_list = [('point_14','point_12'),('point_12','point_14'),
             ('point_11','point_12'),('point_12','point_11'),
             ('point_10','point_11'),('point_11','point_10'),
             ('point_10','point_9'),('point_9','point_10'),
             ('point_9','point_8'),('point_8','point_9'),
             ('point_8','point_7'),('point_7','point_8'),
             ('point_7','point_6'),('point_6','point_7'),
             ('point_6','new_point_13'),('new_point_13','point_6'),
             ('new_point_10','new_point_13'),('new_point_13','new_point_10'),
             ('new_point_10','new_point_12'),('new_point_12','new_point_10'),
             ('new_point_10','new_point_9'),('new_point_9','new_point_10'),
             ('new_point_11','new_point_9'),('new_point_9','new_point_11'),
             ('new_point_9','point_23'),('point_23','new_point_9'),
             ('point_24','point_23'),
             ('point_6','point_5'),('point_5','point_6'),
             ('point_5','new_point_97'),('new_point_97','new_point_14'),
             ('new_point_10','new_point_14'),('new_point_14','new_point_10'),
             ('new_point_14','new_point_97'),('new_point_97','new_point_14'),
             ('point_5','new_point_97'),('new_point_97','point_5'),
             ('point_21','point_15'),('new_point_14','new_point_98'),
             ('new_point_15','new_point_9'),('new_point_9','new_point_15'),
             ('new_point_15','new_point_16'),('new_point_16','new_point_15'),
             ('new_point_17','new_point_16'),('new_point_16','new_point_17'),
             ('new_point_17','point_22'),('point_22','new_point_17'),
             ('point_23','point_22'),
             ('point_22','point_21'),
             ('point_21','point_20'),('point_20','point_19'),
             ('point_16','point_20'),('point_20','point_16'),
             ('point_15','new_point_57'),('new_point_57','point_15'),
             ('point_16','new_point_57'),('new_point_57','point_16'),
             ('point_26','point_21'),('point_25','point_26'),('point_26','point_25'),
             ('point_19','point_25'),('point_25','point_28'),('point_28','new_point_19'),
             ('new_point_19','new_point_18'),('new_point_18','new_point_19'),
             ('point_27','point_19'),('point_19','point_27'),('point_27','new_point_20'),
             ('new_point_20','new_point_19'),('new_point_19','new_point_20'),
             ('point_4','point_5'),('point_5','point_4'),
             ('point_4','point_3'),('point_3','point_4'),
             ('point_3','point_1'),('point_1','point_3'),
             ('point_1','new_point_8'),('new_point_8','point_1'),
             ('new_point_27','new_point_8'),('new_point_8','new_point_27'),
             ('new_point_27','new_point_26'),('new_point_26','new_point_27'),
             ('new_point_25','new_point_26'),('new_point_26','new_point_25'),
             ('new_point_25','new_point_24'),('new_point_24','new_point_25'),
             ('new_point_24','point_2'),('point_2','new_point_24'),
             ('new_point_23','point_18'),('point_18','point_13'),('point_13','new_point_43'),
             ('new_point_43','new_point_41'),('new_point_41','point_2'),
             ('new_point_22','point_27'),('point_27','new_point_22'),
             ('new_point_22','new_point_23'),('new_point_23','new_point_22'),
             ('point_19','point_17'),('point_17','point_18'),
             ('point_15','new_point_1'),('new_point_1','point_15'),
             ('new_point_54','new_point_1'),('new_point_1','new_point_54'),
             ('new_point_54','new_point_52'),('new_point_52','new_point_54'),
             ('new_point_52','new_point_46'),('new_point_46','new_point_47'),
             ('new_point_50','new_point_47'),('new_point_47','new_point_50'),
             ('new_point_50','new_point_51'),('new_point_51','new_point_50'),
             ('new_point_51','point_13'),('point_13','new_point_51'),
             ('new_point_57','new_point_56'),('new_point_56','new_point_57'),
             ('new_point_56','new_point_55'),('new_point_55','new_point_56'),
             ('new_point_54','new_point_55'),('new_point_55','new_point_58'),
             ('new_point_58','new_point_59'),('new_point_59','new_point_60'),('new_point_60','new_point_61'),
             ('new_point_61','new_point_50'),('new_point_59','new_point_62'),('new_point_62','new_point_59'),
             ('new_point_62','point_17'),('point_17','new_point_62'),
             ('new_point_62','new_point_63'),('new_point_63','new_point_62'),
             ('new_point_1','new_point_2'),('new_point_2','new_point_1'),('new_point_2','new_point_3'),('new_point_3','new_point_2'),
             ('new_point_3','new_point_4'),('new_point_4','new_point_3'),('new_point_4','new_point_5'),('new_point_5','new_point_4'),
             ('new_point_5','new_point_6'),('new_point_6','new_point_5'),('new_point_6','new_point_7'),('new_point_7','new_point_6'),
             ('new_point_7','new_point_8'),('new_point_8','new_point_7'),
             ('new_point_27','new_point_28'),('new_point_28','new_point_27'),
             ('new_point_28','new_point_29'),('new_point_29','new_point_28'),
             ('new_point_28','new_point_30'),('new_point_30','new_point_28'),
             ('new_point_30','new_point_31'),('new_point_31','new_point_30'),
             ('new_point_33','new_point_30'),('new_point_30','new_point_33'),
             ('new_point_33','new_point_34'),('new_point_34','new_point_33'),
             ('new_point_34','new_point_36'),('new_point_36','new_point_34'),
             ('new_point_31','new_point_32'),('new_point_32','new_point_31'),
             ('new_point_31','new_point_32'),('new_point_32','new_point_31'),
             ('new_point_32','new_point_35'),('new_point_35','new_point_32'),
             ('new_point_35','new_point_36'),('new_point_36','new_point_35'),
             ('new_point_36','new_point_37'),('new_point_37','new_point_36'),
             ('new_point_37','new_point_38'),('new_point_38','new_point_37'),
             ('new_point_38','new_point_39'),('new_point_39','new_point_38'),
             ('new_point_39','new_point_40'),('new_point_40','new_point_39'),
             ('new_point_40','new_point_41'),('new_point_41','new_point_40'),
             ('new_point_42','new_point_43'),('new_point_43','new_point_42'),
             ('new_point_32','new_point_44'),('new_point_44','new_point_32'),
             ('new_point_44','new_point_45'),('new_point_45','new_point_44'),
             ('new_point_45','new_point_46'),('new_point_46','new_point_45'),
             ('new_point_52','new_point_53'),('new_point_53','new_point_52'),
             ('new_point_47','new_point_48'),('new_point_48','new_point_47'),
             ('new_point_48','new_point_49'),('new_point_49','new_point_48'),
             ('point_2', 'new_point_66'),('new_point_66','new_point_67'),
             ('new_point_67','new_point_68'),('new_point_68','new_point_64'),
             ('new_point_64','new_point_65'),('new_point_65','new_point_69'),
             ('new_point_65','new_point_70'),('new_point_69','new_point_70'),
             ('new_point_70','new_point_72'),('new_point_72','new_point_94'),
             ('new_point_94','new_point_89'),('new_point_89','new_point_74'),
             ('new_point_74','new_point_90'),('new_point_90','new_point_75'),
             ('new_point_75','new_point_77'),('new_point_77','new_point_91'),
             ('new_point_91','new_point_78'),('new_point_78','new_point_79'),
             ('new_point_79','new_point_81'),('new_point_81','new_point_92'),
             ('new_point_81','new_point_84'),('new_point_84','new_point_81'),
             ('new_point_81','new_point_92'),('new_point_92','new_point_82'),
             ('new_point_84','new_point_88'),('new_point_88','new_point_84'),
             ('new_point_88','new_point_87'),('new_point_87','new_point_88'),
             ('new_point_86','new_point_87'),('new_point_87','new_point_86'),
             ('new_point_86','new_point_85'),('new_point_85','new_point_86'),
             ('new_point_85','new_point_93'),('new_point_93','new_point_85'),
             ('new_point_84','new_point_93'),('new_point_93','new_point_84')
]



def euclidean_distance(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5


def creat_graph(coordinate_dict,edge_list):
    g = nx.DiGraph()
    g.add_nodes_from(coordinate_dict.keys())
    nx.set_node_attributes(g, coordinate_dict, 'pos')

    for edge in edge_list:
      node1, node2 = edge
      weight = euclidean_distance(coordinate_dict[node1], coordinate_dict[node2])
      g.add_edge(node1, node2, weight=weight)
    return g

g = creat_graph(coordinate_dict, edge_list)


node = 'new_point_1'
neighbors = g.neighbors(node)
print(neighbors)










