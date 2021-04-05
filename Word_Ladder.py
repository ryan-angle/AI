# Name: Ryan Angle        
# Date: Oct 15, 2020
import time
from collections import defaultdict

def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''
   adj_set = set()
   # TODO 1: adjacents
   letters = "abcdefghijklmnopqrstuvwxyz"
   temp = current
   for c in current:
      for l in letters:
         temp = current
         t = temp.replace(c, l)
         if t in words_set and t != current:
            adj_set.add(t)
   return adj_set
      

def check_adj(words_set):
   # This check method is written for words_6_longer.txt
   adj = generate_adjacents('listen', words_set)
   target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
   return (adj == target)

def bi_bfs(start, goal, words_set):
   '''The idea of bi-directional search is to run two simultaneous searches--
   one forward from the initial state and the other backward from the goal--
   hoping that the two searches meet in the middle. 
   '''
   if start == goal: return []
   # TODO 2: Bi-directional BFS Search
   wordList = set(words_set)
   wordList.discard(goal)
     
   l = len(start)
   children = defaultdict(list)
   queue = set([start])
   queue2 = set([goal])
   backward = False
   found = False
   
   while queue and queue2 and not found:
      for word in queue:
         wordList.discard(word)
      for word in queue2:
         wordList.discard(word)
   
      if len(queue) > len(queue2):
         queue, queue2 = queue2, queue
         backward = not backward
          
      next_queue = set()
      for word in queue:
         for i in range(l):
            for j in range(26):
               curr = word[:i] + chr(j + ord('a')) + word[i+1:]
               if curr in queue2:
                  found = True
                  if backward:
                     children[curr].append(word)
                  else:
                     children[word].append(curr)
               elif curr in wordList and not found:
                  next_queue.add(curr)
                  if backward:
                    children[curr].append(word)
                  else:
                     children[word].append(curr)
   
      queue = next_queue.copy()
   
   if not found:
      return None
   
   result = []
   queue = [[start]]
   stop = False
   while queue and not stop:
      next_queue = []
      for path in queue:
         for child in children[path[-1]]:
            new_path = path + [child]
            next_queue.append(new_path)
            if child == goal:
               stop = True
               result.append(new_path)
      queue = next_queue[:]
   
   return result[0]      
      
         
   return None

def main():
   filename = input("Type the word file: ")
   words_set = set()
   file = open(filename, "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))
   #print ("Check generate_adjacents():", check_adj(words_set))
   #print ("listen", generate_adjacents("listen", words_set))
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   cur_time = time.time()
   path = (bi_bfs(initial, goal, words_set))
   if path != None:
      print (path)
      print ("The number of steps: ", len(path))
      print ("Duration: ", time.time() - cur_time)
   else:
      print ("There's no path")
 
if __name__ == '__main__':
   main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''
