// Module that governs user sign in, sign up, password restoration

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from "@angular/http";
import { FormsModule} from '@angular/forms';


@NgModule({
    declarations: [
      UserFolderComponent      
      ],
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        AlbumRouterModule
      ],
    providers: [AlbumService],
})
export class PhotoModule{}
