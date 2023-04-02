/*
 * @(#)LoanAmortization.java 2023.1
 *
 * Copyright (c) 2023 by DPAEVD
 * All rights reserved
 */
package org.homedns.dpaevd.ai.lab.economy.loan;

import java.util.Scanner;

/**
 * This code was generated with the help of ChatGPT-4
 *
 * @author Daniele Denti (daniele.denti@bluewin.ch)
 * @version 2023.1
 * @since 2023.1
 */
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
