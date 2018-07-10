docker run -v $(pwd)/downloads:/app/downloads pascalwacker/eth-video-downloader:version-1.0
sudo chown $(whoami):$(whoami) -R downloads
