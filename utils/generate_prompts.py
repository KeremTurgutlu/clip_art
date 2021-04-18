description_templates = [
                        ["__DIMENSION__", "__CULTURE__", "__ART_OBJECT__", "made from __MEDIUM__", "with __TAG__", "from country __COUNTRY__"],
    
                        ["__DIMENSION__", "__CULTURE__", "__ART_OBJECT__", "with __TAG__", "from country __COUNTRY__", "made out of __MEDIUM__"],

                        ["__DIMENSION__", "__CULTURE__", "__ART_OBJECT__", "with __TAG__", "from __COUNTRY__", "made from __MEDIUM__"],
                        
                        ["__DIMENSION__", "__CULTURE__", "__ART_OBJECT__", "with __TAG__", "from __COUNTRY__", "made from __MEDIUM__"]
]

### TODO: Try combinations up to 5 for tags and mediums

res = []
for _,row in progress_bar(train_df.iterrows(), total=len(train_df)): 
    _id = row['id']
    # create row dicts
    labeldict = defaultdict(list)
    for l in row['labels']:
        c,o = l.split("::")
        labeldict[c].append(o)

    # create row labels
    row_labels = []
    for desc in description_templates:
        for art_noun in ['art object', 'artwork', 'art']:
            descfinal = []
            for descpart in desc:
                if "__ART_OBJECT__" in descpart:                           descfinal += [descpart.replace("__ART_OBJECT__", art_noun)]
                if "__DIMENSION__" in descpart and labeldict['dimension']: descfinal += [descpart.replace("__DIMENSION__", ", ".join(labeldict['dimension']))]
                if "__CULTURE__" in descpart and labeldict['culture']:     descfinal += [descpart.replace("__CULTURE__", ", ".join(labeldict['culture']))]
                if "__MEDIUM__" in descpart and labeldict['medium']:       descfinal += [descpart.replace("__MEDIUM__", ", ".join(labeldict['medium']))]
                if "__TAG__" in descpart and labeldict['tags']:             descfinal += [descpart.replace("__TAG__", ", ".join(labeldict['tags']))]
                if "__COUNTRY__" in descpart and labeldict['country']:     descfinal += [descpart.replace("__COUNTRY__", ", ".join(labeldict['country']))]

            desc_label = " ".join(descfinal)
            res.append((_id, desc_label))
            