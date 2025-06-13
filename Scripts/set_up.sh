conda activate pybdy-clean2
#conda activate pybdy-dev
#JVM="jre-1.8.0-openjdk-1.8.0.392.b08-2.el7_9.x86_64"
#JVM="jre-1.8.0-openjdk-1.8.0.402.b06-1.el7_9.x86_64"
#JVM="jre-1.8.0-openjdk-1.8.0.412.b08-1.el7_9.x86_64"
#JVM="jre-11-openjdk-11.0.24.0.8-2.el9.x86_64"
#JVM="java-1.8.0-openjdk-1.8.0.412.b08-1.el7_9.x86_64"

JVM="jre-11"
#JVM="jre-1.8.0"
#JVM="jre-1.8.0-openjdk"
#JVM="java-1.8.0-openjdk-1.8.0.412.b08-1.el7_9.x86_64"
#JVM="jre"
#JVM="jre-1.8.0"
#JVM="jre-1.8.0-openjdk-1.8.0.412.b08-1.el7_9.x86_64"
#JVM="jre-openjdk"

#JVM=java-1.8.0-openjdk-1.8.0.412.b08-1.el7_9.x86_64
#JVM=jre
#JVM=jre-1.8.0
#JVM=jre-1.8.0-openjdk
#JVM=jre-1.8.0-openjdk-1.8.0.412.b08-1.el7_9.x86_64
#JVM=jre-openjdk

JVM="jre-17"

export JAVA_HOME=/usr/lib/jvm/$JVM/
#export JVM_PATH=/etc/alternatives/jre_openjdk/lib/server/libjvm.so
#export JVM_PATH=/usr/lib/jvm/$JVM/lib/amd64/server/libjvm.so
#export JVM_PATH=/usr/lib/jvm/jre-11/lib/server/libjvm.so
#export JVM_PATH=/usr/lib/jvm/$JVM/lib/server/libjvm.so
#export JVM_PATH=/usr/lib/jvm/java-11-openjdk-11.0.24.0.8-2.el9.x86_64/bin/java
alias iniarc='eval $(ssh-agent -s); ssh-add ~/.ssh/id_rsa_archer'
