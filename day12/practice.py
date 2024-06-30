# Scope:
#         this tells which variables can be accessed locally, i.e within a function and which variables can be accessed globally, i.e throughout the code
#         global scope = accessible to all
#         local scope = accessible locally

# there is no block scope in python, only functions create local and global scopes

# modifying global scope : we can create a local variable inside a function with the same name as the global scope, but it is bad practice to have the same name for global and local variables
# to modify the global variable, we can use "global 'variable_name'", this allows changes in the global variable inside the function
# but avoiding changing the global variable is good practice

# if we have to change global variable for a particular reason, we can use 'return' statements to change the value of global variable within a function and return it and use the function as the changed global variable, that way, the global variable is not changed explicitly but by using functions

# Global Constants : they are variables that are made to never change in the code
