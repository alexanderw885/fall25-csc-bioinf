This assignment was fairly simple, and gave me at least an initial understanding of Codon.

### Steps taken 
1. Remove references to `matplotlib` and `sys.recursionlimit`. Neither of these are natively in Codon, and are unneeded to replicate the expected behaviour, so they can be safely removed
2. Specify types for all function arguments and return values. I was getting issues with functions returning `Optional` types when they always had a return value, this helped to resolve that problem. It also gave me a much better understanding of the algorithm, as I had to go through every function and at least get a basic understanding of what it did
3. Specify dictionary types. This took me a while to understand, both in concept and in syntax. Initializing a dict with `ex = {}` gives it a key type of `NoneType`, and a value of `NoneType`. I do think this stricter typing makes the code much easier to understand, but it took a bit to get used to doing in python-like code
4. Move class attributes into the class body instead of the `__init__()` function. This also took me quite a while to catch, but I greatly prefer this method. Python lets you play way too loose with classes, this change makes classes feel much more familiar and understandable to me.
5. Make the evaluation script. This was conceptually very easy to me, but I struggle with bash syntax. This was a good opportunity to try and learn, and I feel just as confused as when I started.

The biggest gotchas were definitely class attributes and dictionaries, once they were resolved the assignment was essentially completed.