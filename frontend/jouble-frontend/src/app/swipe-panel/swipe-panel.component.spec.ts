import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SwipePanelComponent } from './swipe-panel.component';

describe('SwipePanelComponent', () => {
  let component: SwipePanelComponent;
  let fixture: ComponentFixture<SwipePanelComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SwipePanelComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SwipePanelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
