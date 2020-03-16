# twig-code-challenge

Please find here my solution for the twig education coding challenge.

For this challenge I have made the assumption that the values in the arrays are not of any specific type i.e. they all integers.

The solution has 2 files the codechallenge.py file which contains the function to run the solution, and test_codechallenge.py file which is a unit test file with some unit test within.

To run the solution:

I assume that Python 3 is installed on the machine running the code. 
 
    • From the directory containing the solution files, open a terminal from that location
    • To run the main solution file use the command
        ◦ python3 codechallenge.py <comma seperated values> <size of arrays to be made>
        ◦ for example:
            ▪ python3 codechallenge.py 1,2,3,4,5 3
    • To Execute the UnitTest file run the following command
        ◦ python3 -m unittest test_codechallenge.py


The solution is taking in the array of values and the size value and creating a new list based on these values. The create_split_array() function is using these values, utalising the divmod() function and a list generatior in which to create the desired combination of lists within the the main list.

Thank you for your time and consideration of this solution, Python is not my main language but I have enjoyed getting reaquated with it working on this solution.
 


