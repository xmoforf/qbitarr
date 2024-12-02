#!/bin/bash

# Place default option values here
declare -A options_map=(
    ["--host"]=""
    ["--port"]=""
    ["--username"]=""
)
declare -A docker_options_map=(
    ["--network"]=""
)

build_options() {
    local -n assoc_array=$1
    for key in "${!assoc_array[@]}"; do
        if [ -n "${assoc_array[$key]}" ]; then
            printf "%s %s " "$key" "${assoc_array[$key]}"
        fi
    done
}

echo docker run -it --rm $(build_options docker_options_map) \
    ghcr.io/xmoforf/qbitarr:latest \
    $(build_options options_map) \
    "$@"