## reactorsim

The intent of this script is to be run every 5-10 seconds with a systemd
service and associated timer unit on a linux based [EPICS](https://docs.epics-controls.org/en/latest/index.html)
SoftIOC. The simulation covers some of the signals associated 
with providing a reactor trip for a four loop pressurized 
water reactor. 

For those who like reading lots of pdfs about the arcane 
practice of building a PWR and implementing reactor trip
and ESFAS features, the source information is available 
on the NRCs site [here](https://www.nrc.gov/docs/ML1122/).

I should probably make another repo with all of the documents
on github for posterity when they notice or Westinghouse begins 
to care that those files are outward facing.

## Development

* Spin up a linux image, it can be physical, virtual, container, whatever (tested on Arch running in VMware, pretty sure it'll work on Debian too.)
* [Install EPICS](https://docs.epics-controls.org/projects/how-tos/en/latest/getting-started/installation.html) on it
    * You'll need gcc, perl, git, python3, and systemd to make the shenanigans work
* Once you can launch softIoc life is perdy good from the EPICS side
* Install reactorsim.service and reactorsim.timer to /etc/systemd/system, have to enable the timer (but not the service) with:
    systemctl enable --now reactorsim.timer
* Make another VM (tested on Debian rinning in VMware)
* [Install Phoebus](https://github.com/ControlSystemStudio/phoebus) on it
    * If you aren't a maven wizard (I'm not), you'll want to do the JAVA_HOME config in /etc/profile. Or else maven will be grumpy with you and you will spend two bewildered days wondering where maven needs JAVA_HOME even though you can call '$JAVA_HOME/bin/java -version' and '$JAVA_HOME/bin/javadoc --version'from the command line just fine.
    * If you don't care about my ramblings, /etc/profile should have:

        export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
        export PATH=${JAVA_HOME}:${PATH}

    at the end of it. I'm sure newer java's work fine but I ended up down a pretty deep rabbit hole trying to figure out what was going on here. NOTE: '/usr/lib/jvm/default' did not seem to work. I have no idea why. 
* Pull 'main.bob' down and open it with Phoebus.
* Make sure your two VMs/containers/machines can hit each other over the network

From there you should be able to fiddle with the HMI. For reactor startup:

    caput turbine:trip 1
