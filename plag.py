class Plagiarism:
    def into_set(self, doc_content):
        '''
        We have to make sure that our content is only strings and the returns it,
        otherwise if it's not don't return it.
        '''
        if not isinstance(doc_content, str):
            raise ValueError('Input must be a string')
        return doc_content.split()  # split text into words
    
    def check_plag(self, words1, words2):
        set1 = set(words1)
        set2 = set(words2)
        common = len(set1 & set2)
        union = len(set1 | set2)
        similarity = (common / union) * 100 if union != 0 else 0
        
        if similarity >= 50:
            print(f'''Alert:
        The document contents are very similar with {similarity:.2f}% similarity (plagiarism detected)''')
        else:
            print(f'''Caution:
        The document contents are not similar with {similarity:.2f}% similarity (no plagiarism)''')
    