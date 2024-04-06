from flask import Flask,request,jsonify
from youtube_transcript_api import YouTubeTranscriptApi as yta
from textblob import TextBlob
import numpy as np
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
import nltk
import pandas as pd
import io
import os
import unicodedata
import string
import glob
import random
import requests


app_id = "c6e4e155"
app_key = "8e66c4be8437dbbd71d0c69465e22e9d"


ALL_LETTERS = string.ascii_letters + ".,;'"

app = Flask(__name__)

dataa = [{'name':'bartek'}]

@app.route('/', methods = ['GET'])
def get_articles():
 return jsonify({"Hello":"World"})



@app.route('/video', methods=['GET', 'POST'])
def video():
    if request.method == "POST":
        #value1 = request.form["value1"]
        # value1 = request.json['value1']
        #name = request.form["name"]
        #name = request.json["name"]
        data = json.loads(request.data)
        #y = json.loads(data)
        y = json.dumps(data)
        x = json.loads(y)

        l = """{"name":"bartek"}"""
        ll = '{"name":"bartek"}'
        m = json.dumps(ll)
        n = json.loads(m)

        print("value1", data['value1'])
        print("y", y)
        print("x", x)

        print("m", m)
        print("n", n)
        #return data['value1']
        #return data
        #return y
        
        #return x
        #return m #now returns
        #return n
        return jsonify(dataa)

@app.route('/video_get', methods=['GET'])
def video_get():
    return jsonify(dataa)

@app.route('/get_split_word', methods=['GET'])
def get_split_word():
    #vid_id = "As3TT3xlddU&t=558s"
    vid_id = "xh2v5oC5Lx4"
    data = yta.get_transcript(vid_id)
    transcript = ''
    test = []
    test_val = []

    for value in data:
        for key, val in value.items():
            if key == "text":
                #print(val)
              
                #y = word_tokenize(val)
                #print(val)
              
                #if len(val) > 0:
                #    val = val[0]
                #    test.append(val)
                #if len(val) >= 0:
                #    print(val[1])
                transcript += val
                
    outPut = transcript.splitlines()
    final_output = ''.join(outPut)

    y = word_tokenize(final_output)
    #print(y)

    #for i, x in y:
    for x in y:
        test.append(x)
        #for key, val in x:
           # if key in range(0,2):
                #test.append(x)
        #test.append(x)

    print(type(test))

    #json_object = json.loads(test)
    json_object = json.dumps(test)
    print(type(json_object))

    #print(test)
    #tests = json.loads(test)

    jsonobj = json.loads(json_object)

    #print(jsonobj)
   
    ##here
    ##for element in range(0, len(jsonobj)):
    ##    print(jsonobj[element][1:])
   
   #for element in range(0, len(jsonobj)):
   #     test.append(element)
   #     print(jsonobj[element:])

   #visible on screen
   #print("test",test)

    for a in test:
       # print(a)
       
        text = nltk.word_tokenize(a)
        #jsonobject = json.dumps({'results': text})
        jsonobject = json.dumps(text)
        #print(type(jsonobject))
        tags = []
        jsonstring = json.loads(jsonobject)
        
        #print(jsonstring)
        for tag in jsonstring:
            tags.append(tag)
        
        #for i in range(len(tags)):
            #print(tags[i] + ':' + str(json[tags[i]]))
           # print(tags[i])

        #print("jsonobject", jsonobject[0])
        #print(text[0:1])
        #result = nltk.pos_tag(text)
        #print(result)
        #result = [i for i in result if i[0].lower() == a]
        #print(result[0:1])
        #print(type(result))

    for x in test:
        found = False
        answer = "No"
     #   word = "generative"
        word = "understand"
        ########print(x[0:])
     #   tmp = wn.synsets(x)[0].pos()
     #   print(tmp)
        if x == word:
            #found = True
            answer = "Yes" 
            break
    return answer



   #for item in jsonobj:
    #    print(item)

    #for item in tests:
    #    print(item)
        


    #####print(test)

    #it just divides into single characters
    #for i in final_output:
    #    a = i.splitlines()
    #    if len(a) > 0:
    #        a = a[0]
    #        test.append(a)
   
   ##    #a = i.split(',')
    ##    a = i.strip()
    ##    if len(a) > 0:
    ##        a = a[0]
    ##        test.append(a)
        
        
    #print(test)

    #######vertically writes words
    #######y = final_output.strip()
    #print(y)
    
    #######for y1 in y:
    #######    print(y1i)
        #if len(y1) > 0:
        #    test.append(y1)

    #print(test)

    #y = final_output.split(',')
    #print(y)

    
    

    #for i,a in y:
    #    return (a[i][0])


    x:string = final_output

    blob = TextBlob(x)

    blobs = blob.parse().split()
    
    #print(blobs)

    #######for blo in blobs:
      #######  return blo[0][0]
        #return blo[100][0]
        #return blo

    #ok 
    #for blo in blobs:
    #    return blo[20][0]    

    ######print(blobs[0:1][0])

    #for blobb in blob.words:
    #`    return blobb[1:2]

    #####for blobb in blob.words:
    ######    return (blobb[1:2])

    #for blobb in blob.words:
    #    for word in range(len(blob.words)):
    #            return word

    ####words = final_output.split()
    ####print(words)
    ####return words

    #return final_output
   # x:string = final_output


   

   #for i in range(len(x)):
   #         return (x[i:2])


