__author__ = 'Kalyan'

notes = '''
Having a level head when it comes to optimizing code is one of the rarest skills in the software industry. The
world is full of software which is optimized for the wrong things or for corner cases.

Blind optimization is the root of much software evil. So getting a good perspective on this topic will serve you well
in your careers :). For now, we are only going to focus on optimizing time, same ideas hold for other resources like
memory, disk, network etc.

e.g
*problem*: If your program contains 2 functions f() and g() and you know a way to speed up f() 2 times and g() 100 times.
 Which should you change first?

*answer*: The default reaction is to answer g() :).

Commentary:

The data I gave is not sufficient to make a call :). For e.g. when you run the program it takes 10 seconds. Of that f()
takes 9.9 sec and g() takes 0.1 sec. Does it make sense to optimize g() at all? Even if you optimize it a million times,
there is no significant reduction in the program runtime (10 to 9.9 sec)!

So should we optimize f()? Again it depends :). If your customer says anything under 15 seconds is good. then optimizing
even f() is a waste of time. You are better off fixing bugs, adding features and making more money :).

So you have consider many things, not just the first level data like *problem* above describes.

Here are a few things to consider:

1. what is the end user expectation of your program?
2. what is the performance determining portion of your program? (f() in the above example)
3. Is it theoretically possible to get to your desired goal in step 1 by optimizing code in step 2?
4. Do you need a different algorithm?
5. Do you need a different design? Should you have done upfront performance planning when you designed your solution?
6. If you host the solution on the web, is it much cheaper to solve the problem by picking a bigger computer rather
   than investing in programmer time? etc.

As you can see performance optimization is a fascinating topic and you need a lot of acquired wisdom to do it well.
There is no formula and context matters a lot. Different kinds of applications and products require very
different approaches to this problem.

In this lesson, we are going to focus on measurement of small programs with a focus on 2-5

Do go through the assignments and figure out how the various profiling options you have in python. Write sample scripts
and work with them on the command line.
'''

unit_assignments = '''
Each of the assignment introduces one measurement tool. Your job is write code to measure performance using that tool
and summarize what you have learnt.
'''
