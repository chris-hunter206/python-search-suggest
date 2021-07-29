#!/usr/local/bin/python3
'''
Define functions to return suggestions for partial search terms, such as one
would see when typing into a form.

Matches should only return if the word starts with the first letter typed,
and so forth. i.e. matches should not return if the word contains the search
term starting at some other point within the word.
'''

import pprint

def init_search_cache(wordlist):
    '''Initialize search cache based on a given wordlist'''

    search_cache = {}

    # parse each word given
    for word in wordlist:
        substring = ''
        for letter in word:
            # create new substring adding to previous letters
            substring = f'{substring}{letter}'
            if substring not in search_cache.keys():
                search_cache[substring] = [word]
            else:
                search_cache[substring].append(word)

    print('Initialized cache:')
    print(pprint.pprint(search_cache,indent=2))
    return search_cache


def search(search_cache,search_term):
    '''Return cached searches for a given word'''

    results = []
    substring = ''

    if search_term in search_cache.keys():
        match = search_cache[search_term]
        if match not in results:    # avoid duplicates
            results.append(match)

    return results


def test(search_cache,search_words):
    '''Wrapper to test search'''

    for word in search_words:
        results = search(search_cache,word)
        print(f'{word}: {results}')


if __name__ == "__main__":
    '''Test our module'''

    wordlist = ['apple','anyman','ask','band','bold','bolder','man']
    search_cache = init_search_cache(wordlist)

    print("\nExpect to Pass:")
    test(search_cache,['ask','b','band','bo','man'])

    print("\nExpect to Fail:")
    test(search_cache,['many','woman','grapple','rapple'])

