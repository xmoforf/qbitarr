# qbitarr

If you are running docker, this is a super easy way to run some basic commands on the qbit api without installing anything. Good for one-offs or quick jobs.

# Instructions

## Run as an alias

Put this in your ```.bash_aliases``` file or similar.

```bash
alias qbitarr='docker run -it --rm --network {{QBIT_NETWORK}}  ghcr.io/xmoforf/qbitarr:latest --host {{HOST_IP}} --port {{HOST_PORT}} --username {{QBIT_USERNAME}}'
```

Now you can run it like this:

```bash
qbitarr {{command}}
```

## Run with a script

See [example](launch.sh)

# Notes

**NOTE: This project is very incomplete right now and doesnt do anything yet.**

Originally I was thinking a stack language kinda like an RPN calculator:

To construct a command, start with a generic "client" on the stack. The command ```@@torrents``` is a shortcut to the API endpoint ```torrents_info``` and the @@ means it will replace the contents on the stack with the result of the function. Calling @@torrents will then result in a list of torrents to be on the stack.

```
qbitarr @@torrents
```

This prints all torrents.

To print just the names:

```
qbitarr @@torrents @@name
```

To print all torrents with name match:

```
qbitarr @@torrents @name ".*My_Torrent.*" :~ ::filter
```

Here, @name is doing the same as @@name, but it is not actually popping the @@torrent list off the stack yet. A single @ defers execution until the :~ function (deferred as ::~), which place on the stack a function that will regular expression match the torrent list to specified regex. The :filter function then accepts that function and the @@torrents .and places that filtered list back on the stack.

Stop all torrents with name match:

```
qbitarr @@torrents @name ".*My_Torrent.*" :~ ::filter @@stop
```

Replace tracker for all matching trackers:

```
qbitarr @@torrents ".*linuxisos.*" @tracker :~ ::filter "https://trackerisos2.com/announce/12345" @@edit_tracker
```

Tag torrents with no working trackers:

```
qbitarr @@torrents ::notworking "not.working" ::tag
```
