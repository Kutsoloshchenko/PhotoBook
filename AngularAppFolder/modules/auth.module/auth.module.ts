// Module that governs user sign in, sign up, password restoration

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from "@angular/http";
import { FormsModule} from '@angular/forms';

import { MainAuthComponent } from "./components/sign-up-in.components/main-auth.component/main-auth.component"

import { AuthService } from "./services/auth.service/auth.service"

import { AuthRouterModule } from "./modules/auth-router.module"
import { SignInComponent } from './components/sign-up-in.components/sign-in.component/sign-in.component';
import { SignUpComponent } from './components/sign-up-in.components/sign-up.component/sign-up.component';

@NgModule({
    declarations: [
      MainAuthComponent,
      SignUpComponent,
      SignInComponent
      ],
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        AuthRouterModule
      ],
    providers: [AuthService],
})
export class AuthModule{}
