# credicalculator
Suppose you used to run your credit calculator via command line like this:

python credit_calc.py
Using command-line arguments you can run program this way:
python credit_calc.py --type=diff --principal=1000000 --periods=10 --interest=10

The program is supposed to work from the command line and parse the following parameters:
--type, which indicates the type of payments: "annuity" or "diff" (differentiated). 
If --type is specified neither as "annuity" nor as "diff", or it is not specified at all, show the error message.

--payment, that is a monthly payment. For --type=diff the payment is different each month, so we can't calculate 
periods or principal, therefore, its combination with --payment is invalid, too:
> python credit_calc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters
--principal is used for calculations of both types of payment. You can get its value knowing the interest, annuity payment and periods.
--periods parameter denotes the number of months and/or years needed to repay the credit. It's calculated based on the interest, annuity payment and principal.
--interest is specified without a percent sign. Note that it may accept a floating-point value. 
Our credit calculator can't calculate the interest, so these parameters are incorrect:
> python credit_calc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters
Let's make a comment. You might have noticed that for differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (missing either periods, payment or principal). Thus, when less than four parameters are given, you should display the error message too:

> python credit_calc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters
Another case when you should output this message is negative values. We can't work with these!

> python credit_calc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters
