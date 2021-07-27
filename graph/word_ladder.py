# Return number of words in shortest transformation sequence

def ladderLength(self, beginWord, endWord, wordList):
    # build adjacency list
    # all words in variations[i] have an edge between them
    # i.e. are only 1 character transformation away
    variations = {}
    for word in wordList:
        for i in range(len(word)):
            word_li = list(word)
            word_li[i] = "*"
            variation = "".join(word_li)
            if variation not in variations:
                variations[variation] = [word]
            else:
                variations[variation].append(word)
    
    # bfs
    q = [beginWord]
    vis = {beginWord: True}
    dist = {beginWord: 1}
    while q:
        cur = q.pop(0)
        cur_variations = []
        # build all variations of cur
        for i in range(len(cur)):
            cur_li = list(cur)
            cur_li[i] = "*"
            cur_variations.append("".join(cur_li))
        for cur_variation in cur_variations:
            # no other word matches this variation
            if cur_variation not in variations:
                continue
            # for all words that can be transformed into 
            # the current variation
            for word in variations[cur_variation]:
                if word in vis:
                    continue
                vis[word] = True
                q.append(word)
                dist[word] = dist[cur] + 1
                if word == endWord:
                    return dist[word]
    return 0


