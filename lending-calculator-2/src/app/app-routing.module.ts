import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LendingViewComponent } from './lending-view.component';

const routes: Routes = [
  {path: '', redirectTo: 'lending-view', pathMatch: 'full'},
  {path: 'lending-view', component: LendingViewComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
