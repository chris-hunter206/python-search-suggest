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
    '''
    Initialize search cache based on a given wordlist. Return a dict of
    the cached search results.

    The values for each search term in the dict should be a list of all words
    who's beginning matches the search term.
    '''
    search_cache = {}

    # parse each word given
    for word in wordlist:
        substring = ''
        for letter in word:
            # create subsequent search keys by adding additional letters to
            # a stack of all previous letters in the word
            substring = f'{substring}{letter}'

            if substring not in search_cache.keys():
                # create a new key if the search term does not exist yet
                search_cache[substring] = [word]
            else:
                # otherwise append to the list of existing results
                search_cache[substring].append(word)

    print('Initialized cache:')
    print(pprint.pprint(search_cache,indent=2))
    return search_cache


def search(search_cache,search_term):
    '''
    Return a list of cached search words for a given (partial) search term.
    Return an empty list if there are no results.
    '''
    results = []

    if search_term in search_cache.keys():
        results = search_cache[search_term]

    return results


def test(search_cache,search_words):
    '''Wrapper to test search'''

    for word in search_words:
        results = search(search_cache,word)
        print(f'{word}: {results}')