def unicode_to_ascii(s):
    return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
            and c in ALL_LETTERS
            )


def load_data():
    print("load_data")

    words_lines = {}
    all_words = []


    def find_files(path):
        return glob.glob(path)

    def read_lines(filename):
        lines = io.open(filename, encoding='utf-8').read().strip().split('\n')
        return [unicode_to_ascii(line) for line in lines]

    for filename in find_files('words.txt'):
        words = os.path.splitext(os.path.basename(filename))[0]
        all_words.append(words)

        lines = read_lines(filename)
        words_lines[words] = lines

    return words_lines, all_words


def get_a_word_from_oxford(line):
   
    app_id = "c6e4e155"
    app_key = "8e66c4be8437dbbd71d0c69465e22e9d"

    print("line line", line)
    #line_dumps = json.dumps(line)
    #print("line_dumps", line_dumps)
    #line_dumps_split = line_dumps.split()
    #print("line_dumps_split", line_dumps_split)

    #for line in line_dumps:
    #    print("word", line[0])

    #line_loads = json.loads(line_dumps)
    #print("line_loads", line_loads[0]["word"])
    #line_loads_split = line_loads.split()
    #print("line_loads_split", line_loads_split)

    ####linee = json.dumps(line)
    ####linee_json_loads = json.loads(linee)
    ####print("linee_loads", linee_json_loads)
    ####print("linee_loads", linee_json_loads[0][0])
    ####print("linee", linee)



    ##print("line --", linee)
    #print("line --", linee[0][0])
    ##line_ini = json.loads(linee)
    ##print("line_inie", line_ini)
    ##print("line_inie", line_ini[0]["words"])


    language = 'en-gb'
    #word_id = 'Ace'
    #word_id = word
    word_id = line
    fields = 'pronunciations'
    strictMatch = 'false'

    #

    #url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
    #r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})

    #url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;
    #r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

    #url = 'https://api.dictionaryapi.dev/api/v2/entries/en/hello';
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'+word_id.lower();
    r = requests.get(url)


    print("code {}\n".format(r.status_code))
    print("text \n" + r.text)
    print("json dumps \n" + json.dumps(r.json()))
    ini_string = json.dumps(r.json())
    dataStream = json.loads(ini_string)
    print("json loads dataStream", dataStream)
    print("-- word",dataStream[0]["word"])
    print("-- meanings",dataStream[0]["meanings"])
    dataStream_definitions = dataStream[0]["meanings"]
    print("-- definitions", dataStream_definitions)
    print("-- meanings --",dataStream[0]["meanings"][0])  

    dataStream_meanings_partOfSpeech = dataStream[0]["meanings"][0]["partOfSpeech"]
    print("-- dataStream_meanings_partOfSpeech", dataStream_meanings_partOfSpeech)

    dataStream_meanings_definition = dataStream[0]["meanings"][0]["definitions"]
    print("-- dataStream_meanings_definition", dataStream_meanings_definition[0]["definition"])
    print("-- dataStream_meanings_definition_example", dataStream_meanings_definition[0]["example"])


    definitions = dataStream[0]["meanings"][0]
    print("-- d", definitions)
    print("-- phonetics",dataStream[0]["phonetics"])
    dataStream_phonetics = dataStream[0]["phonetics"]
    print("-- dataStream_phonetics", dataStream_phonetics[0]["text"])
    #dataStream_partOfSpeech = dataStream[0]["partOfSpeech"]
    #print("-- dataStream_partOfSpeech", dataStream_partOfSpeech)



    #dataStream_definitions = dataStream[0]["definitions"]
    #print("-- dataStream_definitions", dataStream_definitions)
    #definitions = dataStream[0]["definition"]
    #print("--", definitions)
    
    #print("json \n" + json.dumps(r.json()))


   #print("r.definition", r[0]["definition"])

    return r


