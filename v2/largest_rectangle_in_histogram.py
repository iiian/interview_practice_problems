def largest_rectangle_in_histogram(H):
    stk = []
    max_area = float('-inf')
    for i in range(len(H)):
        next = H[i]
        while stk and next < H[stk[-1]]:
            p = stk.pop()
            if stk:
                area = H[p] * (i - stk[-1] - 1)
            else:
                area = H[p] * i
            max_area = max(area, max_area)
        stk.append(i)
    while stk:
        p = stk.pop()
        if stk:
            area = H[p] * (len(H) - stk[-1] - 1)
        else:
            area = H[p] * len(H)
        max_area = max(area, max_area)
    return max_area


# tests
if __name__ == "__main__":
    from testing import test_case
    test_case(
        "it should return the area of the largest rectangle in a histogram",
        #           %     
        #           %     
        #           %   
        #         % % % 
        #         % % % 
        #         % % % 
        #       % % % % %
        #     % % % % % %
        #   % % % % % % % % %
        largest_rectangle_in_histogram([1,2,3,6,9,6,3,1,1]),
        18,
    )

    test_case(
        "it should return the area of the largest rectangle in a histogram",
        largest_rectangle_in_histogram([1]),
        1,
    )

    test_case(
        #                
        #           %     
        #           %     
        #       %   %  
        #       %   % % 
        #     % %   % % 
        #     % % % % %
        #   % % % % % %
        #   % % % % % %
        "it should return the area of the largest rectangle in a histogram",
        largest_rectangle_in_histogram([2,4,6,3,8,5]),
        15,
    )