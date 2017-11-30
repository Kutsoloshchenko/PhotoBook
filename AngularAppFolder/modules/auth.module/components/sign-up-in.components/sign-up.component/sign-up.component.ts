// Component that responseble for signing user up

import { Component } from "@angular/core";
import { AuthService } from "../../../services/auth.service/auth.service";
import { ItemResponse } from "../classes/response-item";
import { InputLine } from "../classes/input-line";
import { JWTAuthService } from "../../../../../services/jwt-auth.service"
import { Router } from "@angular/router"

@Component({
    selector: "sign-up",
    templateUrl: "../sign-up-in.component.html",
    styleUrls: ["../sign-up-in.component.css"]
})
export class SignUpComponent {

    // list of input fields that component has
    components: InputLine[];

    response: ItemResponse;

    // title of the form
    title: string;

    // Constructor that initializes all lines, title and injects AuthService
    constructor(private signUpService: AuthService, private jwtService: JWTAuthService, private router: Router) {

        this.components = [  new InputLine("Email*"),
                        new InputLine("Display name*"),
                        new InputLine("Password*"),
                        new InputLine("Repeted rassword*")
                     ]
        this.title = "Sign Up Form"
    }

    
    // Function thats called when user presses button submit
    submit(){
        // get server response item
        this.signUpService.authSignUp(this.components[0].value, this.components[1].value, this.components[2].value, this.components[3].value)
                          .then(server_response => {
                              server_response
                                                           
                                      // if there is any responce
                                      if (server_response != undefined) {
                              
                                          // if request failed
                                          if (server_response.result == "Fail") {
                                              // set input lines error messages to recived error messages
                                              console.log("asdfasdf")
                                              this.components[0].error = server_response.email_error;
                                              this.components[1].error = server_response.displayNameError;
                                              this.components[2].error = server_response.password_error;
                                              this.components[3].error = server_response.repeatedPasswordError;
                                          }
                                          else {
                                              // should redirect to user verify step, but currently on prints something
                                              this.jwtService.logUserIn(server_response.username, server_response.token)
                                              this.router.navigateByUrl("albums/"+ this.jwtService.getUserName())
                                          }
                              
                                      }

                            });
                          
    }
}