def random_word(words_lines, all_words):

    def random_choice(a):
        random_idx = random.randint(0, len(a) - 1)
        return a[random_idx]

    word = random_choice(all_words)
    line = random_choice(words_lines[word])
    
    return word, line




@app.route('/get_every_word', methods=['GET'])
def get_every_word():
    vid_id = "As3TT3xlddU&t=558s"
    #vid_id = "xh2v5oC5Lx4"
    data = yta.get_transcript(vid_id)
    transcript = ''
    test_val = []


    #print(data)
    ini_string = json.dumps(data)
    #print(ini_string)
    #print(ini_string[0]["text"])
    dataStream = json.loads(ini_string)
    #print(dataStream)
    print("dataStream", type(dataStream))
    lenofdatastream = len(dataStream)
    print("lenofdatastream", lenofdatastream)
    print(dataStream[0]["text"])
    sentence_one = dataStream[0]["text"]
    print("sentence_one", sentence_one)
    sentence_once_list = sentence_one.split()
    print("sentence_once_list", sentence_once_list)
    sentence_once_list_first_element = sentence_once_list[0]
    print("sentence_one_list_first_element",sentence_once_list_first_element)

    #for i, text in range(data):
    #    print(text[i])

    #for text in dataStream:
    #    value = dataStream[text]
    #    print("print and valus are ({}) = ({})".format(key,value))

    for i in range(len(dataStream)):
        #print(dataStream[i]["text"])
        sentence = (dataStream[i]["text"])
        sentence_split_list = sentence.split()
        print("sentence_split_list_loop", sentence_split_list)
        for j in range(len(sentence_split_list)):
                print("sentence_split_list[j]",sentence_split_list[j])
                sentence_split_list_token = nltk.word_tokenize(sentence_split_list[j])
                print("sentence_split_list_token",sentence_split_list_token)
                postag = nltk.pos_tag(sentence_split_list_token)
                print("postag", postag)
                postagini = json.dumps(postag)
                print("postagini", postagini)
                postagini_data = json.loads(postagini)
                print("postagini_data",postagini_data)
                for k in range(len(postagini_data)):
                    print("postagini_data__",postagini_data[0][k])
                    print("postagini_data_",postagini_data[0][1])
                    word_to_write = postagini_data[0][k]
                    file_name = postagini_data[0][1]
                    array_name = postagini_data[0][1]
                    dot = "."
                    file_ext = "txt"
                    #filename = file_name + dot + file_ext
                    filename = "words" + dot + file_ext
                    print("filename", filename)
                    print("word_to_write", word_to_write)
                    
                    #arrayname = array_name

                    arrayname = []
                    
                    size = 3
                    memory = []





                    ##for a in array_name:
                    ##    arrayname.append(a)

                      ##  print("arrayname", arrayname[0][0])



                    #for arrayname in array_nam:
                    #    print("array_name", array

                    #####for i in range(len(array_name)):
                        #####arrayname.append(arrayname)

                        #####for array in arrayname:
                            #print("array", array[i][0])
                            #####print("array", array[0][0])






                    #search_string = 'new new'
                    search_string = word_to_write

                   
                    #####f = open(filename, "w")

                    #####with open(filename, "r+") as f:
                        #f.read()
                        #####f.read()
                        #####file_content = f.read()
                        #####if search_string in file_content:
                        #####    print("There is this string")
                        #####    return
                        #####else:
                        #####    print("There isn't this string")
                        #####    f.write(word_to_write+"\n")

                        #f.write("new new \n")
                        #####f.write(word_to_write+"\n")

                   #####here
                    #####with open(filename, 'r') as file:
                        #####lines = []

                        #####for line in file:
                            #####line = line.strip()
                            #####lines.append(line)
                    #####print("lines lines", lines)
                   #####here

                    ##with open(filename, "a+") as f:
                       ## f.write("\n"+word_to_write)
                       ## read i= f.readlines()
                        #print("read", read)
                        #for sentence in read:
                        #    line = sentence.split()
                        #    print("line", line)
                       ## for r in read:
                            
                       ##     print("line", r)
                       ## f.close()
                   

                
                    ##outfile = open(filename, "w")
                    ##for line in open(filename, "r"):
                    ##    if word_to_write not in line:
                    ##        outfile.write(word_to_write)
                    ##outfile.close()

                    #out = open(filename, "w")
                    #file = open(filename, "r")
                    #file_content = file.readline()
                    #if word_to_write in file_content:
                    #    print("Yes")
                    #else:
                    #    print("No")

                   
                    #removes the duplicates
                    with open(filename, "r") as f:
                        lines = dict.fromkeys(f.readlines())
                    with open(filename, "w") as f:
                        f.writelines(lines)
                    #

                    #here
                    file = open(filename, "a+")
                    
                    print("file", file.read())
                   

                    lines = file.readlines()
                    for line in lines:
                        print("line line", line)


                    #file.write(word_to_write+"\n")
                    #file.write(f"{word_to_write},{file_name}\n")
                    file.write(f"{word_to_write}\n")
                    
                    file.close() 
                    #here


    first_element_token = nltk.word_tokenize(sentence_once_list_first_element)
    print("first_element_token",first_element_token)
    postag = nltk.pos_tag(first_element_token)
    #postag_first = postag[:1]
    print(postag)
    print("type-postag",type(postag))

    postag_ini = json.dumps(postag)
    print("postag_ini",postag_ini)
    #print(postag_ini[1])
    post_init_data = json.loads(postag_ini)
    print("post_init_data",post_init_data)
    print(post_init_data[0][1].lower())

    postag_for_file = post_init_data[0][1].lower()
    print("postag_for_file", postag_for_file)

    file_name = postag_for_file
    dot = "."
    file_ext = "txt"
    filename = file_name + dot + file_ext
    print(filename)

    #file = open(filename, "a")
    
    #file = open("nn.txt", "a")
    #phrase = "lkajsd"
    #file.write("\n"+phrase)
    #file.close()

    phrase = "laksd"
    with open("text2.txt", "a") as f:
        #pass
        f.write(phrase)


    #try:
    #    with open("nn.txt", 'w') as f:
    #        f.write("Hello, World")
    #except PermissionError:
    #    print("Do not have permissions")
    print(os.stat("/home/ubuntu/bartosz/projects/dev4passion_ewordable_backend/ewordable-backend"))



    #postagsplit = postag.split()
    #print("postag-split",postagsplit)

    #ini_string_postag = nltk.pos_tag(postag)
    #print(ini_string_postag)
   
    print("sentence_once", sentence_one)
    print(dataStream[1]["text"])


    for value in data:
        for key, val in value.items():
            if key == 'text' and val == 'start':
                
                if len(val) == 12.24:
                #if val == 12.24i:
                    print(key)
                #####ini_string = json.dumps(val)
                #print(ini_string)
                #####test_val.append(ini_string)
                #print(test_val)
                
                #key = ["word"]
                #data = [dict(zip(key,json_obj)) for json_obj in ini_string]
                #jsondata = json.dumps(data)
                #print(data)

               ##### transcript += val
                transcript += key

    outPut = transcript.splitlines()
    final_output = ''.join(outPut)

    x:string = final_output

    #for i in range(len(x)):
    #    return (x[i:2])

    blob = TextBlob(x)

   #for blobb in blob.words:
   # for word in range(len(blob.words)):
       # return blobb.polarity
       # return (word[0:2])
   # return blob.words
    #return blob.words
    blobs = blob.parse().split()
  
    #######print(type(final_output))
    ini_string = json.dumps(final_output)
    print(type(ini_string))
    #json_object = json.loads(ini_string)
    json_object = json.loads(ini_string)
    
    ######key = ["word"]
    ######data = [dict(zip(key, json_obj)) for json_obj in json_object]
    ######jsondata = json.dumps(data)
    ######print(jsondata)
    
    #df = pd.read_json(json_object)
    #print(df)
    #print(json_object[0])
    #for a in json_object[0]:
        #print(a[0][0])
    #######print(type(json_object))
    #print(json_object)
    #######print(str(json_object))
    #######print(type(json_object))
    
    #######for j in json_object:
        #print(j[0][1])
        #resultt = "No"
        
        #######text = nltk.word_tokenize(j)
        #######key = ['word']

        #######data = [dict(zip(key,textt)) for textt in text]
        #######jsondata = json.dumps(data)
        #######print(data)

        #######for d in data:
            #######print(d)
            #print(d['word'][0:1])
            #print(d)

        #####print(text)
       
        #####result = nltk.pos_tag(text)
        
        #if (result == 'NN'):
        #    resultt = "Yes"
        
        #######print(text)
        #print(result)
        
        #return resultt

    #for j in range(len(json_object)):
    #    print(j)
   
    ##here
    ##for j in json_object:
    ##    for key, val in j.items():
    ##        if key == "text":
    ##            if len(val) >= [0]:
    ##                print(val[0])
       # print(j)
    #    print(j:0)
   
   #print(json_object)
    return final_output
    #return blobs
     
  #  print(blobs[16][0])
    
   ## for blo in blobs: ##here
       # return blo[4]
       
       #correct
       # return blo[94][0]
       # return blo[94][0].lower()
   

     ## return blo[16][0].lower() ##here
     
       #this piece is ok
         #wordprefix:string = blo[17][0].lower()
         #wordprefix:string = "thevideo"
         #print(wordprefix)
         #afterwordprefix:string = removeprefix(wordprefix)
         #return afterwordprefix
       #this piece is ok
    
       #  return blo


       # return blo

       # for bl in blo:
            #for b in bl:
                #return b[0][0]
            #return bl[0]
            #return bl[0][2][3]





