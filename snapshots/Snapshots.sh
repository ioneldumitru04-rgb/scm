
#!/usr/bin/env bash

if ! source "${WORKSPACE}/scm/common/common.sh"; then 
    echo "[ERROR] Error to source common script."
fi

if ! source "${WORKSPACE}/scm/prepare_env/prepare_environment.sh"; then 
    echo "[ERROR] Error to source common script."
fi

snapshot_json_file="${WORKSPACE}/Snapshots/Snapshots.json"

function clone_repo() {
    base_repo=$(echo $REPO_SNAPSHOT | cut -d'/' -f4)
    repo=$(echo $REPO_SNAPSHOT | cut -d'/' -f5)
    full_repo="ssh://git@github.com/${base_repo}/${repo}"
    git clone ${REPO_SNAPSHOT} -b ${BRANCH}
}

function update_snapshots() {
    repo=$(echo $REPO_SNAPSHOT | cut -d'/' -f5)
    pushd "${WORKSPACE}/${repo}"
    echo $repo
    echo $REVISION
    content=$(jq --arg COMPONENT "$repo" --arg REVISION "$REVISION" '.[$COMPONENT].revision = $REVISION' ${WORKSPACE}/Snapshots/Snapshots.json)
    echo -E "${content}" > "${WORKSPACE}/Snapshots/Snapshots.json"
    popd
}


function main() {
    clone_repo
    update_snapshots
}

main