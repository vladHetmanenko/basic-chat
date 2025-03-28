dev_start:
	cd server_a && daphne -b 127.0.0.1 -p 8000 server_a.asgi:application

ngrok_start:
	ngrok http 8000