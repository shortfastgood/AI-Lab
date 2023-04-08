import { TestBed } from '@angular/core/testing';

import { LendingService } from './lending.service';

describe('LendingService', () => {
  let service: LendingService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LendingService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
