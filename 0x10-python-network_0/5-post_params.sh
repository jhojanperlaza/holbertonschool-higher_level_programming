#!/bin/bash
# POST request to the passed URL, and displays the body of the response, A variable email must be sent with the value test@gmail.com
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
