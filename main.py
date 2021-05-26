from subprocess import Popen, PIPE
import requests

def execute_return(cmd):
    args = cmd.split()      #Subprocess req commans split and passed
    proc = Popen(args, stdout=PIPE, stderr=PIPE)    #obj from Popen class taking args
    #fetch output and error code using communicate()
    out, err = proc.communicate()

    return out, err

#Request to Stack Exchange

def make_req(error):    
    res = requests.get("https://api.stackexchange.com/" + "/2.2/search?order=desc&sort=activity&tagged=python&intitle={}&site=stackoverflow".format(error))
    return res.json()

def getURLs(json_dict):
    urlList = []
    count = 0
    for i in json_dict["items"]:        #All keys of json
        if i["is_answered"]:            #If the question has been answered
            urlList.append(i["link"])   #Fetching the links
            count += 1
        if count == 3:
            break

    import webbrowser
    for i in urlList:
        webbrowser.open(i)


#Main

if __name__ == "__main__":
    op, err = execute_return("python test.py")
    errorMessage = err.decode("utf-8").strip().split("\r\n")[-1]

    print(errorMessage)

    if errorMessage:
        filterError = errorMessage.split(":")
        # json1 = make_req(filterError[0])        #calling makereq with filter error passing type of error 
        # json2 = make_req(filterError[1])        #calling with the errorMessage for better results
        json = make_req(errorMessage)           #3 calls to fetch the json

        # getURLs(json1)
        # getURLs(json2)
        getURLs(json)
    else:
        print("No Error !! You are a pro :P")


