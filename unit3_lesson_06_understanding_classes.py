__author__ = 'Kalyan'

notes = '''
Python allows users to add user defined types via classes. This allows you to augment
builtin types like dict, list, tuple with your own types with their own specific behavior.

Like most common languages like java and c#, python supports objected oriented features
like class definitions, inheritance and polymorphism.

However, unlike java and c#, python does not insist that you have to forcibly model your
problem domain as classes if it does not make sense. You could use any mix of modules,
functions and classes to model your application. For e.g. if you goal is to code up the
fibonacci function or write a routine that sorts a sequence, defining a class
does not make sense.
'''

from placeholders import *

notes_1 = '''
 We are defining the classes in the function scope so that we can redefine them for every test.
 Generally you would define them at the module scope.

 We will use new style classes only, introduced in 2.2 and will be default in 3.x
 http://docs.python.org/2/reference/datamodel.html#new-style-and-classic-classes
'''


#classes are objects too, they have a type, have attributes, can be passed
# to functions, held in data structures etc.
def test_classes_are_objects():
    class TestQueue(object):
        """TestQueue empty class."""
        pass

    def get_attr_count(obj):
        return len(dir(obj)) ##### dir(object)--list of strings\n\nIf called without an argument, return the names in the current scope.
                             # \nElse, return an alphabetized list of names comprising (some of) the attributes\nof the given object
    #even an empty class will have 18 attribytres ------['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__',
    #  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    assert "type" == type(TestQueue).__name__ #note this.
    assert """TestQueue empty class."""== TestQueue.__doc__
    assert 18==get_attr_count(TestQueue)

def test_classes_are_callable_objects():
    class TestQueue(object):
        pass

    #classes are callable objects just like function objects
    assert True == callable(TestQueue)


def test_classes_are_object_factories():
    class TestQueue(object):
        pass

    q1 = TestQueue()  # you can 'call' a class to create an instance
    q2 = TestQueue()

    assert TestQueue == q1.__class__ ########### important ######### ####### no need to give it in double quotes
    assert TestQueue == q2.__class__

    assert False  == (q1 is TestQueue)
    assert False  == (q2 is TestQueue)
    assert False  == (q2 is q1)

    assert True == isinstance(q1, TestQueue)
    assert True == isinstance(q2, TestQueue)

    assert 18 == len(dir(TestQueue))
    assert 18 == len(dir(q1))
    assert 18 == len(dir(q2))


# if an __init__ method exists it is called with the object that is
# being created, so you can initialize it.
def test_classes_init_initializer():      ############### DOUBT ##################
    test_list = []
                                          # self returns to the instance of the class
    class TestQueue(object):
        def __init__(self):
            assert True, "Entered here !"
            test_list.append(self)

    q1 = TestQueue() # fix the assert to pass this.
    self_argument = test_list[0]
    assert True == (self_argument is q1)

def test_classes_init_with_args():
    class TestQueue(object):
        def __init__(self, name):
            self.name = name

    # note the lack of first argument, see the previous method for what is self.
    q1 = TestQueue("q1")
    q2 = TestQueue("q2")

    assert "q1" == q1.name
    assert "q2"== q2.name

    try:
        q3 = TestQueue()    ##### why it is raising an error????? -- as we have defined an argument in __init__ we should pass somethng as an arguement
    except TypeError as te : #what error do you get? ###########DOUBT##############
        pass


#just like def, class is also a runtime statement which bounds a class name with the class body code
def test_class_is_an_executable_statement():
    def create_class(value):
        if (value > 10):
            class TestQueue(object):
                def __init__(self):
                    self.name = ">10TestQueue"
        else:
            class TestQueue(object):
                def __init__(self):
                    self.name = "<=10TestQueue"

        return TestQueue

    Q_class = create_class(20)
    q1 = Q_class()
    assert ">10TestQueue" == q1.name

    Q_class = create_class(5)
    q1 = Q_class()
    assert "<=10TestQueue" == q1.name


