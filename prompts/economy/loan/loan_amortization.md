# CASE STUDY: Loan Amortization

**question**: How can you calculate the monthly payments for a loan, including interest, to be repaid within a specified period?

**answer**: To calculate the monthly payments for a loan, including interest, to be repaid within a specified period, you can use the loan amortization formula. The formula used to calculate the fixed monthly payment (M) on a loan is:

M = P * r * (1 + r)^n / ((1 + r)^n - 1)

Where:

- M is the fixed monthly payment
- P is the principal amount (the total loan amount)
- r is the monthly interest rate (annual interest rate divided by 12)
- n is the total number of payments (loan term in years multiplied by 12)

Here's a step-by-step example of calculating the monthly payment for a loan:

- Determine the principal amount (P) of the loan.
- Determine the annual interest rate (as a decimal) and divide it by 12 to get the monthly interest rate (r).
- Determine the loan term in years and multiply it by 12 to get the total number of payments (n).
- Plug P, r, and n into the formula and calculate the fixed monthly payment (M).

For example, let's say you have a loan of $10,000, an annual interest rate of 5%, and a loan term of 5 years:

- P = $10,000
- r = (5 / 100) / 12 = 0.05 / 12 = 0.004167
- n = 5 * 12 = 60
- M = 10000 * 0.004167 * (1 + 0.004167)^60 / ((1 + 0.004167)^60 - 1) ≈ $188.71
- The fixed monthly payment for this loan, including interest, would be approximately $188.71.

**command**: generate a java program using that formula

**execution**: Here's a Java program that calculates the fixed monthly payment for a loan using the loan amortization formula:

    import java.util.Scanner;

    public class LoanAmortization {

        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
    
            System.out.println("Enter the principal loan amount (P): ");
            double principal = scanner.nextDouble();
    
            System.out.println("Enter the annual interest rate (as a percentage): ");
            double annualInterestRate = scanner.nextDouble();
    
            System.out.println("Enter the loan term (in years): ");
            int loanTermYears = scanner.nextInt();
    
            double monthlyPayment = calculateMonthlyPayment(principal, annualInterestRate, loanTermYears);
    
            System.out.printf("The fixed monthly payment is: $%.2f%n", monthlyPayment);
        }
    
        public static double calculateMonthlyPayment(double principal, double annualInterestRate, int loanTermYears) {
            double monthlyInterestRate = (annualInterestRate / 100) / 12;
            int totalNumberOfPayments = loanTermYears * 12;
    
            double monthlyPayment = principal * monthlyInterestRate * Math.pow(1 + monthlyInterestRate, totalNumberOfPayments) /
                    (Math.pow(1 + monthlyInterestRate, totalNumberOfPayments) - 1);
    
            return monthlyPayment;
        }
    }

This Java program prompts the user to enter the principal loan amount, annual interest rate, and loan term in years. It then calculates the fixed monthly 
payment using the loan amortization formula and displays the result.
