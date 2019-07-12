#Goal
* Run a simple server on rasberry pi that has a /stats endpoint to return random drone stats. 
* Other machines on same network can access the endpoint

#Steps

* turn on pi
	* Assuming that the pi can connect to internet, allows ssh, etc.
	* Will add docs on this general setup in the future.
	
* ssh into pi
	* ssh pi@*[pi ip address]*
	* Some ways to get the ip address: https://www.raspberrypi.org/documentation/remote-access/ip-address.md
	* For me it is ssh pi@10.0.0.88

* Copy over *app.py* and run it
	* *python app.py*
	* install flask if necessary (should add a requirements.txt or virtual env later)
	* Flask app should be running ...
![running](imgs/running.png?raw=true)

* GET /stats endpoint 
	* /stats url is http://*[pi ip address]*:5000/stats. 
	* For me it is http://10.0.0.88:5000/stats
	* Run a get request in postman with the url or point browser to the url
	* Should now get json with drone stats and status 200 status codes!
![postman](imgs/postman.png?raw=true)
![codes](imgs/status_codes.png?raw=true)

