'''
Advent of Code 
2024 day 21
my solution to tasks

task 1 - 

task 2 - 


'''

import time
import heapq
from tqdm import tqdm
from sys import maxsize
from collections import Counter

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper


class Solution:

    def __init__(self, filename) -> None:
        '''
        initialize Solution
        '''
        self.sequences = []
        self.get_data(filename)
        self.numeric_keypad = {
                                 '0': {'>': 'A', '^': '2'},
                                 '1': {'>': '2', '^': '4'},
                                 '2': {'<': '1', '>': '3', '^': '5', 'v': '0'},
                                 '3': {'<': '2', '^': '6', 'v': 'A'},
                                 '4': {'>': '5', '^': '7', 'v': '1'},
                                 '5': {'<': '4', '>': '6', '^': '8', 'v': '2'},
                                 '6': {'<': '5', 'v': '3', '^': '9'},
                                 '7': {'v': '4', '>': '8'},
                                 '8': {'<': '7', '>': '9', 'v': '5'},
                                 '9': {'<': '8', 'v': '6'},
                                 'A': {'^': '3', '<': '0'}
                               }

        self.directional_keypad = {
                                    '^': {'>': 'A', 'v': 'v'},
                                    'v': {'>': '>', '<': '<', '^': '^'},
                                    '>': {'^': 'A', '<': 'v'},
                                    '<': {'>': 'v'},
                                    'A': {'<': '^', 'v': '>'}
                                  }
        # (start, stop): set_of_min_sequences
        self.min_sequences = {(key, key): Counter('A') for key in set(self.numeric_keypad.keys()).union(set(self.directional_keypad.keys()))} 
        print(self.min_sequences)



    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.sequences.append(line.strip())


    def get_min_paths_to_get_char(self, start_position, char, keypad):
        '''
        get all min sequences to get to char
        '''
        if (start_position, char) in self.min_sequences.keys():
            return self.min_sequences[(start_position, char)]
        # len(act_pos_to_get_there), act_position, act_sequence_to_get_there (><^VA), 
        # act_pos_sequence (A321)
        stack = [(0, start_position, '', start_position)] # len(act_pos_to_get_there), act_position, act_sequence_to_get_there (><^VA), act_pos_sequence
        heapq.heapify(stack)
        min_sequence_len = maxsize
        while stack:
            path_len, act_position, act_sequence, pos_sequence = heapq.heappop(stack)
            if act_position == char:
                if path_len > min_sequence_len:
                    break
                min_sequence_len = path_len
                resulting_counter = Counter(act_sequence + 'A')
                break
            for direction, new_position in keypad[act_position].items():
                if new_position not in pos_sequence:
                    heapq.heappush(stack, (path_len + 1, new_position, act_sequence + direction, pos_sequence + new_position))
        self.min_sequences[(start_position, char)] = resulting_counter
        return resulting_counter
    
    
    @time_it
    def solution_1(self, num_of_robots) -> int:
        '''
        get result for task 1
        '''
        result = 0
        for sequence in tqdm(self.sequences):
            # numeric keypad transform to moves of first robot
            start_pos = 'A'
            seq_int = int(sequence[:-1])
            possible_sequence = Counter()
            for char in sequence:
                possible_sequence += self.get_min_paths_to_get_char(start_pos, char, self.numeric_keypad)
                start_pos = char
            print(possible_sequence)
            # robot moves to transform (as 2 more robots so range 2)
            for _ in range(num_of_robots):
                robot_sequence = Counter()
                for char, value in possible_sequence.items():
                    for new_char, new_value in self.get_min_paths_to_get_char('A', char, self.directional_keypad).items():
                        robot_sequence[new_char] += new_value * value
                possible_sequence = robot_sequence
                print(possible_sequence)
            print(seq_int, possible_sequence.total())
            result += seq_int * possible_sequence.total()
        return result
    

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        return 0
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_21/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(2), 'should equal ?')
 #   print('test 1:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_21/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(2))
 #   print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()