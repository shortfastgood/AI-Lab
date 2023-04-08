import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LendingService {

  private currentItem : CalculatorItem;

  private allCalculatorItems : CalculatorItem[];

  constructor() {
    this.allCalculatorItems = CALCULATOR_ITEMS;
    this.calculate(this.allCalculatorItems[0], 0);
    this.calculate(this.allCalculatorItems[1], 0);
    this.currentItem = this.allCalculatorItems[0];
  }

  calculate(item: CalculatorItem, timeout: number) {

    item.isPending = true;
    item.isCalculated = false;

    // the principal
    var P = item.amount;

    // the compounding frequency
    var f = item.frequency;

    // compounding length
    var cl = 12 / f;

    // compounding loops
    var clo = f * item.period ;

    // calculate the monthly rate
    var r = (item.rate / 12) / 100;

    // calculate the number of payments
    var N = item.period * 12;

    // calculate fee's rate
    var fr = item.fee / 100;

    // monthly payment
    var c = 0;
    if (r != 0) {
      c = P * r / (1 - Math.pow(1 + r, -N));
    } else {
      c = P/N;
    }

    var cip = 0, fees = 0;
    item.result = this.emptyResult();
    for (var eb = 0, ip = 0, np = 0, p = 0, peb = P, l = 1; l <= clo; l++) {
      // number of payments
      np = l * cl;
      // ending balance
      eb = Math.pow(1 + r, np) * P - ((Math.pow(1 + r, np) - 1) / r) * c;
      // principal principal paid
      p = peb - eb;
      // interest paid
      ip = c * cl - p;
      // cumulated iterest paid
      cip += ip;
      // cumulated fees paid
      fees += fr * p;
      // store the ending balance for the next loop
      peb = eb;

      var yearPayment = new YearPayment;
      yearPayment.months = cl * l;
      yearPayment.endingBalance = Math.round(eb);
      yearPayment.monthlyPayment = Math.round(c);
      yearPayment.principalPaid = Math.round(p);
      yearPayment.interestPaid = Math.round(ip);
      yearPayment.feePaid = Math.round(fr * p);
      item.result.yearPayments.push(yearPayment);
    }

    item.result.monthlyPayment = Math.round(c);
    item.result.principal = P;
    item.result.interest = Math.round(cip);
    item.result.fees = Math.round(fees);
    item.result.payments = P + Math.round(cip) + Math.round(fees);

    setTimeout(() => {item.isPending = false}, timeout);

    item.isCalculated = true;
  }

  emptyResult() : CalculationResult {
    var calculationResult = new CalculationResult();
    calculationResult.interest = 0;
    calculationResult.payments = 0;
    calculationResult.principal = 0;
    calculationResult.fees = 0;
    var yearPayments : YearPayment[] = [];
    calculationResult.yearPayments = yearPayments;
    return calculationResult;
  }

  getAllItems() : CalculatorItem[] {
    return this.allCalculatorItems;
  }

  getCurrentItem() : CalculatorItem {
    return this.currentItem;
  }

  setCurrentItem(item : CalculatorItem) {
    this.currentItem = item;
  }

  switchTo(itemNo: number) : CalculatorItem {
    this.currentItem = this.allCalculatorItems[itemNo];
    return this.currentItem;
  }
}

export class CalculatorItem {
  title : string;
  description : string;
  amount : number;
  fee : number;
  rate : number;
  period : number;
  frequency : number;
  isPending : boolean;
  isCalculated : boolean;
  result : CalculationResult;

  constructor() { 
    this.title = '';
    this.description = '';
    this.amount = 0;
    this.fee = 0;
    this.rate = 0;
    this.period = 0;
    this.frequency = 0;
    this.isPending = false;
    this.isCalculated = false;
    this.result = new CalculationResult();
  }
}

export class CalculationResult {
  principal : number;
  interest : number;
  monthlyPayment : number;
  payments : number;
  fees : number;
  yearPayments : YearPayment[];

  constructor() {
    this.principal = 0;
    this.interest = 0;
    this.monthlyPayment = 0;
    this.payments = 0;
    this.fees = 0;
    this.yearPayments = [];
  }
}

export class YearPayment {
  months : number;
  monthlyPayment : number;
  endingBalance : number;
  principalPaid : number;
  interestPaid : number;
  feePaid : number;

  constructor() {
    this.months = 0;
    this.monthlyPayment = 0;
    this.endingBalance = 0;
    this.principalPaid = 0;
    this.interestPaid = 0;
    this.feePaid = 0;
  }
}

export const CALCULATOR_ITEMS: CalculatorItem[] = [
  {title: 'Car Loan', description: 'Template for short term loan fixed rate loan.', amount: 15000, fee: 0, rate: 3.5, period: 4, frequency: 1, isPending: false, isCalculated: false, result: {principal: 0, interest: 0, monthlyPayment: 0, payments: 0, fees: 0, yearPayments: [] }},
  {title: 'House Mortgage', description: 'Template for a long term fixed rate mortgage.', amount: 150000, fee: 0, rate: 2.15, period: 10, frequency: 1, isPending: false, isCalculated: false, result: {principal: 0, interest: 0, monthlyPayment: 0, payments: 0, fees: 0, yearPayments: [] }},
  {title: 'Mortgage 1', description: 'Customer on line calculation.', amount: 50000, fee: 0, rate: 3, period: 1.5, frequency: 2, isPending: false, isCalculated: false, result: {principal: 0, interest: 0, monthlyPayment: 0, payments: 0, fees: 0, yearPayments: [] }},
  {title: 'Mortgage 2', description: 'Customer on line calculation.', amount: 200000, fee: 0, rate: 1.95, period: 20, frequency: 1, isPending: false, isCalculated: false, result: {principal: 0, interest: 0, monthlyPayment: 0, payments: 0, fees: 0, yearPayments: [] }},
  {title: 'Mortgage 3', description: 'Customer on line calculation.', amount: 350000, fee: 0, rate: 2.5, period: 10, frequency: 1, isPending: false, isCalculated: false, result: {principal: 0, interest: 0, monthlyPayment: 0, payments: 0, fees: 0, yearPayments: [] }},
]
