import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError('List must contain Nine numbers.')
    else:
        list2 = np.array(list).reshape(3, 3)

    mean = [(list2.mean(axis=0).tolist()), (list2.mean(axis=1).tolist()),
            (list2.mean())]
            
    var = [(list2.var(axis=0).tolist()), (list2.var(axis=1).tolist()),
           (list2.var())]

    std = [(list2.std(axis=0).tolist()), (list2.std(axis=1).tolist()),
           (list2.std())]

    maxi = [(list2.max(axis=0).tolist()), (list2.max(axis=1).tolist()),
           (list2.max())]

    mini = [(list2.min(axis=0).tolist()), (list2.min(axis=1).tolist()),
           (list2.min())]

    summ = [(list2.sum(axis=0).tolist()), (list2.sum(axis=1).tolist()),
           (list2.sum())]

    return {
        "mean": mean,
        "variance": var,
        "standard deviation": std,
        "max": maxi,
        "min": mini,
        "sum": summ,
    }
    