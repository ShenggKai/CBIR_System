import io
import sys
from typing import List, Set

# use type hint to make the code more readable and maintainable.
def load_list(fname: str) -> List[str]:
    ret = []
    try:
        with io.open(fname, 'r', encoding='utf-8') as fobj:
            for line in fobj:
                ret.append(line.strip())
    except FileNotFoundError:
        print(f"File {fname} not found!", file=sys.stderr)
        sys.exit(-1)
    return ret

def vector_to_set(vec: List[str]) -> Set[str]:
    return set(vec)

# amb: a set of ambiguous items
def compute_ap(pos: Set[str], amb: Set[str], ranked_list: List[str]) -> float:
    old_recall = 0.0
    old_precision = 1.0
    ap = 0.0

    intersect_size = 0
    i = 0
    j = 0
    for i in range(len(ranked_list)):
        if ranked_list[i] in amb:
            continue
        if ranked_list[i] in pos:
            intersect_size += 1

        recall = intersect_size / len(pos)
        precision = intersect_size / (j + 1.0)

        ap += (recall - old_recall) * ((old_precision + precision) / 2.0)

        old_recall = recall
        old_precision = precision
        j += 1
    return ap

if __name__ == '__main__':
    # check whether the system have three arguments or not
    if len(sys.argv) != 3:
        # file=sys.stderr to direct the output of the print statement to the standard error stream
        print("Usage: python compute_ap.py [GROUNDTRUTH QUERY] [RANKED LIST].txt", file=sys.stderr)
        sys.exit(-1)

    # load ground truth query set
    gtq = sys.argv[1]

    # load ranked list
    ranked_list = load_list(sys.argv[2])

    good_set = vector_to_set(load_list(f"{gtq}_good.txt"))
    ok_set = vector_to_set(load_list(f"{gtq}_ok.txt"))
    junk_set = vector_to_set(load_list(f"{gtq}_junk.txt"))

    # positive set of ground truth = ok_set + good_set
    pos_set = good_set.union(ok_set)

    ap = compute_ap(pos_set, junk_set, ranked_list)

    print(ap)
