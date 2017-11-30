// Component that responseble for signing user up

import { Component} from "@angular/core";
import { JWTAuthService } from "../../../../services/jwt-auth.service"
import { Router } from "@angular/router"
import { OnInit } from "@angular/core/src/metadata/lifecycle_hooks";

@Component({
    selector: "user-folder",
    templateUrl: "../user-folder.component.html",
    styleUrls: ["../user-folder.component.css"]
})
export class SignUpComponent implements OnInit {
    /*Name of the logged in user */
    username: string;

    albums: string[];
    
    /*Constructor in whitch jwtAuth service is injected */
    constructor(private jwtAuth: JWTAuthService){}

    ngOnInit(): void {
        
                /*Methor that is called during initialization of component*/
        
                this.username = this.jwtAuth.getUserName() // get user name first time
        
                this.jwtAuth.usernameChange.subscribe(
                (user) => this.username = user );          // subscribe to username chage to recive new one as soon as user log ins or logs out

                this.albums = this.albumsService.getAlbums()

            }



}
