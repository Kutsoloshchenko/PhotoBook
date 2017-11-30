// Module that governs user sign in, sign up, password restoration

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from "@angular/http";
import { FormsModule} from '@angular/forms';

import { AuthRouterModule } from "./modules/auth-router.module"

@NgModule({
    declarations: [
        
      ],
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        AuthRouterModule
      ],
    providers: [],
})
export class AuthModule{}
