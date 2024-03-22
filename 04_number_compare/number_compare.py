def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    return {
        a==b: 'Numbers are equal',
        a<b: 'Second is greater',
        a>b: 'First is greater'
    }[True]