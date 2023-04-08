import { CUSTOM_ELEMENTS_SCHEMA, Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CalculatorItem, LendingService } from './lending.service';
import { SpinnerComponent } from './spinner.component';

@Component({
  selector: 'app-lending-view',
  standalone: true,
  imports: [CommonModule, FormsModule, SpinnerComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  templateUrl: './lending-view.component.html',
  styleUrls: ['./lending-view.component.css']
})
export class LendingViewComponent {

  currentItem : CalculatorItem;

  allCalculatorItems : CalculatorItem[];

  constructor(readonly lendingService: LendingService) {
    this.allCalculatorItems = new Array<CalculatorItem>(); ;
    this.currentItem = new CalculatorItem();
  }

  calculate(timeout: number) {
    this.lendingService.calculate(this.currentItem, timeout);
  }

  switchTo(itemNo: number) {
    this.currentItem = this.lendingService.switchTo(itemNo);
  }

  ngOnInit(): void {
    this.allCalculatorItems = this.lendingService.getAllItems() ;
    this.currentItem = this.lendingService.getCurrentItem();
  }

  trackByFn(index: number, item: Object) {
    return index;
  }

}
