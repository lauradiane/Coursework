from operator import itemgetter

def read_restaurants(file):
    """(file) -> ({str: int}, {str: [str]}, {str: [str]})

    Read the file and create data structures to represent the data in the file.

    Return a tuple of three dictionaries:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    lines = open(file).read().splitlines()

    entries =[lines[0:4], lines[5:9], lines[10:14], lines[15:19]]

    for entry in entries:
        name_to_rating[entry[0]] = int(entry[1].split('%')[0])
        price_to_names[entry[2]].append(entry[0])
        for cuisine in  entry[3].split(','):
            if cuisine in cuisine_to_names:
                cuisine_to_names[cuisine].append(entry[0])
            else:
                cuisine_to_names[cuisine] = [entry[0]]
    return (name_to_rating, price_to_names, cuisine_to_names)


def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ ([str], {str: [str]}, [str]) -> [str]

    Filter the list of restaurant names matching price to only return a list of restaurant names that also have cuisines from cuisines_list. 
    """
    names_matching_cuisine = []
    final_list = []

    for cuisine in cuisines_list:
        names_matching_cuisine.append(''.join(cuisine_to_names[cuisine]))

    for name in names_matching_cuisine:
        if name in names_matching_price:
            final_list.append(name)

    return final_list


def build_rating_list(name_to_rating, names_final):
    """({str: int}, [str]) -> [[int, str]]
        Return list names_final list of restaurants, sorted by ranking, in format [['ranking', 'name']]
    """
    new_list = []
    for name in names_final:
        new_list.append([name_to_rating[name], name])
    
    sorted_list = sorted(new_list, reverse=True)
    
    return sorted_list

def recommend(file, price, cuisines_list):
    """
    (file open for reading, str, [str]) -> [[str]]

    Returns restaurant recommendations from the file that match the price and cuisines_list inputs, sorted by rating.
    """
    # Read the file and create data structures to represent the data in the file.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cuisiine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]
    
    # Cuisines: Narrow this list of matching restaurants to the specified cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)
    
    # Sort this final list by ratings.
    result = build_rating_list(name_to_rating, names_final)

    # Return sorted result list.
    print result
    return result


def main():
    data = recommend("restaurants.txt", '$', ['Chinese', 'Thai'])
    return data

if __name__ == "__main__":
    main()
