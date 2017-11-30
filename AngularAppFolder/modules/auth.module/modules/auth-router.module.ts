// router for AuthModule 

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from "@angular/router";

import { MainAuthComponent } from "../components/sign-up-in.components/main-auth.component/main-auth.component"

const routes: Routes = [
    {path: "main", component:MainAuthComponent}
]

@NgModule ({
    imports: [ RouterModule.forChild(routes)],
    exports: [ RouterModule ]
})
export class AuthRouterModule {}