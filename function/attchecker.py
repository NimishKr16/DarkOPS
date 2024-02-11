
 #-----------Checks if the attributes in attrdict are present and not None.-----------#

def check_attr(attrdict: dict,taburl:str, reviews=[]):
    supported = ["myntra","ajio","reliancedigital"]
    result = "All Attributes Found"
    all_not_none = True

    if supported[1] in taburl: # AJIO
        all_not_none = len(attrdict)==5 and all(value is not None for value in attrdict.values())
    
    elif supported[0] in taburl: # MYNTRA
        all_not_none = len(attrdict) == 3 and all(value is not None for value in attrdict.values()) and len(reviews)!=0
    
    elif supported[2] in taburl: # Reliance Digital
        all_not_none = len(attrdict) == 3 and all(value is not None for value in attrdict.values()) and len(reviews)!=0
    
    if not all_not_none:
        result = "FLAG: All attributes NOT Found"
    
    return result
        
         





   


