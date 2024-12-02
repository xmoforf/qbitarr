# qbitarr

If you are running docker, this is a super easy way to run some basic commands on the qbit api without installing anything. Good for one-offs or quick jobs.

# Instructions

## Run as an alias

Put this in your ```.bash_aliases``` file or similar.

```bash
alias qbitarr='docker run -it --rm --network npm_net ghcr.io/xmoforf/qbitarr:latest --host {{HOST_IP}} --port {{HOST_PORT}} --username {{QBIT_USERNAME}}'
```

Now you can run it like this:

```bash
qbitarr {{command}}
```

## Run with a script

See [example](launch.sh)
