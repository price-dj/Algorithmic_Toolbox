import operator

class MergeSorted:

    def __init__(self):
        self.inversions = 0

    def __call__(self, l, key=None, reverse=False):

        self.inversions = 0

        if key is None:
            self.key = lambda x: x
        else:
            self.key = key

        if reverse:
            self.compare = operator.gt
        else:
            self.compare = operator.lt

        dest = list(l)
        working = [0] * len(l)
        self.inversions = self._merge_sort(dest, working, 0, len(dest))
        return dest

    def _merge_sort(self, dest, working, low, high):
        if low < high - 1:
            mid = (low + high) // 2
            x = self._merge_sort(dest, working, low, mid)
            y = self._merge_sort(dest, working, mid, high)
            z = self._merge(dest, working, low, mid, high)
            return (x + y + z)
        else:
            return 0

    def _merge(self, dest, working, low, mid, high):
        i = 0
        j = 0
        inversions = 0

        while (low + i < mid) and (mid + j < high):
            if self.compare(self.key(dest[low + i]), self.key(dest[mid + j])):
                working[low + i + j] = dest[low + i]
                i += 1
            else:
                working[low + i + j] = dest[mid + j]
                inversions += (mid - (low + i))
                j += 1

        while low + i < mid:
            working[low + i + j] = dest[low + i]
            i += 1

        while mid + j < high:
            working[low + i + j] = dest[mid + j]
            j += 1

        for k in range(low, high):
            dest[k] = working[k]

        return inversions


msorted = MergeSorted()
