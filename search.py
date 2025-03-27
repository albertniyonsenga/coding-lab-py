class Searching:
    def into_set(self, doc_content):
        '''
        We have to make sure that our content is only strings and the returns it,
        otherwise if it's not don't return it.
        '''
        if not isinstance(doc_content, str):
            raise ValueError('Input must be a string')
        return doc_content.split() 
        
    def search(self, query,words1, words2):
        set1 = set(words1)
        set2 = set(words2)
        self.query = query
        for words in set1 or set2:
            if self.query == words:
                return True
            else:
                return False