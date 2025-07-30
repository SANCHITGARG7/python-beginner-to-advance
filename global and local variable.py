x=10 #it is a global variable
def function():

    global x #it is a local function
    x=20

function()
print(x)
#output it prints 20 because of global function in a local funtion if it is not defined a global it would print 10 