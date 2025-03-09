pgup:
	podman run -d --name test-postgres -p 5432:5432 localhost/test-postgres