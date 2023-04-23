"""Given an array of integers where every integer occurs three times except for one integer, which only occurs once, 
find and return the non-duplicated integer.
For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19."""



def get_unique(arr) -> int:
    unique_elem = 0
    mask = 1
#NOTE: &, |, solos, son BITWISE operators, que trabajan de forma directa con el binario. << es SHL(1, num).
    for _ in range(64):
        sum_i_pos_bits = 0
        # calculating the sum of the bits in the current position
        for elem in arr:
            if elem & mask != 0:
                sum_i_pos_bits = sum_i_pos_bits + 1
        # updating the unique element
        if sum_i_pos_bits % 3 == 1:
            unique_elem = unique_elem | mask
        # updating mask
        #SHL con un 1
        mask = mask << 1
    return unique_elem


if __name__ == "__main__":
    arr = [3, 3, 2, 3]
    print(get_unique(arr))

    arr = [13, 19, 13, 13]
    print(get_unique(arr))

    arr = [6, 1, 3, 3, 3, 6, 6]
    print(get_unique(arr))

    arr = [12, 1, 3, 1, 1, 2, 3, 2, 2, 3]
    print(get_unique(arr))
