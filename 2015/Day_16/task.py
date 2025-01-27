'''
Advent of Code 
2015 day 16
my solution to task 1
task 1 - iterate over Sues data to get the right one
task 2 - add lambda functions to check for sue


'''


class Solution:

    def __init__(self, sue_filename, filename) -> None:
        self.sues_dict = {}
        self.original_sue = self.get_sue(sue_filename)
        self.get_data(filename)
    
    def get_sue(self, filename):
        sue_dict = {}
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().split(':')
                sue_dict.setdefault(line[0], int(line[-1]))
        return sue_dict

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            i = 1
            for line in myfile:
                line = line[line.find(':') + 1:]
                line = line.strip().split(',')
                self.sues_dict.setdefault(i, {})
                for chunk in line:
                    chunk = chunk.strip().split(':')
                    self.sues_dict[i].setdefault(chunk[0], int(chunk[-1]))
                i += 1
    
    def check_sue(self, sue):
        for key, value in sue.items():
            if value != self.original_sue[key]:
                return False
        return True

    def check_sue_2(self, sue, check_functions):
        for key, value in sue.items():
            if key in check_functions.keys():
                if check_functions[key](value, self.original_sue[key]):
                    return False
            elif value != self.original_sue[key]:
                return False
        return True
    

    def solution_1(self) -> int:
        for key, sue in self.sues_dict.items():
            if self.check_sue(sue):
                return key
        
        return 0
    
    def solution_2(self) -> int:
        check_functions = {'cats': lambda value, original: value <= original,
                           'trees': lambda value, original: value <= original,
                           'pomeranians': lambda value, original: value >= original,
                           'goldfish': lambda value, original: value >= original}
        for key, sue in self.sues_dict.items():
            if self.check_sue_2(sue, check_functions):
                return key
        
        return 0
    
    


def main():

    print('TASK 1')
    sol = Solution('2015/Day_16/original_aunt.txt', '2015/Day_16/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
