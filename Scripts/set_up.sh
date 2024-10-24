conda activate pybdy-dev
#JVM="jre-1.8.0-openjdk-1.8.0.392.b08-2.el7_9.x86_64"
#JVM="jre-1.8.0-openjdk-1.8.0.402.b06-1.el7_9.x86_64"
#JVM="jre-1.8.0-openjdk-1.8.0.412.b08-1.el7_9.x86_64"
JVM="jre-1.8.0-openjdk"
export JAVA_HOME=/usr/lib/jvm/$JVM/
export JVM_PATH=/usr/lib/jvm/$JVM/lib/amd64/server/libjvm.so
alias iniarc='eval $(ssh-agent -s); ssh-add ~/.ssh/id_rsa_archer'
