# Changelog

## 0 (dev)

### 0.5.0

Features:

* follow the playlist progression as items are played
* the --dev option enable debug logs

Internals:
* use [Hypercorn](https://pgjones.gitlab.io/hypercorn/) instead of Uvicorn as Uvicorn does not let us specify the event loop
* a lot of routes are now asynchronous
* start an async loop at app startup to listen for MPV events
* connect to MPV on startup, do not wait for first request anymore
* add some logs, mostly related to the Player and MPV management

### 0.4.1

Bugfix:
* fix migrations not running

### 0.4.0

This realease breaks again the db migrations.
You need to delete you current database and recreate one.

Features:
* auto generate configuration on startup if not given (default path to `$XDG_CONFIG_HOME/escarpolette/escarpolette.conf`)
* create the database on startup and apply any missing migrations
* youtbe-dl version bump
* fix user identification

Bugfix:
* an item with the same URL can be added again if the previous ones have been played

Internals:
* migration to [FastAPI](https://fastapi.tiangolo.com/). So long, Flask!
* no more usage of Alembic but plain SQL migrations files
* use [Uvicorn](https://www.uvicorn.org/) as web server

### 0.3.0

This release breaks the db migrations.
You need to delete your current database and recreate one.

* new model Playlist
