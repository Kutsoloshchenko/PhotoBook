// Component that responseble for signing user up

import { Component} from "@angular/core";
import { JWTAuthService } from "../../../../services/jwt-auth.service"
import { PhotoService } from "../../services//photo.service"
import { Router } from "@angular/router"
import { OnInit } from "@angular/core/src/metadata/lifecycle_hooks";
import { Photo } from '../../classes/photo';

@Component({
    selector: "user-folder",
    templateUrl: "./user-folder.component.html",
    styleUrls: ["./user-folder.component.css"]
})
export class AlbumComponent implements OnInit {
    /*Name of the logged in user */
    username: string;

    album: string;

    Photos: Photo[];

    create_photo_name: string;
    
    /*Constructor in whitch jwtAuth service is injected */
    constructor(private jwtAuth: JWTAuthService, private photoService: PhotoService){}

    ngOnInit(): void {
        
                /*Methor that is called during initialization of component*/
        
                this.username = this.jwtAuth.getUserName() // get user name first time
        
                this.jwtAuth.usernameChange.subscribe(
                (user) => this.username = user );          // subscribe to username chage to recive new one as soon as user log ins or logs out

            }

    getAlbums(): void{

        this.albumService.GetUserAlbums(this.username, this.jwtAuth.getToken())
        .then(server_responce => 
         { console.log(server_responce)
            this.albums = server_responce;
         })
        }

    changeFolderName(folder_name: string, new_name: string): void{

        this.albumService.ChangeUserAlbums(this.username, this.jwtAuth.getToken(), folder_name, new_name)
                         .then(server_responce => {
                             if (server_responce.result == "Ok")
                             {
                                this.getAlbums()
                             }
                             else {
                                 console.log(server_responce.error_message)
                             }
                            })
    }

    deleteFolder(folder_name: string): void{
        
        console.log(folder_name)

                this.albumService.DeleteAlbum(this.username, this.jwtAuth.getToken(), folder_name)
                                 .then(server_responce => {
                                     if (server_responce.result == "Ok")
                                     {
                                        this.getAlbums()
                                     }
                                     else {
                                         console.log(server_responce.error_message)
                                     }
                                    })
            }

    CreateAlbum(): void{
                
                this.albumService.CreateAlbum(this.username, this.jwtAuth.getToken(), this.create_album_name)
                                  .then(server_responce => {
                                             if (server_responce.result == "Ok")
                                             {
                                                this.getAlbums()
                                             }
                                             else {
                                                 console.log(server_responce.error_message)
                                             }
                                            })
                    }
        

}
