import torch
import torch.nn as nn
from abc import ABC, abstractmethod

# 1. Viết class và cài phương thức softmax


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


class StableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x, dim=0)
        x_exp = torch.exp(x - c.values)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
print(output)

my_softmax = MySoftmax()
output = my_softmax(torch.Tensor([1, 2, 3000000000]))
print(output)

stable_softmax = StableSoftmax()
output = stable_softmax(torch.Tensor([1, 2, 3]))
print(output)


# 2. Tạo class Person và các class con Student, Doctor, Teacher
class Person(ABC):
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"I am: {self.name} and I am: {self.yob} years old - Grade: {self.__grade}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"I am: {self.name} and I am: {self.yob} years old - Specialist: {self.__specialist}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"I am: {self.name} and I am: {self.yob} years old - Subject: {self.__subject}")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = []

    def add_person(self, person):
        self.__list_people.append(person)

    def remove_person(self, person):
        self.__list_people.remove(person)

    def describe(self):
        print(f"Ward: {self.__name}")
        for person in self.__list_people:
            person.describe()

    def list_people(self):
        return self.__list_people

    def count_doctor(self):
        count = 0
        for person in self.__list_people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_yob(self):
        return sorted(self.__list_people, key=lambda x: x.yob)

    def compute_average(self):
        total = 0
        count = 0
        for person in self.__list_people:
            if isinstance(person, Teacher):
                count += 1
                total += person.yob
        return total / len(self.__list_people) if count > 0 else 0


student1 = Student("Nam", 2001, 10)
doctor1 = Doctor("Nam", 2001, "Medicine")
doctor2 = Doctor("Hung", 2002, "Medicine2")

ward1 = Ward("Ward1")
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.add_person(student1)
ward1.describe()
print(ward1.list_people())
print("Number of doctors:", ward1.count_doctor())
print("Sorted list by year of birth:", ward1.sort_yob())


# 3. Thực hiện xây dựng class Stack với các phương thức
class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__list = []

    def is_empty(self):
        return len(self.__list) == 0

    def is_full(self):
        return len(self.__list) == self.__capacity

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")
        else:
            self.__list.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__list.pop()

    def top(self):
        if not self.is_empty():
            return self.__list[-1]


my_stack = MyStack(3)
print("Is stack empty?", my_stack.is_empty())
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print("Top element:", my_stack.top())
print("Popped element:", my_stack.pop())
print("Is stack full?", my_stack.is_full())


# 4. Thực hiện xây dựng class Queue với các chức năng
class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full")
        else:
            self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self.__queue.pop(0)


my_queue = MyQueue(5)
print("Is queue empty?", my_queue.is_empty())
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
print("Dequeued element:", my_queue.dequeue())
print("Is queue full?", my_queue.is_full())
