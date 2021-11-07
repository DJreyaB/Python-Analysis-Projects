def separate_year_type(df):
    '''
    description: Accepts a dataframe with overloaded id column and separates into 2 columns[year, type]
    argument: 
        df = pandas dataframe 
    return:
        cleaned dataframe
    '''
    types = {
    'F ': "Field Pumpkin", 
    'P' : "Giant Pumpkin", 
    'S' : "Giant Squash", 
    'W' : "Giant Watermelon", 
    'L' : "Long Gourd" , 
    'T' : 'Tomato'
}
    df[['year', 'type']] = df['id'].str.split('-', expand = True)
    df['type'] = df['type'].map(types)
    return df