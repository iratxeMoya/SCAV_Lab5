from menu import mainMenu, videoNameMenu, renameMenu, sizeMenu
import subprocess, os


def parseFfmpeg(ffmpegQuery):

    proc = subprocess.Popen([ffmpegQuery], stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT) 
    output, err = proc.communicate() 

    output_spl = str(output).split(" ")
    videoDuration = output_spl[output_spl.index("Duration:") + 1]
    videoBitrate = output_spl[output_spl.index("bitrate:") + 1]
    nameList = output_spl[output_spl.index("title") + 1:output_spl.index("artist")]

    while("" in nameList) : 
        nameList.remove("")

    nameList.remove(":")

    name = " ".join(nameList)[:-2]

    print("Video name: " + name + "\nduration: " + videoDuration + "\nbitrate: " + videoBitrate + " kb/s")

def renameFile(newName, filepath):

    path = os.path.dirname(filepath)

    if path != "":
        path = path + "/"

    os.rename(filepath, path + newName)

def scaleVideo(videoFile, sizeW, sizeH):

    os.system("ffmpeg -i {} -vf scale={}:{} scaled.mp4".format(videoFile, sizeW, sizeH))

def changeCodec(videoFile):

    os.system("ffmpeg -i {} -codec:v mpeg2video mpeg2Video.mpg".format(videoFile))

if __name__ == "__main__":

    menu = mainMenu()
    action = menu['Action menu']

    if action == "Parse ffmpeg":

        parseFfmpeg("ffmpeg -i BBB.mp4")

    elif action == "Rename":

        videoFile = videoNameMenu()['video file']
        newName = renameMenu()['rename']

        renameFile(newName, videoFile)

    elif action == "Resize":

        videoFile = videoNameMenu()['video file']
        sizes = sizeMenu()

        W = sizes['width']
        H = sizes['height']

        scaleVideo(videoFile, W, H)

    elif action == "Change codec":

        videoFile = videoNameMenu()['video file']

        changeCodec(videoFile)
    
    else: 

        print("Please, select a correct answer")