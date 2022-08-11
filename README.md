## reactorsim

The intent of this script is to be run every 5-10 seconds with a systemd
service and associated timer unit on a linux based [EPICS](https://docs.epics-controls.org/en/latest/index.html)
SoftIOC. The simulation covers some of the signals associated 
with providing a reactor trip for a four loop pressurized 
water reactor. 

For those who like reading lots of pdfs about the arcane 
practice of building a PWR and implementing reactor trip
and ESFAS features the source information is available 
on the NRCs site [here](https://www.nrc.gov/docs/ML1122/).

I should probably make another repo with all of the documents
on github for posterity when they notice those files are 
outward facing.
'''