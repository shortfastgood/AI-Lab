import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'css3-spinner',
  standalone: true,
  imports: [CommonModule],
  template: `
<div class="css3-spinner css3-spinner-balls-increase">
  <div class="css3-spinner-bar1"></div>
  <div class="css3-spinner-bar2"></div>
  <div class="css3-spinner-bar3"></div>
  <div class="css3-spinner-bar4"></div>
  <div class="css3-spinner-bar5"></div>
  <div class="css3-spinner-bar6"></div>
  <div class="css3-spinner-bar7"></div>
  <div class="css3-spinner-bar8"></div>
</div>  `,
  styleUrls: ['./spinner.component.css']
})
export class SpinnerComponent {

}
