# ETH Video Downloader
Docker scripts to download videos from the ETH Zürich video portal  
  
## Current Version:  
`1.1`

## Requirements:
- Docker  
  
## Howto:  
1) Clone (or download) this repo
2) Modify the `config.json` script and add your courses.  
3) Run `docker run -v $(pwd)/downloads:/app/downloads -v $(pwd)/config.json:/app/config.json --rm pascalwacker/eth-video-downloader:version-1.1` to run the docker image directly from docker cloud
  
## Options:
In `config.json` the key `existing` accepts either `overwrite` or `skip`. Default is `skip`. `overwrite` will overwrite existing files, while `skip` skips them.
  
## Alternative (build the docker image yourself):  
1) Clone (or download) this repo
2) Modify the `config.json` script and add your courses.  
3) Run `docker build -t eth-video-downloader .`  
4) Run `docker run -v $(pwd)/downloads:/app/downloads -v $(pwd)/config.json:/app/config.json --rm eth-video-downloader`
  
## Note:
If you have permission issues in the download folder after running this script, you can add ` && sudo chown $(whoami):$(whoami) -R downloads` at the end of the `docker run` command. This will change the permission of both user and group to the current user  
  
## The "lazy" way (tested on linux):
You can also run the `run.sh` file, which will run the downloader for you (you still need to follow step 1 and 2 from the howto ;)).  
To run it, simply navigate to the folder containing it and run `sh ./run.sh`. It will ask you for your sudo password, to run the "Note" step, about file ownership!  
  
## Disclaimer:
This software is provided as is. The are not responsible for any damages on your system or legal actions brought forward against you. Only use it if you're allowed to save the videos on your hardware by ETH Zürich (http://www.video.ethz.ch/footer/copyright.html)
