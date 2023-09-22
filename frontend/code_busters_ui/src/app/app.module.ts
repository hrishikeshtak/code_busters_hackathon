import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { TrackerComponent } from './tracker/tracker.component';
import { RegistrationFormComponent } from './tracker/registration-form/registration-form.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from  '@angular/common/http';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ReportingComponent } from './reporting/reporting.component';
import { TopnavComponent } from './topnav/topnav.component';
import { BottomnavComponent } from './bottomnav/bottomnav.component';
import { TrackingComponent } from './tracking/tracking.component';
import { RegistrationComponent } from './registration/registration.component';
import { CanvasJSAngularChartsModule } from '@canvasjs/angular-charts';
import { LoginComponent } from './login/login.component';

@NgModule({
  declarations: [
    AppComponent,
    TrackerComponent,
    RegistrationFormComponent,
    LoginComponent,
    DashboardComponent,
    ReportingComponent,
    TopnavComponent,
    BottomnavComponent,
    TrackingComponent,
    RegistrationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    NgbModule,
    ReactiveFormsModule,
    CanvasJSAngularChartsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
