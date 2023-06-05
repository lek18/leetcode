
rates = [['US', 'JPY', 110], ['US', 'AUD', 1.45], ['JPY', 'GBP', 0.007]]
result = ['GBP', 'AUD', 1.89]


from typing import List
from collections import defaultdict, deque
import decimal

def Solution(rates:List, exchange:List) -> float:


    def bfs(start:str, end:str) -> float:
        # do bfs
        
        visited = set((start))
        queue = deque([(start,1)])
        while queue:

            N = len(queue)

            for _ in range(N):
                # pop each node
                node,curr_rate = queue.popleft()
    
                if node == end:
                    return  decimal.Decimal(curr_rate).quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_UP)
                
                for neighbour, rate in currency_graph[node]:

                    if neighbour not in visited and neighbour!=start:
                        visited.add(neighbour)
                        queue.append((neighbour, curr_rate*rate))        
        return None




    # compute graph first

    currency_graph = defaultdict(list)
    for start,end, rate in rates:

        currency_graph[start].append((end,rate))
        currency_graph[end].append((start,1.0/rate))
    
    print(currency_graph)

    
    return bfs(exchange[0], exchange[1])


print(Solution(rates, exchange=['GBP', 'AUD']))

        


# {'US': [('JPY', 110), ('AUD', 1.45)], 'JPY': [('US', 0.009), ('GBP', 0.007)], 'AUD': [('US', 0.69)], 'GBP': [('JPY', 142.857)]}

# GBP  -> JPY 142
# JPY -> US JPY -> GBP
# 142* 0.01, 142* 0.007

# US -> AUD
