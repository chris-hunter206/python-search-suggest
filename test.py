#!/usr/bin/env python3
'''
Test the Module
'''

from search_suggest import init_search_cache
from search_suggest import suggest

def test(search_cache,search_words):
    '''Wrapper to test search'''

    for word in search_words:
        results = suggest(search_cache,word)
        print(f'{word}: {results}')


if __name__ == "__main__":
    '''Run Tests'''

    wordlist = [
        'apple',
        'anyman',
        'ask',
        'band',
        'bold',
        'bolder',
        'man',
    ]
    search_cache = init_search_cache(wordlist)

    print(f"\nUsing Wordlist: {wordlist}")

    print("\nExpect to Pass:")
    print("---------------")
    test(search_cache,['ask','b','band','bo','man'])

    print("\nExpect to Fail:")
    print("---------------")
    test(search_cache,['many','woman','grapple','rapple'])

