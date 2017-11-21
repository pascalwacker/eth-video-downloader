Docker scripts to download videos from the ETH Zürich video portal  
  
Howto:  
1) Modify the `config.json` script and add your courses.  
2) Run `docker build -t eth-video-downloader .`  
3) Run `docker run -v $(pwd)/downloads:/app/downloads eth-video-downloader && sudo chown $(whoami):$(whoami) -R downloads`
  
Disclaimer: This software is provided as is. Only use it if you're allowed to save the videos on your hardware by ETH Zürich (http://www.video.ethz.ch/footer/copyright.html)