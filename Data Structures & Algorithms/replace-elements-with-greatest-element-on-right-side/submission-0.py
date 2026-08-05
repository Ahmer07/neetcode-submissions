class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # iterate array from start to second last element
        # set write index to 0
        # start reading from next elements
        # find greatest
        # write to write index
        # increment write index
        # at last set last element to -1

        for write_index in range(len(arr)-1):
            value = arr[write_index+1]
            for read_index in range(write_index+1, len(arr)):
                if arr[read_index] > value:
                    value = arr[read_index]
            arr[write_index] = value
            write_index += 1
        arr[-1] = -1
        return arr

        