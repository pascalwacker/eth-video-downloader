docker run -v $(pwd)/downloads:/app/downloads -v $(pwd)/config.json:/app/config.json --rm pascalwacker/eth-video-downloader:version-1.1
sudo chown $(whoami):$(whoami) -R downloads
