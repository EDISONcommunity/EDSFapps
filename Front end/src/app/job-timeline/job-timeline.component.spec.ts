import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { JobTimelineComponent } from './job-timeline.component';

describe('JobTimelineComponent', () => {
  let component: JobTimelineComponent;
  let fixture: ComponentFixture<JobTimelineComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ JobTimelineComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(JobTimelineComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
