import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LoginComponent } from './login/login.component';
import { ReportingComponent } from './reporting/reporting.component';
import { TrackingComponent } from './tracking/tracking.component';
import { RegistrationComponent } from './registration/registration.component';
import { RegistrationFormComponent } from './tracker/registration-form/registration-form.component';

const routes: Routes = [
  {
    path:'',
    component: LoginComponent
  },
  {
    path:'home',
    component: AppComponent
  },
  {
    path:'dashboard',
    component: DashboardComponent
  },
  {
    path:'reporting',
    component: ReportingComponent
  },
  {
    path:'tracking',
    component: TrackingComponent
  },
  {
    path:'registration',
    component: RegistrationFormComponent
  }
  
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
