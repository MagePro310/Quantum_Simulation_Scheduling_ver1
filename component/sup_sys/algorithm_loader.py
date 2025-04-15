import os
import pandas as pd

def load_algorithms(algorithm_path='component/d_scheduling/algorithm'):
    type_algorithm = os.listdir(algorithm_path)
    clean_type_algorithm = [item for item in type_algorithm if item not in ['__pycache__', '__init__.py']]

    dict_algorithm = {}
    for item in clean_type_algorithm:
        sub_path = os.path.join(algorithm_path, item)
        dict_algorithm[item] = os.listdir(sub_path)
        clean_dict_algorithm = [algo for algo in dict_algorithm[item] if algo not in ['__pycache__', '__init__.py']]
        dict_algorithm[item] = clean_dict_algorithm

    rows = []
    for alg_type, alg_list in dict_algorithm.items():
        if alg_list:
            for alg in alg_list:
                rows.append({'Algorithm Type': alg_type, 'Algorithm': alg})
        else:
            rows.append({'Algorithm Type': alg_type, 'Algorithm': '(none)'})

    df = pd.DataFrame(rows)
    return df