import { TestBed } from '@angular/core/testing';

import { CurrentCardDataService } from './current-card-data.service';

describe('CurrentCardDataService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CurrentCardDataService = TestBed.get(CurrentCardDataService);
    expect(service).toBeTruthy();
  });
});
