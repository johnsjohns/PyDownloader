import import
import sys
import urllib.request as request

BUFFER_SIZE = 1024

def download_lenght(response, out_file, length):
    times = lengh // BUFFER_SIZE
    if lengh % BUFFER_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFFER_SIZE))
        print("Downloaded %d" %(((time *BUFFER_SIZE) / length) * 100))
    
def download(response, output):
    total_downloaded =0
    while True:
        data = response.read(BUFFER_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print("Downloaded {bytes}".format(bytes=total_downloaded))
        
def main():
    response = request.urlopen(sys.argv[1])
    output = io.FileIO("saida.zip", "w")

    content_length = response.getheader("Content-Length")
    if content_length:
        length = int(content_length)
        download_lenght(response, out_file, lengh)
    else:
        download(response, output)

    response.close()
    out_file.close()
    print("Download concluído!")

if __main__ == "__main__":
    main()