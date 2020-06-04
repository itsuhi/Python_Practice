# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    final_list = []
    if len(sequence) == 1:
        final_list.append(sequence)
        return final_list
    elif len(sequence) == 2:
        final_list.extend([sequence, sequence[::-1]])
        return final_list
    else:
        for combo in get_permutations(sequence[1::]):
            char_list = list(combo)
            
            for index in range(0, len(char_list) + 1):
                permu_list = char_list[:]
                permu_list.insert(index, sequence[0])
                permu_string = "".join(permu_list)
                final_list.append(permu_string)
        return final_list
        

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)



