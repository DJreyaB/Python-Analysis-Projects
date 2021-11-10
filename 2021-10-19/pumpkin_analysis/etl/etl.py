def separate_year_type(df):
    '''
    description: Accepts a dataframe with overloaded id column and separates into 2 columns[year, type]
    argument: 
        df = pandas dataframe 
    return:
        df: cleaned dataframe
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

def drop_cols(df, cols):
    '''
    description: Accepts dataframe and list of columns to remove from the dataframe. returns the dataframe with the columns removed.
    arguments:
        df = pandas dataframe 
        cols = list of columns to remove
    return:
        df: reduced dataframe
    '''
    df.drop(['id', 'variety'], axis = 1, inplace = True)
    return df