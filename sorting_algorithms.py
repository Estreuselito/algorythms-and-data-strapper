def merge_sort(unsorted_list):
    """recursive function which sorts a list by divide and sort

    Attributes
    ----------
    unsorted_list : list
        an unsorted list

    Returns
    -------
    sorted unsorted_list
    """
    if len(unsorted_list) <= 1:
        return unsorted_list

    left = merge_sort(unsorted_list[:len(unsorted_list)//2])
    right = merge_sort(unsorted_list[len(unsorted_list)//2:])

    return reduce(left, right)
    
def reduce(left, right):
    """merge and sort the left and right element

    Attributes
    ----------
    left : list
        a list with values

    right : list
        a list with values    
    """
    result = []
    left_index = 0
    right_index = 0
    while True:
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
        if left_index == len(left):
            result.extend(right[right_index:])
            break
        if right_index == len(right):
            result.extend(left[left_index:])
            break
    return result

def inseration_sort(unsorted_list, verbose = False):
    """a self-implemented method for inseration sorting

    Attributes
    ----------
    unsorted_list : list
        an unsorted list or an unsorted np.ndarray

    verbose : boolean
        in order to see, how this algorithms sorts, the verbose parameter can be changed to true

    Returns
    -------
    the sorted unsorted_list
    """
    j = 1
    while j <= len(unsorted_list)-1:
        key = unsorted_list[j]
        if verbose == True:
            BOLD = '\033[1m'
            END = '\033[0m'
            print("The complete list looks like: ", unsorted_list, "\n",
            'j is now at position: {}{}{}'.format(BOLD, j, END), "\n",
            "this is the following number in this list: {}{}{}".format(BOLD, key, END))
            time.sleep(5)
            clear_output(wait=True)

        i = j - 1
        while i >= 0 and unsorted_list[i] >= key:
            unsorted_list[i + 1] = unsorted_list[i]
            i -= 1
        j += 1
        unsorted_list[i + 1] = key
    return unsorted_list
