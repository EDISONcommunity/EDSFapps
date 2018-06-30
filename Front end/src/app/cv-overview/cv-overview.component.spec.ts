import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CvOverviewComponent } from './cv-overview.component';

describe('CvOverviewComponent', () => {
  let component: CvOverviewComponent;
  let fixture: ComponentFixture<CvOverviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CvOverviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CvOverviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
