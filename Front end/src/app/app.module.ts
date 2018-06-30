import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { SafePipe } from './cv-overview/cv-overview.component';

// External
import { MglTimelineModule } from 'angular-mgl-timeline';

// Material
import { MatProgressSpinnerModule } from '@angular/material';

// Components
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { CvOverviewComponent } from './cv-overview/cv-overview.component';
import { JobTimelineComponent } from './job-timeline/job-timeline.component';

const appRoutes: Routes = [
  {
    path: '', component: HomeComponent,
  },
  {
    path: '**',
    component: HomeComponent
  }
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CvOverviewComponent,
    JobTimelineComponent,
    SafePipe
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
    MatProgressSpinnerModule,
    MglTimelineModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