@app.route('/get_better_captionss', methods = ['GET'])
def get_better_captionss():
    vid_id = "As3TT3xlddU&t=558s"
    data = yta.get_transcript(vid_id)
    transcript = ''

    for value in data:
        for key, val in value.items():
            if key == 'text':
               transcript += val

    outPut = transcript.splitlines()
    final_output = ''.join(outPut)

   #print_type
   # print(type(final_output))

    x:string = final_output

    print(len(x))

    #worked
    text = "The titular threat of The Blob has always struck me as the ultimate movie "
    
    #text = text.read()
    #array_string = np.array(final_output)
    #blob = TextBlob(array_string)

    #worked
    # blob = TextBlob(text)
    blob = TextBlob(x)

    #worked
    #return blob.words
    return blob.words
    #return blob.correct
 
# return text


    #b = str("Machin Learnin")
    #x = TextBlob(b)
    #return x.correct()
    
    #return b.tags



@app.route('/get_better_captions', methods = ['GET'])
def get_better_captions():
    vid_id = "As3TT3xlddU&t=558s"
    data = yta.get_transcript(vid_id)
    transcript = ''

    for value in data:
        for key, val in value.items():
            if key == 'text':
               transcript += val

    outPut = transcript.splitlines()
    final_output = ''.join(outPut)
    #return final_output
    x = str(final_output)
    #return x

   # b = TextBlob(final_output)
   # return b.correct()
    b = TextBlob(x)
    #return b.correct()
    return TextBlob("")
    


@app.route('/get_captions', methods = ['GET'])
#@app.route('/get_captions'methods = ['GET'])
def get_captions():
    vid_id = "As3TT3xlddU&t=558s"
    data = yta.get_transcript(vid_id)
    transcript = ''

    for value in data:
        for key, val in value.items():
            if key == 'text':
               transcript += val

    outPut = transcript.splitlines() 
    final_output = ''.join(outPut)

#print(final_output)

    return final_output


if __name__ == "__main__":

  words_lines, all_words = load_data()
  word, line = random_word(words_lines, all_words)
  print("words_lines", words_lines)
  print("all_words", all_words)

  print("word", word)
  print("line", line)
  get_a_word_from_oxford(line)

  # app.run(debug=True)
  # app.run(host='0.0.0.0', port=5000)
  app.run(host='0.0.0.0', port=5000)