# the self argument name is just a convention but it is
# followed widely, so don't change the name of the first argument
# this is in contrast to other languages where the instance is implicit via
# the 'this' keyword.
def test_classes_methods():     ######### important #########
    class TestQueue(object):
        def __init__(self, name):
            self.name = name
            self._TestQueue = []

        def push(self, obj):
            self._TestQueue.append(obj)

        def pop(self):
            return self._TestQueue.pop(0)

    q1 = TestQueue("q1")
    q1.push(10) #note that we pass only one argument
    assert 10 == q1.pop()

    #above is a equivalent to
    TestQueue.push(q1, 10) # self="q1",obj=10
    assert 10 == TestQueue.pop(q1)


def test_classes_bound_and_unbound_methods(): ######################## important ####################
    class TestQueue(object):
        def __init__(self, name):
            self.name = name
            self._TestQueue = []

        def push(self, obj):
            self._TestQueue.append(obj)

        def pop(self):
            return self._TestQueue.pop(0)

    q1 = TestQueue("q1")
    q1_push = q1.push

    assert False == (q1.push is TestQueue.push)

    assert  None== TestQueue.push.__self__   #unbound method
    assert q1== q1_push.__self__      #bound method, is associated with an instance

    # now understand the output of these 2 statements.
    print q1.push
    print TestQueue.push
    # make this true once you have seen the output of the prints. py.test suppresses the output of passing tests!
    assert True

def test_classes_can_have_state(): ####### important ###########
    class TestQueue(object):
        count = 0
        def __init__(self, name):
            self.name = name
            self._TestQueue = []
            TestQueue.count += 1

        def push(self, obj):
            self._TestQueue.append(obj)

        def pop(self):
            return self._TestQueue.pop(0)

    assert 0 == TestQueue.count
    q1 = TestQueue("q1")
    assert 1 == TestQueue.count
    q2 = TestQueue("q2")
    assert 2 == TestQueue.count

    # if instance has not state, it is looked up in the class.
    # generally a bad practice to access ClassState through an instance.
    assert 2 == q1.count


def test_instances_state():
    class Record(object):
        pass

    r1 = Record()
    # note that we added an attribute called name into r1 at runtime
    r1.name = "jack"

    r2 = Record()
    # note that we added an attribute called age into r2 at runtime
    r2.age = 20

    try:
        name = r2.name
        assert False, "Should not reach here"
    except AttributeError as ae: # fill up the exception you got
        assert True

    try:
        age = r1.age
        assert False, "Should not reach here"
    except AttributeError as ae : #what exception do you get?
        assert True

    r2.name = "harry"
    r1.age = 15

    assert "harry" == r2.name
    assert 15 == r1.age

    #Note that though python allows you to add instance specific
    #state, you should rarely use it as it can lead to very buggy
    #code as you deal with instances with different attributes.

    #it is always a good idea to define an init method and assign default values that cannot be given a value
    class Record2(object):
        # if for some reason you cannot fill up all attributes at construction time, give defaults like below.
        def __init__(self):
            self.name = None
            self.age = -1

notes_2 = '''
 Now that you have used classes for sometime,
 read through: http://docs.python.org/2/tutorial/classes.html
 Ignore the parts about inheritance for now.
'''

# Now create your first class based on what you have learnt.

# write a class Person with attributes name, age, weight (kgs), height (ft) and takes
# them through the constructor and exposes a method get_bmi_result()
# which returns one of "underweight", "healthy", "obese"
# http://en.wikipedia.org/wiki/Body_mass_index
class Person(object):
    def __init__(self,name,age,height,weight):
        self.weight=weight
        self.height=height
    def get_bmi_result(self):
        bmi=(int(self.weight))/(int(self.height)*0.3048)**2
        if bmi<18.5:
            return "underweight"
        elif 18.5<bmi<29:
            return "healthy"
        elif bmi>29:
            return "obese"




def test_classes_write_your_own():
    p = Person("hari", "25", "6", "30")
    assert "underweight" == p.get_bmi_result()

    p = Person("hari", "25", "6", "200")
    assert "obese" == p.get_bmi_result()

    p = Person("hari", "25", "6", "75")
    assert "healthy" == p.get_bmi_result()

three_things_i_learnt = """
-
-
-
"""