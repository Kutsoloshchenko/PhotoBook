// router for AuthModule 

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from "@angular/router";
import { AlbumComponent } from "../components/user-folder.component/album.component"


const routes: Routes = [
    {path: "albums/:username/:album", component:AlbumComponent},
]

@NgModule ({
    imports: [ RouterModule.forChild(routes)],
    exports: [ RouterModule ]
})
export class AlbumRouterModule {}