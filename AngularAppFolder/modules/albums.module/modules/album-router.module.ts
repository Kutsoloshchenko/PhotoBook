// router for AuthModule 

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from "@angular/router";
import { UserFolderComponent } from "../components/user-folder.component/user-folder.component"


const routes: Routes = [
    {path: "albums/:username", component:UserFolderComponent},
]

@NgModule ({
    imports: [ RouterModule.forChild(routes)],
    exports: [ RouterModule ]
})
export class AlbumRouterModule {}