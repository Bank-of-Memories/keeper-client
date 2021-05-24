mkdir .tmp
cd .tmp

IPFS_VERSION='v0.6.0'
MIRROR="https://dist.ipfs.io/go-ipfs/${IPFS_VERSION}/"

FILENAME="go-ipfs_${IPFS_VERSION}_darwin-amd64.tar.gz"
EXTRACT_COMMAND='tar -zxvf'

URL=${MIRROR}${FILENAME}

curl ${URL} --output ${FILENAME} 2>&1
${EXTRACT_COMMAND} ${FILENAME} 2>&1

#cd go-ipfs
#chmod +x ./ipfs
#./ipfs init
#./ipfs daemon &