def clean(dictionary: dict):
    """
    Used to remove inconsistencies such as word_tag1-tag2
    Converts it to word_tag1 and word_tag2
    """
    clean_dictionary = dictionary.copy()
    for key, value in dictionary.items():
        word, tag = key.split('_', 1)
        tag_parts = tag.split('-')
        if len(tag_parts) > 1:
            factor = len(tag_parts)
            value = value / factor
            del clean_dictionary[key]
            for tag_part in tag_parts:
                word_tag = word + '_' + tag_part
                if word_tag in clean_dictionary:
                    clean_dictionary[word_tag] = clean_dictionary[word_tag] + value
                else:
                    clean_dictionary[word_tag] = value
    return clean_dictionary
