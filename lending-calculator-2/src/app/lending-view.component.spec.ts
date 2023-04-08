import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LendingViewComponent } from './lending-view.component';

describe('LendingViewComponent', () => {
  let component: LendingViewComponent;
  let fixture: ComponentFixture<LendingViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ LendingViewComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LendingViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
