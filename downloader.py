import io
import sys
import urllib.request as request

BUFFER_SIZE = 1024

def download_length(response, output, length):
    times = length // BUFFER_SIZE
    if length % BUFFER_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFFER_SIZE))
        print("\rDownloaded %d%%" %(((time *BUFFER_SIZE) / length) * 100), end="", flush=True)
    
def download(response, output):
    total_downloaded =0
    while True:
        data = response.read(BUFFER_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print("\rDownloaded {bytes}".format(bytes=total_downloaded), end="", flush=True)

def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("saida.zip", "w")

    content_length = response.getheader("Content-Length")
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)

    response.close()
    out_file.close()
    print("Download concluído!")

if __name__ == "__main__":
    main()