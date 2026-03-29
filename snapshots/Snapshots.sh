
#!/usr/bin/env bash

if ! source "${WORKSPACE}/scm/common/common.sh"; then 
    echo "[ERROR] Error to source common script."
fi

if ! source "${WORKSPACE}/scm/prepare_env/prepare_environment.sh"; then 
    echo "[ERROR] Error to source common script."
fi

snapshot_json_file="${WORKSPACE}/Snapshots/Snapshots.json"

function clone_repo() {
    for repo in $(jq -r '.[].repo' "${snapshot_json_file}"); do
        git clone "${repo}"
    done
}

function main() {
    clone_repo
}

main