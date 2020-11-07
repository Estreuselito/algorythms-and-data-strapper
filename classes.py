import numpy as np
import pandas as pd
import time
from tqdm import tqdm
import matplotlib.pyplot as plt

class Student:
    """Class for student information
    
    Attributes
    ---------
    course : str
        the name of a taken university course

    grade : float
        the grade as a float

    Methods
    -------
    add_grades(course, grade)
        adds grades to one student object

    get_gpa()
        returns the current gpa of a student
    """
    
    def __init__(self,
                 student_id,
                 first_name,
                 last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.grades = {}
        
    def add_grades(self, course, grade):
        self.grades[course] = grade
        
    def get_gpa(self):
        if len(self.grades) == 0:
            return 0.
        sum_ = 0
        for g in self.grades.values():
            sum_ += g
        return sum_/len(self.grades)
    
    def __repr__(self):
        return f"Student_id: {self.student_id}\n\
First name: {self.first_name}\n\
Last name: {self.last_name}\n\
GPA: {self.get_gpa()}"

    def __lt__(self, other):
        return self.student_id < other.student_id

    def __gt__(self, other):
        return self.student_id > other.student_id
        
class Node:
    """
    Class which creates nodes for a binary search tree
    
    Attributes
    ----------
    k: int, str
        the value the node shall take
        
    Methods
    -------
    insert(k)
        inserts a key as a node into the binary search tree, returns false, if node already exists
        
    get(k)
        searches all nodes for a certain value, and returns an according string
        
    display()
        visualizes the binary search tree
        
    _display_aux()
        returns list of strings, width, height, and horizontal coordinate of the root    
    """
    
    def __init__(self, k, data):
        self.left = None
        self.right = None
        self.key = k
        self.data = data
        
    def insert(self, data, key):
        """inserts a key as a node into the binary search tree, returns false, if node already exists
        
        Parameters
        ----------
        k: int, str
            the value the node shall take
        
        Returns
        -------
        Recursive function, returns either itself or "Already in tree", if node alreadys exists
        """
        if self.key == getattr(data, key):
            return "Already in tree"
        elif self.key > getattr(data, key):
            if self.left:
                return self.left.insert(data, key)
            else:
                self.left = Node(getattr(data, key), data)
                return "Inserted left"
        else:
            if self.right:
                return self.right.insert(data, key)
            else:
                self.right = Node(getattr(data, key), data)
                return "Inserted right"
        
    def get(self, k):
        """searches all nodes for a certain value, and returns an according string
        
        Parameters
        ----------
        k: int, str
            the value the node shall take
        
        Returns
        -------
        An according string
        """
        if self.key == k:
            return self.data
        elif k < self.key and self.left:
            return self.left.get(k)
        elif k > self.key and self.right:
            return self.right.get(k)
        return "Sorry pal, you are barking up the wrong tree!" 
    
    def display(self):
        """visualizes the binary search tree
        """
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """returns list of strings, width, height, and horizontal coordinate of the root
        """
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class BST:
    """Class which build the binary search tree, using the Node class

    Attributes
    ----------
    list_ : list
        a list with objects

    key : str
        a string with the key for the objects, which shall be used for the building process

    print : boolean
        decides whether the tree gets printed or not

    Methods
    -------
    create_tree(list_, key)
        function which builds the BST tree
    """
    def create_tree(self, list_, key, print = False):
        """Builds binary search tree and displays it

        Parameters
        ----------
        list_ : list
            a list with objects

        key : str
            a string with the key for the objects, which shall be used for the building process

        print : boolean
            decides whether the tree gets printed or not

        Returns
        -------
        top_node
            objects of class Node
        """
        if len(list_) == 1:
            return Node(getattr(list_[0], key), list_[0])

        middle = len(list_)//2
        root = Node(getattr(list_[middle], key), list_[middle])

        root.left = self.create_tree(list_[:middle], key)

        if middle + 1 < len(list_):
            root.right = self.create_tree(list_[middle+1:], key)

        if print == True:
            root.display()

        return root

        
class Time_complexity:
    """
    A class for benchmarking different sorting algorithms and plotting them
    
    Attributes
    ----------
    sorting_algorithm : function
        the sorting algorithm which shall be benchmarked
        
    sorting_algorithm_1 : function
        the first sorting_algorithm which shall be compared
        
    sorting_algorithm_2 : function
        the second sorting_algorithm which shall be compared
    
    create_function : function
        a function to create a Data Structure

    get_function : function
        the search function for the respective Data Structure

    key : str
        a string, which defines, which key of an Object is used to create the data structure

    Methods
    -------
    time_complexity_sort(sorting_algorithm)
        Calculates a dataframe containing the time complexity for different cases for sorting algorithms
    
    time_complexity_get(create_function, get_function, key)
        Calculates a dataframe containing the time complexity for different sized Data Structures and their search function

    plot()
        Plots the the time complexity of one algorithm
        
    compare_two(sorting_algorithm_1, sorting_algorithm_2)
        Displays a plot to compare two algorithms time complexity
    """
    
    def __init__(self):
        self.n_list = [1000, 2000, 4000, 8000]
        self.get_list = [10**6, 20*10**5, 40*10**5, 80*10**5]
                
    def time_complexity_sort(self, sorting_algorithm):
        """Calculates a dataframe containing the time complexity for different cases
        
        Parameters
        ----------
        sorting_algorithm : function
            the sorting algorithm for which the time complexity shall be measured
            
        Returns
        -------
        dataframe
            a dataframe which contains the different times and numbers
        """
   
        self.df = pd.DataFrame(columns = ["Randomly sorted", "Reversed sorted", "Sorted"])
        self.total_time = []
        for number in tqdm(self.n_list, desc='Iterating numbers'):
            randomly_sorted = np.random.randint(1, number + 1, number)
            reversed_sorted = np.sort(randomly_sorted)[::-1]
            sorted_ = np.sort(randomly_sorted)
            for case in tqdm([randomly_sorted, reversed_sorted, sorted_],
                             desc = f"TC for {number} & {sorting_algorithm.__name__}"):
                start = time.time()
                sorting_algorithm(case)
                total = time.time() - start
                self.total_time.append(total)
        clear_output(wait=True)
        time_list =  [self.total_time[i:i+3] for i in range(0, len(self.total_time), 3)]
        for i in range(0, len(time_list)):
            self.df.loc[i] = time_list[i]
        self.df = (self.df.assign(Algorithm = sorting_algorithm.__name__)
                   .rename(index=dict(zip(self.df.index, self.n_list))))
        return self.df
    
    def time_complexity_get(self, create_function, get_function, key):
        """Calculates a dataframe containing the time complexity for different sized Data Structures and their search function

        Parameters
        ----------
        create_function : function
            a function to create a Data Structure

        get_function : function
            the search function for the respective Data Structure

        key : str
            a string, which defines, which key of an Object is used to create the data structure

        Returns
        -------
            a dataframe which contains the different times and numbers
        """
        self.df = pd.DataFrame(columns = ["Time complexity"])
        self.total_time = {}
        for number in tqdm(self.get_list, desc = "Calculating..."):
            students = [Student(e,
                    "Max",
                    "Mustermann") for e in range(0, number)]
            tree = create_function(students, key)
            avg = 0
            start = time.time()
            for i in range(0, 16000):
                tree.get(i)
                avg += time.time() - start
            self.total_time[number] = avg / 16000
        for i in self.total_time:
            self.df.loc[i] = self.total_time[i]
        return self.df

    def plot(self):
        """Plots the the time complexity of one algorithm
        
        Raises
        ------
        NotImplementedError
            If the time complexity has not been run before
            and no dataframe is thus available.
        """

        if hasattr(self, "df") == False:
            raise NotImplementedError("Please run the function time_complexity_get() or time_complexity_sort() before!")
            
        plt.plot(self.df)
        plt.ylabel('Time in seconds')
        plt.xlabel('Length')
        plt.title("Time complexity")
            
    def compare_two(self, sorting_algorithm_1, sorting_algorithm_2):
        """Displays a plot to compare two algorithms time complexity
        
        Parameters
        ----------
        sorting_algorithm_1 : function
            the first sorting_algorithm which shall be compared
        
        sorting_algorithm_2 : function
            the second sorting_algorithm which shall be compared
        
        Returns
        -------
        dataframe
            dataframe with the different outputs per algorithm and input number
        """
        self.df_compare = (self.time_complexity(sorting_algorithm_1)
                           .append(self.time_complexity(sorting_algorithm_2)))
        fig = px.line(self.df_compare,
              x = self.df_compare.index,
              y = self.df_compare.columns,
              color = "Algorithm",
              labels = { "index": "Length", 
                        "value": "Time in seconds"},
              title = f"Time complexity - {sorting_algorithm_1.__name__} vs. {sorting_algorithm_2.__name__}")
        fig.update_layout(plot_bgcolor="white")
        fig.show(config=dict(displayModeBar=False))
        return self.df_compare