# check if docker is running
docker 1> /dev/null
# success?
if [ $? -eq 0 ]; then
        # folder/file exist?
        if test -f "$2"; then
                docker container create --name paosr4KRv6R9r7Ka -v $1:/root tianon/true
                docker cp "$2" paosr4KRv6R9r7Ka:"/root/$3"
                docker rm paosr4KRv6R9r7Ka
                echo "Copied $2 to $3 in Volume $1"
        else
                echo "$2 does not exist!"
        fi
else
        echo "Docker is not running!"
fi