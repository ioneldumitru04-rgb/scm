
#!/usr/bin/env bash

if ! source "${WORKSPACE}/scm/common/common.sh"; then 
    echo "[ERROR] Error to source common script."
fi

if ! source "${WORKSPACE}/scm/prepare_env/prepare_environment.sh"; then 
    echo "[ERROR] Error to source common script."
fi

snapshot_json_file="${WORKSPACE}/Snapshots.json"

# function clone_repo() {
#     base_repo=$(echo $REPO_SNAPSHOT | cut -d'/' -f4)
#     repo=$(echo $REPO_SNAPSHOT | cut -d'/' -f5)
#     full_repo="ssh://git@github.com/${base_repo}/${repo}"
#     git clone ${REPO_SNAPSHOT} -b ${BRANCH}
# }

function update_snapshots() {
    if [[ "${REVISION}" =~ ^[a-z0-9]{40}$ ]]; then 
        error "Issue with revision. Please check."
        exit 1
    fi
    content=$(jq --arg COMPONENT "$repo" --arg REVISION "$REVISION" '.[$COMPONENT].revision = $REVISION' ${WORKSPACE}/Snapshots.json)
    echo -E "${content}" > "${WORKSPACE}/Snapshots.json"
    cat "${WORKSPACE}/Snapshots.json"
    git_push ${BRANCH}
    popd
}


function main() {
    clone_repo
    update_snapshots
}

main