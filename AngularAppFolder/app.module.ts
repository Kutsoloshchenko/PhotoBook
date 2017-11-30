// Main module that imports all needed modules and is bootstraped 

import { BrowserModule } from '@angular/platform-browser';
import { FormsModule} from '@angular/forms';
import { NgModule } from '@angular/core';
import { HttpModule } from "@angular/http";

import { AppComponent } from './app.component';
import { TitleBar } from "./components/title-bar.component/title-bar.component";
import { PageNotFound } from "./components/page-not-found.component/page-not-found.component";

import { JWTAuthService } from "./services/jwt-auth.service"

import { AppRouterModule } from "./app-router.module";
import { AuthModule } from "./modules/auth.module/auth.module"
import { AlbumsModule } from "./modules/albums.module/albums.module"

@NgModule({
  declarations: [
    AppComponent,
    TitleBar,
    PageNotFound
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AuthModule,
    AlbumsModule,
    AppRouterModule
  ],
  providers: [JWTAuthService],
  bootstrap: [AppComponent]
})
export class AppModule { 
}
