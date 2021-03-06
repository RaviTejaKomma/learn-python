__author__ = 'Kalyan'

notes = '''
Testing is another vast field of software engineering.

In this course we are going to focus on developing only one skill - white box testing.
http://en.wikipedia.org/wiki/White-box_testing

For this unit, if you see some code written by you or someone else, can you come up with a set of inputs that can test
its correctness. If the code is wrong your goal is to come with inputs that can break that code (that the spec allows).

As you will see in the code reviews, a casual approaching to testing can pass incorrect code. Having a set
of random tests written by someone is no substitute for having your own skill to investigate the correctness of your
own code.

- All good programmers are good testers too :).
- The ability to write quality code is directly related to your ability to find what can break your code.
- A good testing mindset can bring out ambiguity or gaps in the problem specification

Testing frameworks make it easy to write tests and run and reports on stats of pass/failure etc.
But coming up with meaningful tests is your job and is the main skill to develop.

You have been using py.test framework so far without knowing it :) and we will continue to use it.

Read this for an introduction:
http://pythontesting.net/framework/pytest/pytest-introduction/

Other resources on the web at this point are a waste of time. So I would suggest you to go through all the assignments
and see how we have designed the tests, how we missed some cases etc. In particular see the tests in the debugging unit.

In addition see what tests would you like to add to check your own code.
'''

unit_assignments = '''
There are 2 kinds of assignments in this unit:

1. We are going to give you a small function and some tests which pass. You job is to write additional tests to
   fail the given code and then fix the given function. Think of this as an extension to the debugging unit, where
   you write the failing tests and then debug the given code.

2. We are going to give a problem specification and you write both the code and the tests. We will run your code
   against our tests after you submit, that will give you feedback on how exhaustive your tests are. You can fix
   your code and tests and submit again.
'''